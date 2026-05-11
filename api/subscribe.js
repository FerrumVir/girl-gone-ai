const BACKEND_URL = process.env.BACKEND_URL || '';

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { email, source, productSlug } = req.body || {};

  // Log subscriber for Vercel function logs (always captured)
  console.log('New subscriber:', {
    email: typeof email === 'string' ? email.trim().toLowerCase() : '',
    source: source || 'unknown',
    productSlug: productSlug || '',
    subscribedAt: new Date().toISOString(),
  });

  // Forward to backend if configured and reachable
  if (BACKEND_URL) {
    try {
      const resp = await fetch(`${BACKEND_URL}/subscribe`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(req.body),
      });
      const data = await resp.json();
      return res.status(resp.status).json(data);
    } catch (err) {
      console.error('Backend proxy error:', err.message);
    }
  }

  return res.status(201).json({ message: "You're on the list!" });
};
