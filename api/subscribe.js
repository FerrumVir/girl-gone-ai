const fs = require('fs');
const path = require('path');

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

  const { email, source, productSlug } = req.body || {};
  const cleanEmail = (email || '').trim().toLowerCase();

  if (!isValidEmail(cleanEmail)) {
    return res.status(400).json({ error: 'Invalid email address' });
  }

  // In serverless, we can't persist to a local file.
  // Log the subscription for now — production should use a database or email service.
  console.log('New subscriber:', {
    email: cleanEmail,
    source: typeof source === 'string' ? source.substring(0, 200) : 'unknown',
    productSlug: typeof productSlug === 'string' ? productSlug.substring(0, 200) : null,
    subscribedAt: new Date().toISOString(),
  });

  return res.status(201).json({
    message: "You're on the list! We'll notify you when we launch.",
  });
};
