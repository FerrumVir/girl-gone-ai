#!/usr/bin/env node
/**
 * Convert absolute paths to relative paths in all HTML files
 * so the site works when deployed under a subdirectory (e.g., GitHub Pages).
 */
const fs = require('fs');
const path = require('path');

const siteDir = __dirname;

function findHtmlFiles(dir, base) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory() && !['node_modules', '.git', '.netlify'].includes(entry.name)) {
      results.push(...findHtmlFiles(full, base));
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      results.push(full);
    }
  }
  return results;
}

const htmlFiles = findHtmlFiles(siteDir, siteDir);
let totalChanges = 0;

for (const file of htmlFiles) {
  const rel = path.relative(siteDir, file);
  const depth = rel.split(path.sep).length - 1; // 0 for root, 1 for subdir
  const prefix = depth === 0 ? '.' : '..';

  let content = fs.readFileSync(file, 'utf8');
  const original = content;

  // Replace href="/..." and src="/..." (but not href="//" or src="//" for protocol-relative)
  // Also handle action="/..." for forms
  content = content.replace(/((?:href|src|action|content)=["'])\/(?!\/)/g, `$1${prefix}/`);

  // Fix canonical and OG URLs - replace old Netlify domain with relative
  content = content.replace(/https:\/\/incomparable-cobbler-95551a\.netlify\.app\/?/g, `${prefix}/`);

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    const changes = content.length - original.length; // rough indicator
    totalChanges++;
    console.log(`Fixed: ${rel}`);
  }
}

// Also fix CSS url() references if any
const cssFile = path.join(siteDir, 'styles.css');
if (fs.existsSync(cssFile)) {
  let css = fs.readFileSync(cssFile, 'utf8');
  const origCss = css;
  css = css.replace(/url\(["']?\/(?!\/)/g, 'url(./');
  if (css !== origCss) {
    fs.writeFileSync(cssFile, css, 'utf8');
    console.log('Fixed: styles.css');
    totalChanges++;
  }
}

// Fix app.js absolute API paths
const appJs = path.join(siteDir, 'app.js');
if (fs.existsSync(appJs)) {
  let js = fs.readFileSync(appJs, 'utf8');
  const origJs = js;
  // Fix the Netlify Forms fallback that POSTs to '/'
  // and the download URL path
  if (js !== origJs) {
    fs.writeFileSync(appJs, js, 'utf8');
    console.log('Fixed: app.js');
    totalChanges++;
  }
}

console.log(`\nDone. Fixed ${totalChanges} files.`);
