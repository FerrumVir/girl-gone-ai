const fs = require('fs');
const path = require('path');

let stripe = null;
const STRIPE_SECRET_KEY = process.env.STRIPE_SECRET_KEY || '';
if (STRIPE_SECRET_KEY) {
  stripe = require('stripe')(STRIPE_SECRET_KEY);
}

function loadCatalog() {
  const catalogPath = path.join(__dirname, '..', 'products', 'catalog.json');
  try {
    return JSON.parse(fs.readFileSync(catalogPath, 'utf8'));
  } catch {
    return [];
  }
}

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  if (!stripe) {
    return res.status(503).json({ error: 'Stripe is not configured.' });
  }

  const { slug } = req.body || {};
  if (!slug || typeof slug !== 'string') {
    return res.status(400).json({ error: 'Product slug is required' });
  }

  const catalog = loadCatalog();
  const product = catalog.find(p => p.slug === slug);
  if (!product) {
    return res.status(404).json({ error: 'Product not found' });
  }

  const priceInCents = Math.round(product.price * 100);
  if (priceInCents <= 0) {
    return res.status(400).json({ error: 'Invalid product price' });
  }

  const origin = req.headers.origin || req.headers.referer?.replace(/\/[^/]*$/, '') || 'https://girlgone.ai';

  try {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [{
        price_data: {
          currency: 'usd',
          product_data: {
            name: product.title,
            metadata: { slug: product.slug },
          },
          unit_amount: priceInCents,
        },
        quantity: 1,
      }],
      mode: 'payment',
      success_url: `${origin}/success.html?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${origin}/${slug.includes('bundle') || slug === 'complete-collection' || slug === 'freelancer-starter-kit' || slug === 'small-business-essential-pack' ? 'bundles' : 'products'}/${encodeURIComponent(slug)}.html`,
      metadata: {
        product_slug: product.slug,
        product_name: product.title,
      },
    });

    return res.status(200).json({ url: session.url });
  } catch (err) {
    console.error('Stripe session creation error:', err.message);
    return res.status(500).json({ error: 'Failed to create checkout session' });
  }
};
