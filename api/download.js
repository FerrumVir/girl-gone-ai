const path = require('path');
const fs = require('fs');

let stripe = null;
const STRIPE_SECRET_KEY = process.env.STRIPE_SECRET_KEY || '';
if (STRIPE_SECRET_KEY) {
  stripe = require('stripe')(STRIPE_SECRET_KEY);
}

function inlineMd(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');
}

function parseTable(lines) {
  // Parse markdown table lines into proper HTML table
  let html = '<table>';
  let isHeader = true;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // Skip separator rows (|---|---|)
    if (/^\|[\s\-:|]*-[\s\-:|]*\|?\s*$/.test(line)) continue;
    // Split by | keeping empty cells intact
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

function renderMarkdown(md, productName) {
  // Simple markdown-to-HTML for product delivery
  // 1. Extract tables first, render them separately to avoid escaping issues
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
        const escaped = tableBuffer.map(l =>
          l.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        );
        const tableHtml = parseTable(escaped);
        const placeholder = '\x00TBL' + tables.length + '\x00';
        tables.push(tableHtml);
        processed.push(placeholder);
        tableBuffer = [];
      }
      processed.push(line);
    }
  }
  if (tableBuffer.length > 0) {
    const escaped = tableBuffer.map(l =>
      l.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    );
    const tableHtml = parseTable(escaped);
    const placeholder = '\x00TBL' + tables.length + '\x00';
    tables.push(tableHtml);
    processed.push(placeholder);
  }

  // 2. Render markdown (tables are now placeholders that won't be affected)
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
    .replace(/\n{2,}/g, '</p><p>')
    .replace(/(<\/h[1-3]>)<\/p><p>/g, '$1')
    .replace(/<\/li><\/p><p><li>/g, '</li><li>');

  // Wrap consecutive <li> in <ul>
  html = html.replace(/(<li>.*?<\/li>(\s*<li>.*?<\/li>)*)/gs, '<ul>$1</ul>');

  // 3. Restore pre-rendered tables
  for (let i = 0; i < tables.length; i++) {
    html = html.replace('\x00TBL' + i + '\x00', tables[i]);
  }

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>${productName} — Girl Gone AI</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;600;700&family=Be+Vietnam+Pro:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Be Vietnam Pro', sans-serif;
  background: #fdf8f8;
  color: #1a1a1a;
  min-height: 100vh;
  line-height: 1.7;
}
@media print {
  body { background: #fff; color: #111; }
  .brand-bar, .no-print { display: none !important; }
  .container { max-width: 100%; padding: 20px; }
  h1, h2, h3 { color: #111; }
  p, li, td, th { color: #222; }
  strong { color: #000; }
  table { border-collapse: collapse; page-break-inside: avoid; width: 100%; }
  th { background: #f0f0f0 !important; color: #111 !important; border: 2px solid #000; padding: 6px 10px; font-weight: 700; text-align: left; }
  td { border: 2px solid #000; padding: 6px 10px; }
  blockquote { border-left-color: #a3346a; color: #333; }
  code { background: #f0f0f0; color: #333; }
  ul, ol { page-break-inside: avoid; }
  h2, h3 { page-break-after: avoid; }
}
.brand-bar {
  background: #fdf8f8;
  padding: 16px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 4px solid #000;
}
.brand-bar .logo {
  font-family: 'Newsreader', serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: #a3346a;
  text-decoration: none;
}
.brand-bar .badge {
  font-family: 'Be Vietnam Pro', sans-serif;
  font-size: 0.7rem;
  background: #fff;
  color: #a3346a;
  padding: 4px 12px;
  border: 2px solid #000;
  font-weight: 700;
  text-transform: uppercase;
  box-shadow: 2px 2px 0 #000;
}
.container { max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }
h1 { font-family: 'Newsreader', serif; font-size: 2rem; margin: 24px 0 8px; color: #a3346a; border-bottom: 4px solid #000; padding-bottom: 8px; }
h2 { font-family: 'Newsreader', serif; font-size: 1.4rem; margin: 32px 0 12px; color: #a3346a; border-bottom: 2px solid #000; padding-bottom: 4px; }
h3 { font-family: 'Newsreader', serif; font-size: 1.1rem; margin: 24px 0 8px; color: #1a1a1a; font-weight: 600; }
p { margin: 12px 0; color: #333; }
blockquote { border-left: 4px solid #a3346a; padding: 12px 20px; margin: 16px 0; background: #fff; color: #555; font-style: italic; border: 2px solid #000; border-left: 4px solid #a3346a; }
hr { border: none; border-top: 4px solid #000; margin: 24px 0; }
ul, ol { padding-left: 24px; margin: 12px 0; }
li { margin: 6px 0; color: #333; }
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.85rem; border: 2px solid #000; }
th { padding: 10px 12px; border: 2px solid #000; background: #a3346a; font-weight: 600; color: #fff; text-align: left; }
td { padding: 8px 12px; border: 2px solid #000; color: #333; }
tr:nth-child(even) td { background: #fdf0f4; }
code { background: #fdf0f4; padding: 2px 6px; font-size: 0.85em; color: #a3346a; border: 1px solid #000; }
strong { color: #000; }
.action-bar { text-align: center; margin: 24px 0; }
.action-btn { display: inline-block; padding: 12px 28px; font-weight: 700; text-decoration: none; cursor: pointer; border: 2px solid #000; font-size: 0.95rem; margin: 0 8px; font-family: 'Be Vietnam Pro', sans-serif; }
.action-btn.primary { background: #a3346a; color: #fff; box-shadow: 4px 4px 0 #000; }
.action-btn.primary:hover { transform: translate(2px,2px); box-shadow: 2px 2px 0 #000; }
.action-btn.secondary { background: #fff; color: #1a1a1a; box-shadow: 4px 4px 0 #000; }
.action-btn.secondary:hover { transform: translate(2px,2px); box-shadow: 2px 2px 0 #000; }
</style>
</head>
<body>
<div class="brand-bar">
  <a href="https://girlgone.ai" class="logo">Girl Gone AI</a>
  <div class="badge">Your Product</div>
</div>
<div class="container">
  <div class="action-bar no-print">
    <button class="action-btn primary" onclick="window.print()">Print / Save as PDF</button>
    <a href="https://girlgone.ai" class="action-btn secondary">Browse More Products</a>
  </div>
  ${html}
</div>
</body>
</html>`;
}

function renderBundleDelivery(bundle, bundleName, productsDir, sessionId) {
  // Find included products from the bundle HTML page
  const bundlesDir = path.join(__dirname, '..', 'bundles');
  const bundleSlug = bundle ? bundle.slug : '';
  const bundleFileName = bundleSlug.replace(/^\d+-/, '') || bundleName;
  const bundlePath = path.join(bundlesDir, bundleFileName + '.html');

  let includedProducts = [];
  if (fs.existsSync(bundlePath)) {
    const html = fs.readFileSync(bundlePath, 'utf8');
    const matches = html.matchAll(/<a href="[^"]*\/products\/(\d+-[^"]+)\.html">([^<]+)<\/a>/g);
    for (const m of matches) {
      includedProducts.push({ slug: m[1], name: m[2] });
    }
  }

  // If we couldn't parse, fall back to catalog lookup
  if (includedProducts.length === 0) {
    const catalog = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'products', 'catalog.json'), 'utf8'));
    includedProducts = catalog
      .filter(p => !p.slug.includes('bundle') && p.slug !== 'complete-collection' && p.slug !== 'freelancer-starter-kit' && p.slug !== 'small-business-essential-pack')
      .slice(0, 20)
      .map(p => ({ slug: p.slug, name: p.title }));
  }

  const productLinks = includedProducts.map(p => {
    const name = p.slug.replace(/^\d+-/, '');
    const hasMd = fs.existsSync(path.join(productsDir, name + '.md'));
    const hasHtml = fs.existsSync(path.join(productsDir, name + '.html'));
    if (hasMd || hasHtml) {
      return `<li><a href="/api/download?session_id=${encodeURIComponent(sessionId)}&product=${encodeURIComponent(name)}">${p.name}</a></li>`;
    }
    return `<li>${p.name}</li>`;
  }).join('\n');

  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>${bundleName} — Girl Gone AI</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;600;700&family=Be+Vietnam+Pro:wght@400;600;700&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0;padding:0}body{font-family:'Be Vietnam Pro',sans-serif;background:#fdf8f8;color:#1a1a1a;line-height:1.7;min-height:100vh}
.bar{background:#fdf8f8;padding:16px 32px;display:flex;align-items:center;justify-content:space-between;border-bottom:4px solid #000}
.bar a{font-family:'Newsreader',serif;font-size:1.2rem;font-weight:700;color:#a3346a;text-decoration:none}
.badge{font-size:0.7rem;background:#fff;color:#a3346a;padding:4px 12px;border:2px solid #000;font-weight:700;text-transform:uppercase;box-shadow:2px 2px 0 #000}
.c{max-width:900px;margin:0 auto;padding:40px 24px}h1{font-family:'Newsreader',serif;font-size:2rem;margin-bottom:8px;color:#a3346a;border-bottom:4px solid #000;padding-bottom:8px}
p{color:#555;margin:8px 0 24px}ul{list-style:none;padding:0}li{padding:12px 16px;border-bottom:2px solid #000}
li a{color:#1a1a1a;text-decoration:none;font-weight:600}li a:hover{color:#a3346a}
.browse-btn{display:inline-block;margin:24px 0;padding:12px 28px;background:#a3346a;color:#fff;border:2px solid #000;font-weight:700;cursor:pointer;text-decoration:none;box-shadow:4px 4px 0 #000;font-family:'Be Vietnam Pro',sans-serif}
.browse-btn:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 #000}
</style></head><body>
<div class="bar"><a href="https://girlgone.ai">Girl Gone AI</a><span class="badge">Your Bundle</span></div>
<div class="c"><h1>${bundleName}</h1><p>Click any product below to view and download it.</p>
<ul>${productLinks}</ul>
<a href="https://girlgone.ai" class="browse-btn">Browse More Products</a></div></body></html>`;
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

  let session;
  try {
    session = await stripe.checkout.sessions.retrieve(sessionId);
  } catch (err) {
    console.error('Session retrieval error:', err.message);
    return res.status(400).json({ error: 'Invalid or expired session' });
  }

  if (session.payment_status !== 'paid') {
    return res.status(403).json({ error: 'Payment has not been completed' });
  }

  const productSlug = session.metadata?.product_slug;
  if (!productSlug) {
    return res.status(400).json({ error: 'No product associated with this session' });
  }

  // Handle bundle item delivery (?product=name for individual items within a bundle)
  const bundleItemParam = req.query.product;
  if (bundleItemParam) {
    const itemName = path.basename(String(bundleItemParam).replace(/[^a-z0-9-]/gi, ''));
    if (!itemName) return res.status(400).json({ error: 'Invalid product name' });
    const productsDir = path.join(__dirname, '..', '_products');
    const itemMdPath = path.join(productsDir, itemName + '.md');
    if (fs.existsSync(itemMdPath)) {
      const md = fs.readFileSync(itemMdPath, 'utf8');
      const rendered = renderMarkdown(md, itemName);
      res.setHeader('Content-Type', 'text/html');
      return res.status(200).send(rendered);
    }
    const itemHtmlPath = path.join(productsDir, itemName + '.html');
    if (fs.existsSync(itemHtmlPath)) {
      const html = fs.readFileSync(itemHtmlPath, 'utf8');
      res.setHeader('Content-Type', 'text/html');
      return res.status(200).send(html);
    }
    return res.status(404).json({ error: 'Product not found in bundle' });
  }

  const productName = session.metadata?.product_name || productSlug;
  // Strip number prefix and sanitize: "22-wedding-planning-dashboard" -> "wedding-planning-dashboard"
  const fileName = path.basename(productSlug.replace(/^\d+-/, '').replace(/[^a-z0-9-]/gi, ''));
  if (!fileName) {
    return res.status(400).json({ error: 'Invalid product slug' });
  }

  const productsDir = path.join(__dirname, '..', '_products');

  // Bundle delivery: render a page listing all included products
  if (fileName.includes('bundle') || fileName === 'complete-collection' || fileName === 'freelancer-starter-kit' || fileName === 'small-business-essential-pack') {
    try {
      const catalog = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'products', 'catalog.json'), 'utf8'));
      const bundle = catalog.find(p => p.slug === productSlug || p.slug.replace(/^\d+-/, '') === fileName);
      const bundleHtml = renderBundleDelivery(bundle, productName, productsDir, session.id);
      res.setHeader('Content-Type', 'text/html');
      return res.status(200).send(bundleHtml);
    } catch (err) {
      console.error('Bundle delivery error:', err.message);
    }
  }

  // Prefer .md template (actual product content) over .html (overview)
  const mdPath = path.join(productsDir, fileName + '.md');
  const htmlPath = path.join(productsDir, fileName + '.html');

  // Try markdown template first
  if (fs.existsSync(mdPath)) {
    try {
      const md = fs.readFileSync(mdPath, 'utf8');
      const rendered = renderMarkdown(md, productName);
      res.setHeader('Content-Type', 'text/html');
      res.setHeader('Content-Disposition', 'inline; filename="' + fileName + '.html"');
      return res.status(200).send(rendered);
    } catch (err) {
      console.error('Markdown render error:', err.message);
    }
  }

  // Fallback to HTML file
  try {
    const html = fs.readFileSync(htmlPath, 'utf8');
    res.setHeader('Content-Type', 'text/html');
    res.setHeader('Content-Disposition', 'inline; filename="' + fileName + '.html"');
    return res.status(200).send(html);
  } catch (err) {
    console.error('Download file not found:', fileName, err.message);
    return res.status(404).json({ error: 'Download file not found' });
  }
};
