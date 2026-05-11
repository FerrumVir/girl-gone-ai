const path = require('path');
const fs = require('fs');

function inlineMd(text) {
  return text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/\*(.+?)\*/g, '<em>$1</em>').replace(/`([^`]+)`/g, '<code>$1</code>');
}

function parseTable(lines) {
  let html = '<table>';
  let isHeader = true;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^\|[\s\-:|]*-[\s\-:|]*\|?\s*$/.test(line)) continue;
    const raw = line.replace(/^\|/, '').replace(/\|$/, '');
    const cells = raw.split('|').map(c => inlineMd(c.trim()));
    if (isHeader) {
      html += '<thead><tr>' + cells.map(c => '<th>' + c + '</th>').join('') + '</tr></thead><tbody>';
      isHeader = false;
    } else {
      html += '<tr>' + cells.map(c => '<td>' + c + '</td>').join('') + '</tr>';
    }
  }
  html += '</tbody></table>';
  return html;
}

function renderFreeMarkdown(md, name) {
  const lines = md.split('\n');
  const tables = [];
  const processed = [];
  let tableBuffer = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^\|/.test(line)) {
      tableBuffer.push(line);
    } else {
      if (tableBuffer.length > 0) {
        const escaped = tableBuffer.map(l => l.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'));
        const placeholder = '\x00TBL' + tables.length + '\x00';
        tables.push(parseTable(escaped));
        processed.push(placeholder);
        tableBuffer = [];
      }
      processed.push(line);
    }
  }
  if (tableBuffer.length > 0) {
    const escaped = tableBuffer.map(l => l.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'));
    const placeholder = '\x00TBL' + tables.length + '\x00';
    tables.push(parseTable(escaped));
    processed.push(placeholder);
  }

  let html = processed.join('\n')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/^---$/gm, '<hr>')
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/^\d+\. (.+)$/gm, '<li>$1</li>')
    .replace(/\n{2,}/g, '</p><p>');
  html = html.replace(/(<li>.*?<\/li>(\s*<li>.*?<\/li>)*)/gs, '<ul>$1</ul>');
  for (let i = 0; i < tables.length; i++) {
    html = html.replace('\x00TBL' + i + '\x00', tables[i]);
  }
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>${name} — Girl Gone AI</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;600;700&family=Be+Vietnam+Pro:wght@400;600;700&display=swap" rel="stylesheet"><style>*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}body{font-family:'Be Vietnam Pro',sans-serif;background:#fdf8f8;color:#1a1a1a;line-height:1.7;margin:0}@media print{body{background:#fff;color:#111}.bar,.no-print{display:none!important}.c{max-width:100%;padding:20px}h1,h2,h3{color:#111}p,li,td,th{color:#222}strong{color:#000}table{border-collapse:collapse;page-break-inside:avoid;width:100%}th{background:#f0f0f0!important;color:#111!important;border:2px solid #000;padding:6px 10px;font-weight:700;text-align:left}td{border:2px solid #000;padding:6px 10px}blockquote{border-left-color:#a3346a;color:#333}code{background:#f0f0f0;color:#333}ul,ol{page-break-inside:avoid}h2,h3{page-break-after:avoid}}.c{max-width:900px;margin:0 auto;padding:40px 24px}h1{font-family:'Newsreader',serif;font-size:2rem;color:#a3346a;border-bottom:4px solid #000;padding-bottom:8px;margin-bottom:16px}h2{font-family:'Newsreader',serif;font-size:1.4rem;color:#a3346a;margin:32px 0 12px;border-bottom:2px solid #000;padding-bottom:4px}h3{font-family:'Newsreader',serif;color:#1a1a1a;margin:24px 0 8px;font-weight:600}p{margin:12px 0;color:#333}blockquote{border-left:4px solid #a3346a;padding:12px 20px;margin:16px 0;background:#fff;color:#555;font-style:italic;border:2px solid #000;border-left:4px solid #a3346a}hr{border:none;border-top:4px solid #000;margin:24px 0}ul{padding-left:24px}li{margin:6px 0;color:#333}table{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.85rem;border:2px solid #000}th{padding:10px 12px;border:2px solid #000;background:#a3346a;font-weight:600;color:#fff;text-align:left}td{padding:8px 12px;border:2px solid #000;color:#333}tr:nth-child(even) td{background:#fdf0f4}code{background:#fdf0f4;padding:2px 6px;font-size:0.85em;color:#a3346a;border:1px solid #000}strong{color:#000}.bar{background:#fdf8f8;padding:16px 32px;display:flex;align-items:center;justify-content:space-between;border-bottom:4px solid #000}.bar a{font-family:'Newsreader',serif;font-size:1.2rem;font-weight:700;color:#a3346a;text-decoration:none}.badge{font-size:0.7rem;background:#fff;color:#a3346a;padding:4px 12px;border:2px solid #000;font-weight:700;text-transform:uppercase;box-shadow:2px 2px 0 #000}.act{text-align:center;margin:24px 0}.act button{display:inline-block;padding:12px 28px;font-weight:700;cursor:pointer;border:2px solid #000;font-size:0.95rem;background:#a3346a;color:#fff;box-shadow:4px 4px 0 #000;font-family:'Be Vietnam Pro',sans-serif}.act button:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 #000}.act a{display:inline-block;padding:12px 28px;font-weight:700;text-decoration:none;font-size:0.95rem;background:#fff;color:#1a1a1a;margin-left:8px;border:2px solid #000;box-shadow:4px 4px 0 #000;font-family:'Be Vietnam Pro',sans-serif}.act a:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 #000}</style></head><body><div class="bar"><a href="https://girlgone.ai">Girl Gone AI</a><span class="badge">Free Product</span></div><div class="c"><div class="act no-print"><button onclick="window.print()">Print / Save as PDF</button><a href="https://girlgone.ai">Browse More Products</a></div>${html}</div></body></html>`;
}

const FREE_FILES = new Set([
  'ai-productivity-starter-kit',
  'morning-glow-checklist',
  'freelance-invoicing-notion',
  'content-calendar-notion',
  'wellness-tracker',
  'teacher-lesson-planner',
  'adhd-planner',
  'content-creator-prompts',
  'budget-tracker-sheets',
  'habit-streak-tracker-sheets',
  'meal-prep-planner',
]);

module.exports = async function handler(req, res) {
  const rawFile = req.query.file || '';
  const fileName = path.basename(rawFile, '.html').replace(/[^a-z0-9-]/gi, '');

  if (fileName && FREE_FILES.has(fileName)) {
    const productsDir = path.join(__dirname, '..', '_products');
    const mdPath = path.join(productsDir, fileName + '.md');
    const htmlPath = path.join(productsDir, fileName + '.html');

    // Prefer .md template (actual product content)
    if (fs.existsSync(mdPath)) {
      try {
        const md = fs.readFileSync(mdPath, 'utf8');
        res.setHeader('Content-Type', 'text/html');
        return res.status(200).send(renderFreeMarkdown(md, fileName));
      } catch (err) { /* fall through */ }
    }
    try {
      const html = fs.readFileSync(htmlPath, 'utf8');
      res.setHeader('Content-Type', 'text/html');
      return res.status(200).send(html);
    } catch (err) {
      // fall through
    }
  }

  res.setHeader('Content-Type', 'text/html');
  return res.status(403).send(`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Access Denied — Girl Gone AI</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;600;700&family=Be+Vietnam+Pro:wght@400;600;700&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0;padding:0}body{font-family:'Be Vietnam Pro',sans-serif;background:#fdf8f8;color:#1a1a1a;min-height:100vh;display:flex;flex-direction:column}
.bar{background:#fdf8f8;padding:16px 32px;display:flex;align-items:center;justify-content:space-between;border-bottom:4px solid #000}
.bar a{font-family:'Newsreader',serif;font-size:1.2rem;font-weight:700;color:#a3346a;text-decoration:none}
.c{max-width:600px;margin:80px auto;padding:40px;border:4px solid #000;box-shadow:8px 8px 0 #000;text-align:center;background:#fff}
h1{font-family:'Newsreader',serif;font-size:2rem;color:#a3346a;margin-bottom:16px}
p{color:#555;margin-bottom:24px}
.btn{display:inline-block;padding:12px 28px;background:#a3346a;color:#fff;border:2px solid #000;font-weight:700;text-decoration:none;box-shadow:4px 4px 0 #000;font-family:'Be Vietnam Pro',sans-serif}
.btn:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 #000}
</style></head><body>
<div class="bar"><a href="https://girlgone.ai">Girl Gone AI</a></div>
<div class="c"><h1>Access Denied</h1><p>This is a paid download. Please purchase the product to access it.</p>
<a href="/" class="btn">&larr; Browse the catalog</a></div>
</body></html>`);
};
