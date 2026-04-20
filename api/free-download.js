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

  // Log the lead capture
  console.log('Free download lead:', {
    email: cleanEmail,
    name: typeof name === 'string' ? name.trim().substring(0, 200) : '',
    slug: slug.substring(0, 200),
    source: 'free-download',
    subscribedAt: new Date().toISOString(),
  });

  return res.status(200).json({
    message: 'Success! Your download is ready.',
    downloadUrl: `/downloads/${encodeURIComponent(slug)}.md`,
    productTitle: slug.replace(/^\d+-/, '').replace(/-/g, ' '),
  });
};
