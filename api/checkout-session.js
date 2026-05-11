let stripe = null;
const STRIPE_SECRET_KEY = process.env.STRIPE_SECRET_KEY || '';
if (STRIPE_SECRET_KEY) {
  stripe = require('stripe')(STRIPE_SECRET_KEY);
}

module.exports = async function handler(req, res) {
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });

  if (!stripe) {
    return res.status(503).json({ error: 'Stripe is not configured' });
  }

  const sessionId = req.query.session_id;
  if (!sessionId || typeof sessionId !== 'string' || !sessionId.startsWith('cs_')) {
    return res.status(400).json({ error: 'Valid session_id is required' });
  }

  try {
    const session = await stripe.checkout.sessions.retrieve(sessionId);
    return res.status(200).json({
      customerEmail: session.customer_details?.email || null,
      productName: session.metadata?.product_name || 'Your product',
      productSlug: session.metadata?.product_slug || null,
      amountTotal: session.amount_total,
      currency: session.currency,
      paymentStatus: session.payment_status,
    });
  } catch (err) {
    console.error('Session retrieval error:', err.message);
    return res.status(404).json({ error: 'Session not found' });
  }
};
