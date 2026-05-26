const fs = require('fs');
const path = require('path');

const FEEDBACK_FILE = path.join('/tmp', 'girlgone-task-feedback.json');

function loadFeedback() {
  try {
    return JSON.parse(fs.readFileSync(FEEDBACK_FILE, 'utf8'));
  } catch {
    return { actions: [], productScores: {} };
  }
}

function saveFeedback(data) {
  fs.writeFileSync(FEEDBACK_FILE, JSON.stringify(data, null, 2));
}

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') return res.status(204).end();

  // GET — return product scores for daily-tasks to read
  if (req.method === 'GET') {
    const fb = loadFeedback();
    return res.status(200).json({ productScores: fb.productScores });
  }

  // POST — record a task action from Jaci
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { taskId, title, action, message, product, slug, timestamp } = req.body || {};

  if (!action || !taskId) {
    return res.status(400).json({ error: 'taskId and action required' });
  }

  const fb = loadFeedback();

  // Store the raw action
  fb.actions.push({
    taskId,
    title: (title || '').substring(0, 200),
    product: (product || '').substring(0, 200),
    slug: (slug || '').substring(0, 200),
    action, // done, replied, ignored
    message: (message || '').substring(0, 500),
    timestamp: timestamp || new Date().toISOString(),
  });

  // Keep last 500 actions max
  if (fb.actions.length > 500) {
    fb.actions = fb.actions.slice(-500);
  }

  // Update product scores
  // Score system: done = +2, replied = +1, ignored = -2
  // Products Jaci consistently completes get promoted; ignored ones get suppressed
  const key = slug || product || title || '';
  if (key) {
    if (!fb.productScores[key]) {
      fb.productScores[key] = { score: 0, done: 0, replied: 0, ignored: 0, lastSeen: '' };
    }
    const ps = fb.productScores[key];
    ps.lastSeen = new Date().toISOString().slice(0, 10);

    if (action === 'done') {
      ps.score += 2;
      ps.done++;
    } else if (action === 'replied') {
      ps.score += 1;
      ps.replied++;
    } else if (action === 'ignored') {
      ps.score -= 2;
      ps.ignored++;
    }
  }

  saveFeedback(fb);

  // Log for Vercel function logs
  console.log('Task feedback:', { taskId, action, product: product || title, slug });

  return res.status(200).json({ message: 'Feedback recorded' });
};
