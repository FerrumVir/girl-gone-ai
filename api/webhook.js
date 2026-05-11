let stripe = null;
const STRIPE_SECRET_KEY = process.env.STRIPE_SECRET_KEY || '';
const STRIPE_WEBHOOK_SECRET = process.env.STRIPE_WEBHOOK_SECRET || '';
if (STRIPE_SECRET_KEY) {
  stripe = require('stripe')(STRIPE_SECRET_KEY);
}

// Vercel needs raw body for webhook signature verification
module.exports.config = { api: { bodyParser: false } };

function getRawBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on('data', chunk => chunks.push(chunk));
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end('Method not allowed');

  if (!stripe) {
    return res.status(503).end('Stripe not configured');
  }

  const rawBody = await getRawBody(req);
  const sig = req.headers['stripe-signature'];
  let event;

  if (STRIPE_WEBHOOK_SECRET && sig) {
    try {
      event = stripe.webhooks.constructEvent(rawBody, sig, STRIPE_WEBHOOK_SECRET);
    } catch (err) {
      console.error('Webhook signature verification failed:', err.message);
      return res.status(400).end('Webhook signature verification failed');
    }
  } else {
    try {
      event = JSON.parse(rawBody.toString());
    } catch {
      return res.status(400).end('Invalid JSON');
    }
  }

  // Forward to Railway backend for order storage + email delivery
  const BACKEND_URL = process.env.BACKEND_URL || 'https://api-production-e5a9.up.railway.app';
  try {
    await fetch(`${BACKEND_URL}/webhook`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: rawBody.toString(),
    });
  } catch (err) {
    console.error('Backend webhook forward failed:', err.message);
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    console.log('Sale completed:', {
      sessionId: session.id,
      email: session.customer_details?.email,
      product: session.metadata?.product_name,
      amount: session.amount_total,
      currency: session.currency,
    });
  }

  return res.status(200).json({ received: true });
};
