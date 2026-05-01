#!/usr/bin/env python3
"""
Restructure the Girl Gone AI index.html catalog:
- Move 12 published Gumroad products into an "Available Now" section
- Move all remaining products into a "Launching Soon" section
- Keep bundles between the two sections
- Update hero stats
"""

import re
from html import unescape

INDEX_PATH = '/home/boogarweed/girl-gone-ai/index.html'

# Published product filenames mapped to their Gumroad URLs
PUBLISHED_PRODUCTS = {
    '18-product-launch-checklist.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/apbls',
        'name': 'Product Launch Playbook',
        'price': '$12',
    },
    '19-invoice-generator.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/thtyoc',
        'name': 'Professional Invoice Generator',
        'price': '$8',
    },
    '20-proposal-template.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/baqfdx',
        'name': 'Client Proposal Template Kit',
        'price': '$10',
    },
    '21-teacher-lesson-planner.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/gkdlq',
        'name': 'Teacher Lesson Planner & Classroom Manager',
        'price': '$12',
    },
    '22-wedding-planning-dashboard.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/hxntlz',
        'name': 'Wedding Planning Dashboard',
        'price': '$18',
    },
    '23-side-hustle-tracker.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/xrlbjs',
        'name': 'Side Hustle Income & Expense Tracker',
        'price': '$9',
    },
    '24-midjourney-prompts.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/rjfayx',
        'name': 'Midjourney & AI Art Prompt Pack',
        'price': '$17',
    },
    '25-meal-prep-planner.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/btxunu',
        'name': 'Meal Prep & Recipe Planner',
        'price': '$10',
    },
    '26-student-study-system.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/rypqg',
        'name': 'Student Study System',
        'price': '$8',
    },
    '27-podcast-launch-kit.html': {
        'gumroad': 'https://girlgoneai.gumroad.com/l/27-podcast-launch-kit',
        'name': 'Podcast Launch Kit',
        'price': '$14',
    },
}

# Two free products that don't have product pages on the site
FREE_PRODUCTS = [
    {
        'name': 'AI Productivity Starter Kit',
        'price': 'FREE',
        'gumroad': 'https://girlgoneai.gumroad.com/l/free-starter-kit',
        'product_page': None,
        'desc': 'Your free entry point into the Girl Gone AI ecosystem. Essential AI productivity tools, templates, and quick-start guides to help you work smarter from day one.',
    },
    {
        'name': 'Free Morning Glow Checklist',
        'price': 'FREE',
        'gumroad': 'https://girlgoneai.gumroad.com/l/wgnvf',
        'product_page': None,
        'desc': 'Start every morning with intention. A simple, beautiful checklist to build your perfect morning routine — skincare, mindset, and productivity in one flow.',
    },
]


def extract_product_cards(html_block):
    """Extract individual product-card divs from an HTML block."""
    cards = []
    pattern = r'<div class="product-card">\s*\n(.*?)</div>\s*\n'
    # Use a more robust approach: find each product-card div
    lines = html_block.split('\n')
    in_card = False
    card_lines = []
    depth = 0

    for line in lines:
        if '<div class="product-card">' in line:
            in_card = True
            card_lines = [line]
            depth = 1
            continue

        if in_card:
            card_lines.append(line)
            depth += line.count('<div') - line.count('</div>')
            if depth <= 0:
                cards.append('\n'.join(card_lines))
                in_card = False
                card_lines = []

    return cards


def get_product_filename(card_html):
    """Extract the product filename from a card's View Product link."""
    match = re.search(r'href="products/([^"]+)"', card_html)
    if match:
        return match.group(1)
    return None


def is_published(card_html):
    """Check if a product card is one of the 12 published products."""
    filename = get_product_filename(card_html)
    if filename and filename in PUBLISHED_PRODUCTS:
        return True
    return False


def add_gumroad_link_to_card(card_html, filename):
    """Add a 'Buy on Gumroad' link to a published product card."""
    info = PUBLISHED_PRODUCTS[filename]
    gumroad_url = info['gumroad']
    # Add the Gumroad link next to the existing View Product link
    card_html = card_html.replace(
        '<div class="links">',
        f'<div class="links"><a href="{gumroad_url}" target="_blank" rel="noopener" class="gumroad-link">Buy on Gumroad</a> '
    )
    return card_html


def add_coming_soon_badge(card_html):
    """Replace buy links with a Coming Soon badge on a product card."""
    # Add a coming soon badge after the price span
    card_html = re.sub(
        r'(<span class="price">[^<]*</span>)',
        r'\1\n        <span class="coming-soon-badge">Coming Soon</span>',
        card_html,
        count=1
    )
    # Remove the View Product link div and replace with a "Coming Soon" note
    card_html = re.sub(
        r'<div class="links"><a href="[^"]*">View Product</a></div>',
        '<div class="links"><span class="coming-soon-text">Coming Soon</span></div>',
        card_html
    )
    return card_html


def build_available_now_section(published_cards):
    """Build the Available Now section HTML."""
    lines = []
    lines.append('  <!-- Available Now - Published on Gumroad -->')
    lines.append('  <section class="section available-now" id="available-now">')
    lines.append('    <div class="container">')
    lines.append('    <div class="section-header">')
    lines.append('      <span class="section-tag">Shop Now</span>')
    lines.append('      <h2 class="section-title">Available Now</h2>')
    lines.append('      <p class="section-desc">These products are live and ready to download. Get instant access on Gumroad.</p>')
    lines.append('    </div>')
    lines.append('    <div class="products-grid">')

    # Add the two free products first
    for fp in FREE_PRODUCTS:
        lines.append('      <div class="product-card published-card">')
        lines.append(f'        <h3>{fp["name"]}</h3>')
        lines.append(f'        <span class="price">{fp["price"]}</span>')
        lines.append('        <span class="free-badge">FREE</span>')
        lines.append(f'        <p class="desc">{fp["desc"]}</p>')
        lines.append(f'        <div class="links"><a href="{fp["gumroad"]}" target="_blank" rel="noopener" class="gumroad-link">Get Free on Gumroad</a></div>')
        lines.append('      </div>')
        lines.append('')

    # Add the 10 published product cards (with Gumroad links added)
    for card in published_cards:
        filename = get_product_filename(card)
        modified_card = add_gumroad_link_to_card(card, filename)
        # Add "published-card" class
        modified_card = modified_card.replace('class="product-card"', 'class="product-card published-card"')
        lines.append(modified_card)
        lines.append('')

    lines.append('    </div>')
    lines.append('    </div>')
    lines.append('  </section>')
    lines.append('')

    return '\n'.join(lines)


def build_launching_soon_wrapper_start():
    """Build the opening of the Launching Soon section."""
    lines = []
    lines.append('  <!-- Launching Soon -->')
    lines.append('  <section class="launching-soon-header" id="launching-soon">')
    lines.append('    <div class="container">')
    lines.append('    <div class="section-header">')
    lines.append('      <span class="section-tag">Preview</span>')
    lines.append('      <h2 class="section-title">Launching Soon</h2>')
    lines.append('      <p class="section-desc">These products are in the works and will be available for purchase soon. Browse what\'s coming next.</p>')
    lines.append('    </div>')
    lines.append('    </div>')
    lines.append('  </section>')
    lines.append('')
    return '\n'.join(lines)


def process_category_section(section_html):
    """Process a category section: remove published cards and add Coming Soon badges to remaining."""
    cards = extract_product_cards(section_html)

    remaining_cards = []
    for card in cards:
        if not is_published(card):
            remaining_cards.append(add_coming_soon_badge(card))

    if not remaining_cards:
        return None  # No remaining cards in this category

    # Rebuild the section with only remaining cards
    # Extract the section header (everything before the first product-card)
    header_match = re.search(r'^(.*?<div class="products-grid">)', section_html, re.DOTALL)
    if not header_match:
        return None

    header = header_match.group(1)
    rebuilt = header + '\n'
    for card in remaining_cards:
        rebuilt += card + '\n\n'
    rebuilt += '    </div>\n  </section>'

    return rebuilt


def main():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # --- Step 1: Update hero stats ---
    # Change "140+" to "12" in hero stats
    html = html.replace(
        '<span class="hero-stat-num">140+</span><span class="hero-stat-label">Products</span>',
        '<span class="hero-stat-num">12</span><span class="hero-stat-label">Available Products</span>'
    )

    # Update the about section stat too
    html = html.replace(
        '<span class="stat-num">140+</span>\n              <span class="stat-label">products</span>',
        '<span class="stat-num">12</span>\n              <span class="stat-label">available</span>'
    )

    # Update section title "9 Categories. 140+ Products."
    html = html.replace(
        '9 Categories. 140+ Products.',
        '12 Available Now. 128+ Launching Soon.'
    )

    # Update meta descriptions
    html = html.replace(
        '140+ premium digital products',
        '12 available digital products, 128+ launching soon'
    )
    html = html.replace(
        '140+ digital products',
        '12 available digital products'
    )

    # --- Step 2: Find the catalog section ---
    # The catalog is: <div class="catalog" id="catalog"> ... </div> before <!-- ========== Social ========== -->
    catalog_start_marker = '<div class="catalog" id="catalog">'
    social_marker = '<!-- ========== Social ========== -->'

    catalog_start_idx = html.index(catalog_start_marker)
    social_idx = html.index(social_marker)

    # The catalog div closes just before the social section
    # Find the closing </div> that ends the catalog, right before social marker
    # Looking at the structure: line 1556 has </div> (closing catalog), then line 1558 has Social
    pre_social = html[catalog_start_idx:social_idx]
    # The catalog closing </div> is the last </div> before the social marker
    catalog_end_idx = html.rfind('</div>', catalog_start_idx, social_idx)
    # Include the </div> and newlines up to social
    catalog_content = html[catalog_start_idx:catalog_end_idx + len('</div>')]

    # --- Step 3: Extract bundles section ---
    bundles_start = catalog_content.index('<!-- Bundles Section -->')
    bundles_section_match = re.search(
        r'(<!-- Bundles Section -->.*?</section>)',
        catalog_content,
        re.DOTALL
    )
    bundles_html = bundles_section_match.group(1) if bundles_section_match else ''

    # --- Step 4: Extract all category sections ---
    category_sections = []
    category_pattern = re.compile(
        r'(<!-- [^>]+ -->\s*\n\s*<section class="section" id="[^"]+">.*?</section>)',
        re.DOTALL
    )
    for match in category_pattern.finditer(catalog_content):
        category_sections.append(match.group(1))

    print(f"Found {len(category_sections)} category sections")

    # --- Step 5: Collect published product cards from all categories ---
    published_cards = []
    for section in category_sections:
        cards = extract_product_cards(section)
        for card in cards:
            if is_published(card):
                published_cards.append(card)

    print(f"Found {len(published_cards)} published product cards in existing categories")

    # Note: some published products may appear in multiple categories (duplicates)
    # We want unique cards by filename
    seen_filenames = set()
    unique_published = []
    for card in published_cards:
        fn = get_product_filename(card)
        if fn not in seen_filenames:
            seen_filenames.add(fn)
            unique_published.append(card)

    print(f"Unique published product cards: {len(unique_published)}")

    # --- Step 6: Process category sections for "Launching Soon" ---
    launching_soon_sections = []
    for section in category_sections:
        processed = process_category_section(section)
        if processed:
            launching_soon_sections.append(processed)

    print(f"Launching Soon category sections: {len(launching_soon_sections)}")

    # Count remaining products
    total_remaining = 0
    for section in launching_soon_sections:
        total_remaining += len(extract_product_cards(section))
    print(f"Total remaining (Launching Soon) products: {total_remaining}")

    # --- Step 7: Build new catalog section ---
    new_catalog_lines = []
    new_catalog_lines.append('<div class="catalog" id="catalog">')
    new_catalog_lines.append('')

    # Available Now section
    new_catalog_lines.append(build_available_now_section(unique_published))

    # Bundles section (unchanged)
    new_catalog_lines.append(bundles_html)
    new_catalog_lines.append('')

    # Launching Soon header
    new_catalog_lines.append(build_launching_soon_wrapper_start())

    # All remaining category sections with Coming Soon badges
    for section in launching_soon_sections:
        new_catalog_lines.append(section)
        new_catalog_lines.append('')

    new_catalog_lines.append('</div>')

    new_catalog = '\n'.join(new_catalog_lines)

    # --- Step 8: Replace the old catalog with the new one ---
    # Replace from catalog_start_idx to catalog_end_idx + len('</div>')
    new_html = html[:catalog_start_idx] + new_catalog + '\n\n' + html[catalog_end_idx + len('</div>'):]

    # --- Step 9: Add CSS for new elements ---
    css_additions = """
<style>
/* Available Now & Launching Soon styles */
.available-now .section-header .section-tag {
  background: linear-gradient(135deg, #10B981, #34D399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.available-now .section-title {
  color: #10B981;
}
.published-card {
  border: 2px solid rgba(16, 185, 129, 0.3) !important;
  position: relative;
}
.published-card::before {
  content: "LIVE";
  position: absolute;
  top: 12px;
  right: 12px;
  background: linear-gradient(135deg, #10B981, #34D399);
  color: white;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  letter-spacing: 1px;
  z-index: 2;
}
.gumroad-link {
  background: linear-gradient(135deg, #FF3B8B, #A855F7) !important;
  color: white !important;
  padding: 8px 16px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.85rem;
  transition: opacity 0.2s;
}
.gumroad-link:hover {
  opacity: 0.9;
}
.free-badge {
  background: linear-gradient(135deg, #10B981, #34D399);
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 12px;
  margin-left: 8px;
}
.launching-soon-header {
  padding: 60px 0 20px;
}
.launching-soon-header .section-tag {
  background: linear-gradient(135deg, #F59E0B, #FBBF24);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.launching-soon-header .section-title {
  color: #F59E0B;
}
.coming-soon-badge {
  background: linear-gradient(135deg, #F59E0B, #FBBF24);
  color: #1a1a2e;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  margin-left: 8px;
}
.coming-soon-text {
  color: #F59E0B;
  font-weight: 600;
  font-size: 0.85rem;
  font-style: italic;
}
</style>
"""
    # Insert CSS before </head>
    new_html = new_html.replace('</head>', css_additions + '</head>')

    # --- Step 10: Write the result ---
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"\nDone! index.html has been restructured.")
    print(f"- Available Now: 2 free + {len(unique_published)} paid = {2 + len(unique_published)} products")
    print(f"- Launching Soon: {total_remaining} products across {len(launching_soon_sections)} categories")


if __name__ == '__main__':
    main()
