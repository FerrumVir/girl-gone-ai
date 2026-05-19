const BACKEND_URL = process.env.BACKEND_URL || '';

function isValidEmail(email) {
  return typeof email === 'string' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, name, slug } = req.body || {};
  const cleanEmail = (email || '').trim().toLowerCase();

  if (!isValidEmail(cleanEmail)) {
    return res.status(400).json({ error: 'Invalid email address' });
  }

  if (!slug || typeof slug !== 'string') {
    return res.status(400).json({ error: 'Product slug is required' });
  }

  // Log the lead capture (always captured in Vercel function logs)
  console.log('Free download lead:', {
    email: cleanEmail,
    name: typeof name === 'string' ? name.trim().substring(0, 200) : '',
    slug: slug.substring(0, 200),
    source: 'free-download',
    subscribedAt: new Date().toISOString(),
  });

  // Forward to backend if configured (persists to subscribers.json + triggers drip)
  if (BACKEND_URL) {
    try {
      const resp = await fetch(`${BACKEND_URL}/free-download`, {
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

  return res.status(200).json({
    message: 'Success! Your download is ready.',
    downloadUrl: `/downloads/files/${encodeURIComponent(slug)}.html`,
    productTitle: slug.replace(/^\d+-/, '').replace(/-/g, ' '),
  });
};
