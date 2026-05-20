// Email signup handler.
// Auto-detects which ESP to call based on env vars. Falls back to console log.
//
// Configure ONE of these on Vercel:
//   CONVERTKIT_API_KEY + CONVERTKIT_FORM_ID
//   MAILCHIMP_API_KEY + MAILCHIMP_LIST_ID + MAILCHIMP_SERVER_PREFIX  (e.g. us21)
//   BEEHIIV_API_KEY + BEEHIIV_PUBLICATION_ID
//   RESEND_API_KEY + RESEND_AUDIENCE_ID

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function isValidEmail(email) {
  return typeof email === 'string' && email.length <= 254 && EMAIL_RE.test(email);
}

async function sendToConvertKit(email, source) {
  const apiKey = process.env.CONVERTKIT_API_KEY;
  const formId = process.env.CONVERTKIT_FORM_ID;
  if (!apiKey || !formId) return null;
  const resp = await fetch(`https://api.convertkit.com/v3/forms/${formId}/subscribe`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ api_key: apiKey, email, tags: source ? [source] : undefined }),
  });
  return { provider: 'convertkit', ok: resp.ok, status: resp.status };
}

async function sendToMailchimp(email, source) {
  const apiKey = process.env.MAILCHIMP_API_KEY;
  const listId = process.env.MAILCHIMP_LIST_ID;
  const prefix = process.env.MAILCHIMP_SERVER_PREFIX;
  if (!apiKey || !listId || !prefix) return null;
  const resp = await fetch(`https://${prefix}.api.mailchimp.com/3.0/lists/${listId}/members`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: 'Basic ' + Buffer.from('anystring:' + apiKey).toString('base64'),
    },
    body: JSON.stringify({
      email_address: email,
      status: 'subscribed',
      tags: source ? [source] : [],
    }),
  });
  // 400 with "Member Exists" is fine
  const ok = resp.ok || resp.status === 400;
  return { provider: 'mailchimp', ok, status: resp.status };
}

async function sendToBeehiiv(email, source) {
  const apiKey = process.env.BEEHIIV_API_KEY;
  const pubId = process.env.BEEHIIV_PUBLICATION_ID;
  if (!apiKey || !pubId) return null;
  const resp = await fetch(`https://api.beehiiv.com/v2/publications/${pubId}/subscriptions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      email,
      reactivate_existing: false,
      send_welcome_email: true,
      utm_source: source || 'website',
    }),
  });
  return { provider: 'beehiiv', ok: resp.ok, status: resp.status };
}

async function sendToResend(email) {
  const apiKey = process.env.RESEND_API_KEY;
  const audienceId = process.env.RESEND_AUDIENCE_ID;
  if (!apiKey || !audienceId) return null;
  const resp = await fetch(`https://api.resend.com/audiences/${audienceId}/contacts`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({ email, unsubscribed: false }),
  });
  return { provider: 'resend', ok: resp.ok, status: resp.status };
}

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const body = req.body || {};
  const email = typeof body.email === 'string' ? body.email.trim().toLowerCase() : '';
  const source = typeof body.source === 'string' ? body.source.slice(0, 200) : 'unknown';
  const productSlug = typeof body.productSlug === 'string' ? body.productSlug.slice(0, 200) : '';

  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Please enter a valid email address.' });
  }

  // Always log so signups aren't silently lost while ESP integration is being wired up
  console.log('New subscriber:', { email, source, productSlug, at: new Date().toISOString() });

  // Try whichever ESP is configured. First non-null wins.
  let result = null;
  try {
    result =
      (await sendToConvertKit(email, source)) ||
      (await sendToMailchimp(email, source)) ||
      (await sendToBeehiiv(email, source)) ||
      (await sendToResend(email));
  } catch (err) {
    console.error('ESP error:', err.message);
  }

  if (result && !result.ok) {
    console.error('ESP rejected signup:', result);
    // Don't leak provider errors to user — keep UX clean and let logs surface issues
    return res.status(201).json({ message: "You're on the list!" });
  }

  return res.status(201).json({
    message: "You're on the list!",
    provider: result?.provider || null,
  });
};
