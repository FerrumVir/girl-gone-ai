#!/usr/bin/env python3
"""Generate ebook content pages and secure download pages for all products."""
import os, re, hashlib, secrets, html as html_mod, json

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_DIR = os.path.join(SITE_DIR, "products")
FILES_DIR = os.path.join(SITE_DIR, "downloads", "files")
SECURE_DIR = os.path.join(SITE_DIR, "downloads", "secure")
os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(SECURE_DIR, exist_ok=True)

# Template for ebook content page (viewable, printable as PDF)
EBOOK_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{title} — Girl Gone AI</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Poppins', -apple-system, sans-serif;
  background: #0a0a1a;
  color: #e0e0f0;
  min-height: 100vh;
}}
@media print {{
  body {{ background: #fff; color: #111; }}
  .brand-bar, .action-bar, .no-print {{ display: none !important; }}
  .container {{ max-width: 100%; padding: 0; }}
  .section-card {{ border: 1px solid #ddd; break-inside: avoid; background: #fff; }}
  .section-card h2 {{ color: #333; }}
  .section-card li {{ color: #444; border-color: #eee; }}
  .section-card li::before {{ color: #333; }}
  h1 {{ color: #111; -webkit-text-fill-color: #111; background: none; }}
  .tagline {{ color: #666; }}
}}
.brand-bar {{
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  padding: 16px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}}
.brand-bar .logo {{
  font-size: 1.2rem;
  font-weight: 700;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-decoration: none;
}}
.brand-bar .badge {{
  font-size: 0.7rem;
  background: rgba(16,185,129,0.15);
  color: #10B981;
  padding: 4px 12px;
  border-radius: 20px;
  border: 1px solid rgba(16,185,129,0.3);
  font-weight: 600;
  letter-spacing: 1px;
}}
.container {{
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 24px 80px;
}}
h1 {{
  font-size: 2rem;
  font-weight: 800;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
}}
.tagline {{
  color: #888;
  font-size: 1rem;
  margin-bottom: 8px;
}}
.price-badge {{
  display: inline-block;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  color: #fff;
  padding: 4px 16px;
  border-radius: 20px;
  font-weight: 700;
  font-size: 0.85rem;
  margin-bottom: 32px;
}}
.action-bar {{
  display: flex;
  gap: 12px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}}
.action-btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 20px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  border: none;
  transition: transform 0.2s;
}}
.action-btn:hover {{ transform: translateY(-1px); }}
.action-btn.primary {{
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  color: #fff;
}}
.action-btn.secondary {{
  background: rgba(255,255,255,0.08);
  color: #ccc;
  border: 1px solid rgba(255,255,255,0.12);
}}
.section-card {{
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 28px;
  margin-bottom: 20px;
}}
.section-card h2 {{
  font-size: 1.1rem;
  font-weight: 700;
  color: #FF3B8B;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.section-card ul {{
  list-style: none;
  padding: 0;
}}
.section-card li {{
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  font-size: 0.9rem;
  color: #ccc;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  line-height: 1.5;
}}
.section-card li:last-child {{ border-bottom: none; }}
.section-card li::before {{
  content: "\\2713";
  color: #10B981;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 1px;
}}
.footer {{
  text-align: center;
  padding: 24px;
  color: #555;
  font-size: 0.8rem;
  border-top: 1px solid rgba(255,255,255,0.04);
  margin-top: 40px;
}}
.footer a {{ color: #A855F7; text-decoration: none; }}
</style>
</head>
<body>
<div class="brand-bar">
  <a href="https://girlgone.ai" class="logo">Girl Gone AI</a>
  <div class="badge">YOUR PRODUCT</div>
</div>
<div class="container">
  <h1>{title}</h1>
  <p class="tagline">{tagline}</p>
  <div class="price-badge">{price}</div>
  <div class="action-bar no-print">
    <button class="action-btn primary" onclick="window.print()">Print / Save as PDF</button>
    <a href="https://girlgone.ai" class="action-btn secondary">Browse More Products</a>
  </div>
{sections}
</div>
<div class="footer">
  <p>&copy; 2026 <a href="https://girlgone.ai">Girl Gone AI</a> by Jaci Ellis. All rights reserved.</p>
  <p style="margin-top:8px;color:#444">Need help? Email <a href="mailto:support@girlgone.ai">support@girlgone.ai</a></p>
</div>
</body>
</html>"""

# Template for secure download page
SECURE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="noindex, nofollow" />
<title>{title} — Download | Girl Gone AI</title>
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Poppins', -apple-system, sans-serif;
  background: #0a0a1a;
  color: #e0e0f0;
  min-height: 100vh;
}}
.brand-bar {{
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  padding: 16px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}}
.brand-bar .logo {{
  font-size: 1.2rem;
  font-weight: 700;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.brand-bar .badge {{
  font-size: 0.7rem;
  background: rgba(168,85,247,0.15);
  color: #A855F7;
  padding: 4px 12px;
  border-radius: 20px;
  border: 1px solid rgba(168,85,247,0.3);
  font-weight: 600;
  letter-spacing: 1px;
}}
.access-wall {{
  max-width: 480px;
  margin: 120px auto;
  text-align: center;
  padding: 40px;
}}
.access-wall h1 {{
  font-size: 1.4rem;
  margin-bottom: 12px;
  color: #FF3B8B;
}}
.access-wall p {{
  color: #888;
  font-size: 0.9rem;
  margin-bottom: 24px;
}}
.access-wall a {{
  color: #A855F7;
  text-decoration: none;
}}
.download-container {{
  max-width: 800px;
  margin: 40px auto;
  padding: 0 24px 80px;
  display: none;
}}
.download-header {{
  text-align: center;
  padding: 40px 0 32px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  margin-bottom: 32px;
}}
.download-header .check {{
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #10B981, #34D399);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  font-size: 28px;
}}
.download-header h1 {{
  font-size: 1.6rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 8px;
}}
.download-header .subtitle {{
  color: #888;
  font-size: 0.9rem;
}}
.content-card {{
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 32px;
  margin-bottom: 24px;
}}
.content-card h2 {{
  font-size: 1.1rem;
  font-weight: 700;
  color: #FF3B8B;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.content-card ul {{
  list-style: none;
  padding: 0;
}}
.content-card li {{
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  font-size: 0.9rem;
  color: #ccc;
  display: flex;
  align-items: flex-start;
  gap: 10px;
}}
.content-card li:last-child {{ border-bottom: none; }}
.content-card li::before {{
  content: "\\2713";
  color: #10B981;
  font-weight: 700;
  flex-shrink: 0;
}}
.content-card p {{
  font-size: 0.9rem;
  color: #bbb;
  line-height: 1.7;
}}
.download-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  color: #fff;
  padding: 14px 32px;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 700;
  font-size: 1rem;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(255,59,139,0.3);
}}
.download-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(255,59,139,0.4);
}}
.support-note {{
  text-align: center;
  margin-top: 40px;
  padding: 24px;
  background: rgba(168,85,247,0.08);
  border-radius: 12px;
  border: 1px solid rgba(168,85,247,0.15);
}}
.support-note p {{
  font-size: 0.85rem;
  color: #999;
}}
.support-note a {{
  color: #A855F7;
  text-decoration: none;
}}
</style>
</head>
<body>
<div class="brand-bar">
  <div class="logo">Girl Gone AI</div>
  <div class="badge">PURCHASED</div>
</div>

<div class="access-wall" id="accessWall">
  <h1>Access Required</h1>
  <p>This download page requires a valid purchase token. If you purchased this product, please use the link from your Gumroad receipt.</p>
  <p><a href="https://girlgone.ai">Back to Girl Gone AI</a></p>
</div>

<div class="download-container" id="downloadContent">
  <div class="download-header">
    <div class="check">&#10003;</div>
    <h1>{title}</h1>
    <p class="subtitle">Thank you for your purchase! Your product is ready below.</p>
  </div>

  <div class="content-card">
    <h2>What's Inside</h2>
    <ul>
{whats_inside}
    </ul>
  </div>

  <div style="text-align:center;margin-bottom:24px"><a href="https://girlgone.ai/products/{product_file}" class="download-btn" style="background:rgba(255,255,255,0.08);box-shadow:none;font-size:0.85rem;padding:10px 24px">View Full Product Details</a></div>
  <div class="content-card">
    <h2>How to Use</h2>
    <ol style="color:#ccc;font-size:0.9rem;padding-left:20px;line-height:2">
{how_to_use}
    </ol>
  </div>

  <div style="text-align:center;padding:32px 0">
    <p style="color:#888;font-size:0.85rem;margin-bottom:16px">Your product is ready for download:</p>
    <a href="https://girlgone.ai/downloads/files/{ebook_file}" class="download-btn">Access Your Product</a>
  </div>

  <div class="support-note">
    <p>Need help? Email <a href="mailto:support@girlgone.ai">support@girlgone.ai</a></p>
    <p style="margin-top:8px"><a href="https://girlgone.ai">Browse more products</a></p>
  </div>
</div>

<script>
(function() {{
  var h = "{token_hash}";
  var p = new URLSearchParams(window.location.search);
  var t = p.get("token");
  if (!t) return;
  crypto.subtle.digest("SHA-256", new TextEncoder().encode(t)).then(function(buf) {{
    var hex = Array.from(new Uint8Array(buf)).map(function(b) {{ return b.toString(16).padStart(2,"0"); }}).join("");
    if (hex === h) {{
      document.getElementById("accessWall").style.display = "none";
      document.getElementById("downloadContent").style.display = "block";
    }}
  }});
}})();
</script>
</body>
</html>"""

# Product category to format type mapping for "How to Use" instructions
FORMAT_INSTRUCTIONS = {
    "notion": [
        "<li>Click the download button to access your Notion template</li>",
        "<li>Click \"Duplicate\" in the top-right to add it to your workspace</li>",
        "<li>Customize the properties and views to match your workflow</li>",
        "<li>Check the instructions page inside the template for setup tips</li>",
    ],
    "sheets": [
        "<li>Click the download button to access your spreadsheet</li>",
        "<li>Open in Google Sheets or Excel</li>",
        "<li>Make a copy (File > Make a Copy) to start editing</li>",
        "<li>Follow the instructions tab for setup tips</li>",
    ],
    "prompts": [
        "<li>Click the download button to access your prompt pack</li>",
        "<li>Browse prompts by category to find what you need</li>",
        "<li>Copy and paste prompts directly into your AI tool</li>",
        "<li>Customize the bracketed variables for your specific use case</li>",
    ],
    "default": [
        "<li>Click the download button to access your product</li>",
        "<li>Review the contents and find the section that fits your needs</li>",
        "<li>Follow the included instructions to get started</li>",
        "<li>Customize templates and resources to match your workflow</li>",
    ],
}


def detect_format(slug, title):
    slug_lower = slug.lower()
    title_lower = title.lower()
    if "notion" in slug_lower or "notion" in title_lower:
        return "notion"
    if "sheets" in slug_lower or "spreadsheet" in slug_lower or "calculator" in slug_lower or "dashboard" in slug_lower:
        return "sheets"
    if "prompt" in slug_lower or "prompt" in title_lower:
        return "prompts"
    return "default"


def extract_product_data(filepath):
    """Extract product data from an HTML product page."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract title
    m = re.search(r"<h1>(.*?)</h1>", content)
    title = html_mod.unescape(m.group(1)) if m else "Product"

    # Extract price
    m = re.search(r'class="product-price-lg">(.*?)</span>', content)
    price = html_mod.unescape(m.group(1).strip()) if m else "$0"

    # Extract category
    m = re.search(r'class="product-category">(.*?)</span>', content)
    category = html_mod.unescape(m.group(1)) if m else ""

    # Extract listing content
    m = re.search(r'class="listing-content">(.*?)</div>\s*<div class="product-buy-bar bottom-bar">', content, re.DOTALL)
    listing_html = m.group(1) if m else ""

    # Extract description
    m = re.search(r'class="product-description">(.*?)</p>', content, re.DOTALL)
    desc = html_mod.unescape(m.group(1).strip()) if m else ""

    return {
        "title": title,
        "price": price,
        "category": category,
        "listing_html": listing_html,
        "description": desc,
    }


def parse_listing_to_sections(listing_html, title):
    """Parse listing HTML into structured sections for the ebook."""
    sections = []

    # Try to extract sections from strong/bold headers + list items
    # Pattern: <strong>Header</strong> followed by bullets or paragraphs
    # Also look for <h2> tags
    parts = re.split(r"<(?:h2|h3)[^>]*>|<(?:strong|b)>", listing_html)

    current_section = None
    items = []

    for part in parts:
        # Check if this starts with a header
        header_match = re.match(r"(.*?)</(?:h2|h3|strong|b)>", part)
        if header_match:
            # Save previous section
            if current_section and items:
                sections.append({"title": current_section, "items": items})
                items = []
            header_text = html_mod.unescape(re.sub(r"<[^>]+>", "", header_match.group(1))).strip()
            if header_text and len(header_text) < 80:
                current_section = header_text

        # Extract list items
        li_matches = re.findall(r"<li[^>]*>(.*?)</li>", part, re.DOTALL)
        for li in li_matches:
            text = html_mod.unescape(re.sub(r"<[^>]+>", "", li)).strip()
            if text:
                items.append(text)

    # Save last section
    if current_section and items:
        sections.append({"title": current_section, "items": items})

    # If no sections found, create a generic one from all list items
    if not sections:
        all_items = re.findall(r"<li[^>]*>(.*?)</li>", listing_html, re.DOTALL)
        items = [html_mod.unescape(re.sub(r"<[^>]+>", "", li)).strip() for li in all_items if li.strip()]
        if items:
            sections.append({"title": "What's Included", "items": items})

    # If still nothing, extract from paragraphs
    if not sections:
        paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", listing_html, re.DOTALL)
        items = []
        for p in paragraphs:
            text = html_mod.unescape(re.sub(r"<[^>]+>", "", p)).strip()
            if text and len(text) > 10 and len(text) < 200:
                items.append(text)
        if items:
            sections.append({"title": "What's Included", "items": items[:12]})

    # Fallback: generate from title
    if not sections:
        sections.append({
            "title": "What's Included",
            "items": [
                f"Complete {title} package",
                "Step-by-step setup instructions",
                "Ready-to-use templates and resources",
                "Customizable for your specific needs",
            ],
        })

    return sections


def generate_ebook_slug(product_file):
    """Convert product filename to ebook slug.
    e.g. '24-midjourney-prompts.html' -> 'midjourney-prompts'
    """
    slug = product_file.replace(".html", "")
    # Remove leading number prefix
    slug = re.sub(r"^\d+-", "", slug)
    return slug


def main():
    # Track tokens for each product (for potential use later)
    tokens = {}
    created_files = 0
    created_secure = 0

    product_files = sorted(os.listdir(PRODUCTS_DIR))

    for pf in product_files:
        if not pf.endswith(".html"):
            continue

        full_slug = pf.replace(".html", "")
        ebook_slug = generate_ebook_slug(pf)
        ebook_file = ebook_slug + ".html"

        # Skip if both ebook and secure page already exist
        ebook_path = os.path.join(FILES_DIR, ebook_file)
        secure_path = os.path.join(SECURE_DIR, ebook_file)

        if os.path.exists(ebook_path) and os.path.exists(secure_path):
            continue

        # Parse product page
        data = extract_product_data(os.path.join(PRODUCTS_DIR, pf))

        # Skip free products (no ebook needed — they have markdown downloads)
        if data["price"].lower() == "free":
            continue

        # Parse content into sections
        sections = parse_listing_to_sections(data["listing_html"], data["title"])

        # Generate tagline from description (first sentence, max 80 chars)
        tagline = data["description"][:80].rsplit(" ", 1)[0] if data["description"] else data["category"]

        # Build ebook sections HTML
        sections_html = ""
        for sec in sections:
            items_html = "\n".join(f"    <li>{item}</li>" for item in sec["items"])
            sections_html += f"""  <div class="section-card">
    <h2>{sec['title']}</h2>
    <ul>
{items_html}
    </ul>
  </div>
"""

        # Generate ebook file
        if not os.path.exists(ebook_path):
            ebook_html = EBOOK_TEMPLATE.format(
                title=data["title"],
                tagline=tagline,
                price=data["price"],
                sections=sections_html,
            )
            with open(ebook_path, "w", encoding="utf-8") as f:
                f.write(ebook_html)
            created_files += 1

        # Generate secure download page
        if not os.path.exists(secure_path):
            # Generate token
            token = secrets.token_hex(16)
            token_hash = hashlib.sha256(token.encode()).hexdigest()
            tokens[ebook_slug] = {"token": token, "hash": token_hash}

            # Build "What's Inside" list from first section
            first_items = sections[0]["items"][:8] if sections else ["Complete product package"]
            whats_inside = "\n".join(f"      <li>{item}</li>" for item in first_items)

            # Build "How to Use" instructions
            fmt = detect_format(full_slug, data["title"])
            how_to_use = "\n".join(FORMAT_INSTRUCTIONS[fmt])

            secure_html = SECURE_TEMPLATE.format(
                title=data["title"],
                whats_inside=whats_inside,
                product_file=pf,
                ebook_file=ebook_file,
                how_to_use=how_to_use,
                token_hash=token_hash,
            )
            with open(secure_path, "w", encoding="utf-8") as f:
                f.write(secure_html)
            created_secure += 1

    # Save tokens to a JSON file for reference
    if tokens:
        tokens_path = os.path.join(SITE_DIR, "downloads", "tokens.json")
        existing = {}
        if os.path.exists(tokens_path):
            with open(tokens_path, "r") as f:
                existing = json.load(f)
        existing.update(tokens)
        with open(tokens_path, "w") as f:
            json.dump(existing, f, indent=2)

    print(f"Created {created_files} ebook files in downloads/files/")
    print(f"Created {created_secure} secure pages in downloads/secure/")
    print(f"Total ebook files: {len(os.listdir(FILES_DIR))}")
    print(f"Total secure pages: {len(os.listdir(SECURE_DIR))}")


if __name__ == "__main__":
    main()
