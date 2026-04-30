#!/usr/bin/env python3
"""Generate secure product delivery system for Girl Gone AI.

Creates:
1. Token-gated download pages for each product
2. Post-purchase thank-you pages per product
3. A master URL mapping for Gumroad integration
"""

import os
import secrets
import json
import hashlib

SITE_URL = "https://girlgone.ai"
BASE_DIR = os.path.expanduser("~/girl-gone-ai")

# All 12 live Gumroad products + esthetician (mentioned in task)
PRODUCTS = [
    {
        "slug": "ai-productivity-starter-kit",
        "name": "AI Productivity Starter Kit",
        "price": "FREE",
        "gumroad_code": "free-starter-kit",
        "category": "Digital Products",
        "desc": "Essential AI productivity tools, templates, and quick-start guides to help you work smarter from day one.",
        "product_page": None,
    },
    {
        "slug": "morning-glow-checklist",
        "name": "Free Morning Glow Checklist",
        "price": "FREE",
        "gumroad_code": "wgnvf",
        "category": "Wellness",
        "desc": "Start every morning with intention. A beautiful checklist to build your perfect morning routine — skincare, mindset, and productivity.",
        "product_page": None,
    },
    {
        "slug": "teacher-lesson-planner",
        "name": "Teacher Lesson Planner & Classroom Manager",
        "price": "$12",
        "gumroad_code": "gkdlq",
        "category": "Notion Templates",
        "desc": "Complete lesson planning system with weekly views, resource library, student tracker, and grade book — all in one Notion workspace.",
        "product_page": "products/21-teacher-lesson-planner.html",
    },
    {
        "slug": "wedding-planning-dashboard",
        "name": "Wedding Planning Dashboard",
        "price": "$18",
        "gumroad_code": "hxntlz",
        "category": "Notion Templates",
        "desc": "Your entire wedding planned in one dashboard — venue tracking, vendor management, budget calculator, guest list, and timeline.",
        "product_page": "products/22-wedding-planning-dashboard.html",
    },
    {
        "slug": "meal-prep-planner",
        "name": "Meal Prep & Recipe Planner",
        "price": "$10",
        "gumroad_code": "btxunu",
        "category": "Notion Templates",
        "desc": "Weekly meal planning, grocery lists, recipe database, and nutrition tracker — everything you need to meal prep like a pro.",
        "product_page": "products/25-meal-prep-planner.html",
    },
    {
        "slug": "student-study-system",
        "name": "Student Study System",
        "price": "$8",
        "gumroad_code": "rypqg",
        "category": "Notion Templates",
        "desc": "Assignment tracker, study schedule, note-taking system, and exam prep planner — built for students who want to study smarter.",
        "product_page": "products/26-student-study-system.html",
    },
    {
        "slug": "midjourney-prompts",
        "name": "Midjourney & AI Art Prompt Pack",
        "price": "$17",
        "gumroad_code": "rjfayx",
        "category": "AI Prompt Packs",
        "desc": "200+ tested Midjourney prompts across 15 categories — portraits, landscapes, product photos, logos, and more. Copy, paste, create.",
        "product_page": "products/24-midjourney-prompts.html",
    },
    {
        "slug": "invoice-generator",
        "name": "Professional Invoice Generator",
        "price": "$8",
        "gumroad_code": "thtyoc",
        "category": "Spreadsheet Tools",
        "desc": "Professional invoice templates with auto-calculations, client tracking, payment status, and export-ready formatting.",
        "product_page": "products/19-invoice-generator.html",
    },
    {
        "slug": "side-hustle-tracker",
        "name": "Side Hustle Income & Expense Tracker",
        "price": "$9",
        "gumroad_code": "xrlbjs",
        "category": "Spreadsheet Tools",
        "desc": "Track every dollar your side hustle makes and spends. Revenue dashboards, expense categories, profit margins, and tax prep.",
        "product_page": "products/23-side-hustle-tracker.html",
    },
    {
        "slug": "proposal-template",
        "name": "Client Proposal Template Kit",
        "price": "$10",
        "gumroad_code": "baqfdx",
        "category": "Workflow Kits",
        "desc": "Win more clients with polished, professional proposals. Customizable templates for freelancers, agencies, and consultants.",
        "product_page": "products/20-proposal-template.html",
    },
    {
        "slug": "podcast-launch-kit",
        "name": "Podcast Launch Kit",
        "price": "$14",
        "gumroad_code": "27-podcast-launch-kit",
        "category": "Workflow Kits",
        "desc": "Everything you need to launch a podcast — episode planner, guest outreach templates, equipment checklist, and launch timeline.",
        "product_page": "products/27-podcast-launch-kit.html",
    },
    {
        "slug": "product-launch-playbook",
        "name": "Product Launch Playbook",
        "price": "$12",
        "gumroad_code": "apbls",
        "category": "Digital Products",
        "desc": "Step-by-step playbook for launching digital products — pre-launch checklist, launch day plan, email sequences, and post-launch optimization.",
        "product_page": "products/18-product-launch-checklist.html",
    },
    {
        "slug": "esthetician-client-management",
        "name": "Esthetician Client Management System",
        "price": "$15",
        "gumroad_code": "esthetician-client-mgmt",
        "category": "Beauty & Wellness",
        "desc": "Complete client management for estheticians — intake forms, treatment logs, product recommendations, rebooking reminders, and revenue tracking.",
        "product_page": "products/142-esthetician-client-management.html",
    },
]


def generate_token():
    """Generate a URL-safe token for product access."""
    return secrets.token_urlsafe(24)


def make_download_page(product, token):
    """Create a token-gated download page."""
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    slug = product["slug"]
    name = product["name"]

    # Check if there's an existing download page with content
    existing_path = os.path.join(BASE_DIR, "downloads", f"{slug}.html")
    has_existing = os.path.exists(existing_path)

    # Check for numbered versions
    numbered_mappings = {
        "teacher-lesson-planner": "21-teacher-lesson-planner",
        "wedding-planning-dashboard": "22-wedding-planning-dashboard",
        "meal-prep-planner": "25-meal-prep-planner",
        "student-study-system": "26-student-study-system",
        "midjourney-prompts": "24-midjourney-prompts",
        "invoice-generator": "19-invoice-generator",
        "side-hustle-tracker": "23-side-hustle-tracker",
        "proposal-template": "20-proposal-template",
        "podcast-launch-kit": "27-podcast-launch-kit",
        "product-launch-playbook": "18-product-launch-checklist",
    }

    # Build product content sections based on category
    content_sections = get_product_content(product)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="noindex, nofollow" />
<title>{name} — Download | Girl Gone AI</title>
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

<!-- Access denied wall (shown when no valid token) -->
<div class="access-wall" id="accessWall">
  <h1>Access Required</h1>
  <p>This download page requires a valid purchase token. If you purchased this product, please use the link from your Gumroad receipt.</p>
  <p><a href="{SITE_URL}">Back to Girl Gone AI</a></p>
</div>

<!-- Actual download content (hidden until token validated) -->
<div class="download-container" id="downloadContent">
  <div class="download-header">
    <div class="check">&#10003;</div>
    <h1>{name}</h1>
    <p class="subtitle">Thank you for your purchase! Your product is ready below.</p>
  </div>

{content_sections}

  <div class="support-note">
    <p>Need help? Email <a href="mailto:support@girlgone.ai">support@girlgone.ai</a></p>
    <p style="margin-top:8px"><a href="{SITE_URL}">Browse more products</a></p>
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
</html>'''


def get_product_content(product):
    """Generate product-specific content sections."""
    slug = product["slug"]
    name = product["name"]
    cat = product["category"]
    desc = product["desc"]

    # Product-specific "What's Inside" content
    contents = {
        "ai-productivity-starter-kit": [
            "AI Productivity Quick-Start Guide (PDF)",
            "5 Ready-to-Use ChatGPT Prompt Templates",
            "Weekly AI Workflow Planner Template",
            "AI Tool Comparison Cheat Sheet",
            "30-Day AI Productivity Challenge Checklist",
        ],
        "morning-glow-checklist": [
            "Morning Glow Routine Checklist (Printable PDF)",
            "Skincare Step-by-Step Guide",
            "Mindset & Affirmation Prompts",
            "Productivity Power Hour Framework",
            "Weekly Habit Tracker Template",
        ],
        "teacher-lesson-planner": [
            "Complete Notion Lesson Planner Template",
            "Weekly & Monthly Planning Views",
            "Student Progress Tracker Database",
            "Resource Library with Tags & Categories",
            "Grade Book with Auto-Calculations",
            "Substitute Teacher Info Sheet",
        ],
        "wedding-planning-dashboard": [
            "Full Notion Wedding Dashboard Template",
            "Vendor Comparison & Booking Tracker",
            "Budget Calculator with Category Breakdown",
            "Guest List Manager with RSVP Tracking",
            "Wedding Timeline & Day-Of Schedule",
            "Seating Chart Planner",
        ],
        "meal-prep-planner": [
            "Notion Meal Prep Dashboard Template",
            "Weekly Meal Planning Calendar",
            "Grocery List Auto-Generator",
            "Recipe Database with Nutrition Info",
            "Meal Prep Batch Cooking Guide",
            "Pantry Inventory Tracker",
        ],
        "student-study-system": [
            "Notion Student Dashboard Template",
            "Assignment & Deadline Tracker",
            "Study Schedule Builder",
            "Note-Taking System with Cornell Method",
            "Exam Prep Countdown Planner",
            "GPA Calculator",
        ],
        "midjourney-prompts": [
            "200+ Tested Midjourney Prompts (PDF + Notion)",
            "15 Category Collections (Portraits, Landscapes, Products, etc.)",
            "Prompt Formula Cheat Sheet",
            "Style Reference Guide with Examples",
            "Parameter & Settings Quick Reference",
            "Bonus: 20 DALL-E & Stable Diffusion Prompts",
        ],
        "invoice-generator": [
            "Professional Invoice Spreadsheet Template",
            "Auto-Calculating Tax & Totals",
            "Client Information Database",
            "Payment Status Tracker",
            "Multiple Currency Support",
            "Print-Ready & PDF Export Formats",
        ],
        "side-hustle-tracker": [
            "Income & Expense Tracking Spreadsheet",
            "Revenue Dashboard with Charts",
            "Expense Category Breakdown",
            "Monthly Profit & Loss Summary",
            "Tax Deduction Tracker",
            "Quarterly Earnings Report Template",
        ],
        "proposal-template": [
            "3 Professional Proposal Templates (Google Docs)",
            "Project Scope & Timeline Framework",
            "Pricing Table with Optional Add-Ons",
            "Terms & Conditions Template",
            "Follow-Up Email Sequences",
            "Client Onboarding Checklist",
        ],
        "podcast-launch-kit": [
            "Podcast Launch Checklist (30-Day Plan)",
            "Episode Planning Template",
            "Guest Outreach Email Templates",
            "Equipment Buying Guide (Budget & Pro)",
            "Show Notes Template with SEO Tips",
            "Launch Day Marketing Checklist",
        ],
        "product-launch-playbook": [
            "Complete Launch Playbook (PDF + Notion)",
            "Pre-Launch Checklist (60 Items)",
            "Launch Day Hour-by-Hour Plan",
            "Email Sequence Templates (5 Emails)",
            "Social Media Launch Calendar",
            "Post-Launch Optimization Guide",
        ],
        "esthetician-client-management": [
            "Client Intake Form Templates",
            "Treatment Log & History Tracker",
            "Product Recommendation System",
            "Rebooking Reminder Calendar",
            "Revenue & Service Tracking Dashboard",
            "Aftercare Instructions Templates",
        ],
    }

    items = contents.get(slug, [f"{name} — Full Digital Product", "Step-by-Step Setup Guide", "Bonus Resources"])
    items_html = "\n".join(f"      <li>{item}</li>" for item in items)

    # How to use section based on category
    if "Notion" in cat:
        how_to = '''
    <ol style="color:#ccc;font-size:0.9rem;padding-left:20px;line-height:2">
      <li>Click the download button below to open the Notion template</li>
      <li>Click "Duplicate" in the top-right corner to add it to your Notion workspace</li>
      <li>Customize the template with your own information</li>
      <li>Start using it immediately — all views and databases are pre-built</li>
    </ol>'''
    elif "Spreadsheet" in cat:
        how_to = '''
    <ol style="color:#ccc;font-size:0.9rem;padding-left:20px;line-height:2">
      <li>Click the download button to get your spreadsheet file</li>
      <li>Open in Google Sheets or Excel</li>
      <li>Make a copy (File > Make a Copy) to start editing</li>
      <li>Follow the instructions tab for setup tips</li>
    </ol>'''
    elif "Prompt" in cat:
        how_to = '''
    <ol style="color:#ccc;font-size:0.9rem;padding-left:20px;line-height:2">
      <li>Download the prompt pack (PDF + Notion version included)</li>
      <li>Browse prompts by category to find what you need</li>
      <li>Copy any prompt and paste it into your AI tool</li>
      <li>Customize the bracketed [variables] for your specific needs</li>
    </ol>'''
    else:
        how_to = '''
    <ol style="color:#ccc;font-size:0.9rem;padding-left:20px;line-height:2">
      <li>Click the download button below to access your product</li>
      <li>Save the files to your device or cloud storage</li>
      <li>Follow the included quick-start guide</li>
      <li>Start using your new tools immediately</li>
    </ol>'''

    product_page_link = product.get("product_page", "")
    view_product = ""
    if product_page_link:
        view_product = f'\n  <div style="text-align:center;margin-bottom:24px"><a href="{SITE_URL}/{product_page_link}" class="download-btn" style="background:rgba(255,255,255,0.08);box-shadow:none;font-size:0.85rem;padding:10px 24px">View Full Product Details</a></div>'

    return f'''
  <div class="content-card">
    <h2>What\'s Inside</h2>
    <ul>
{items_html}
    </ul>
  </div>
{view_product}
  <div class="content-card">
    <h2>How to Use</h2>
{how_to}
  </div>

  <div style="text-align:center;padding:32px 0">
    <p style="color:#888;font-size:0.85rem;margin-bottom:16px">Your product is ready for download:</p>
    <a href="{SITE_URL}/downloads/files/{slug}.html" class="download-btn">Access Your Product</a>
  </div>'''


def make_thankyou_page():
    """Create a single post-purchase thank-you page that routes by product param."""
    products_json = json.dumps({p["slug"]: {"name": p["name"], "price": p["price"]} for p in PRODUCTS})

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="noindex, nofollow" />
<title>Thank You! — Girl Gone AI</title>
<link rel="icon" type="image/svg+xml" href="./favicon.svg">
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
  display: flex;
  flex-direction: column;
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
.container {{
  max-width: 600px;
  margin: 80px auto;
  padding: 0 24px;
  text-align: center;
  flex: 1;
}}
.success-icon {{
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #10B981, #34D399);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 24px;
  font-size: 36px;
  box-shadow: 0 8px 30px rgba(16,185,129,0.3);
}}
h1 {{
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.subtitle {{
  color: #888;
  font-size: 1rem;
  margin-bottom: 32px;
  line-height: 1.6;
}}
.product-name {{
  font-size: 1.2rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 8px;
}}
.info-card {{
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 32px;
  margin-bottom: 24px;
}}
.info-card p {{
  color: #bbb;
  font-size: 0.9rem;
  line-height: 1.7;
}}
.download-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #FF3B8B, #A855F7);
  color: #fff;
  padding: 16px 40px;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 700;
  font-size: 1.1rem;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(255,59,139,0.3);
  margin-bottom: 24px;
}}
.download-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(255,59,139,0.4);
}}
.next-steps {{
  text-align: left;
  background: rgba(168,85,247,0.08);
  border: 1px solid rgba(168,85,247,0.15);
  border-radius: 12px;
  padding: 24px;
  margin-top: 32px;
}}
.next-steps h3 {{
  color: #A855F7;
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: 1px;
  text-transform: uppercase;
}}
.next-steps li {{
  color: #bbb;
  font-size: 0.85rem;
  margin-bottom: 8px;
  line-height: 1.5;
}}
.footer {{
  text-align: center;
  padding: 24px;
  color: #555;
  font-size: 0.8rem;
  border-top: 1px solid rgba(255,255,255,0.04);
}}
.footer a {{
  color: #A855F7;
  text-decoration: none;
}}
</style>
</head>
<body>
<div class="brand-bar">
  <div class="logo">Girl Gone AI</div>
</div>

<div class="container">
  <div class="success-icon">&#10003;</div>
  <h1>Thank You!</h1>
  <p class="subtitle">Your purchase was successful. Your product is ready for immediate access.</p>

  <div class="info-card">
    <p class="product-name" id="productName">Your Product</p>
    <p>Check your email for the Gumroad receipt. You can also access your product directly using the button below.</p>
  </div>

  <a href="#" id="downloadLink" class="download-btn">Access Your Download</a>

  <div class="next-steps">
    <h3>What Happens Next</h3>
    <ol>
      <li>Click the button above to access your product</li>
      <li>Follow the setup guide included with your download</li>
      <li>A copy of your receipt has been sent to your email</li>
      <li>Need help? Email support@girlgone.ai</li>
    </ol>
  </div>
</div>

<div class="footer">
  <p>&copy; 2026 Girl Gone AI. <a href="{SITE_URL}">Browse more products</a></p>
</div>

<script>
(function() {{
  var params = new URLSearchParams(window.location.search);
  var product = params.get("product");
  var token = params.get("token");
  var products = {products_json};
  if (product && products[product]) {{
    document.getElementById("productName").textContent = products[product].name;
    document.title = "Thank You for purchasing " + products[product].name + " | Girl Gone AI";
  }}
  if (product && token) {{
    document.getElementById("downloadLink").href = "{SITE_URL}/downloads/secure/" + product + ".html?token=" + token;
  }}
}})();
</script>
</body>
</html>'''


def main():
    # Generate tokens
    token_map = {}
    for product in PRODUCTS:
        token_map[product["slug"]] = generate_token()

    # Save token map
    os.makedirs(os.path.join(BASE_DIR, "downloads", "secure"), exist_ok=True)

    token_file = os.path.join(BASE_DIR, "downloads", "secure", ".tokens.json")
    with open(token_file, "w") as f:
        json.dump(token_map, f, indent=2)

    # Generate secure download pages
    for product in PRODUCTS:
        token = token_map[product["slug"]]
        html = make_download_page(product, token)
        path = os.path.join(BASE_DIR, "downloads", "secure", f"{product['slug']}.html")
        with open(path, "w") as f:
            f.write(html)

    # Generate thank-you page
    thankyou = make_thankyou_page()
    with open(os.path.join(BASE_DIR, "thank-you.html"), "w") as f:
        f.write(thankyou)

    # Generate product file content pages (the actual downloadable content)
    # These are simple pages that link to the existing download/product content
    os.makedirs(os.path.join(BASE_DIR, "downloads", "files"), exist_ok=True)
    for product in PRODUCTS:
        slug = product["slug"]
        name = product["name"]
        # Create a redirect page to existing product content
        existing_download = os.path.join(BASE_DIR, "downloads", f"{slug}.html")
        if os.path.exists(existing_download):
            target = f"/downloads/{slug}.html"
        elif product.get("product_page"):
            target = f"/{product['product_page']}"
        else:
            target = f"/downloads/secure/{slug}.html"

        file_page = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{name} — File Access | Girl Gone AI</title>
<meta http-equiv="refresh" content="0;url={target}">
</head><body><p>Redirecting to your product... <a href="{target}">Click here</a> if not redirected.</p></body></html>'''
        with open(os.path.join(BASE_DIR, "downloads", "files", f"{slug}.html"), "w") as f:
            f.write(file_page)

    # Print the URL mapping table
    print("\n" + "=" * 100)
    print("SECURE PRODUCT DELIVERY SYSTEM — URL MAPPING")
    print("=" * 100)
    print(f"\n{'Product':<45} {'Price':<8} {'Gumroad Receipt URL (paste into Gumroad)'}")
    print("-" * 100)

    for product in PRODUCTS:
        slug = product["slug"]
        token = token_map[slug]
        receipt_url = f"{SITE_URL}/thank-you.html?product={slug}&token={token}"
        print(f"{product['name']:<45} {product['price']:<8} {receipt_url}")

    print("\n" + "-" * 100)
    print("\nDirect download URLs (alternative — skips thank-you page):")
    print("-" * 100)
    for product in PRODUCTS:
        slug = product["slug"]
        token = token_map[slug]
        direct_url = f"{SITE_URL}/downloads/secure/{slug}.html?token={token}"
        print(f"{product['name']:<45} {direct_url}")

    print(f"\nPost-purchase thank-you page: {SITE_URL}/thank-you.html")
    print(f"Token map saved to: downloads/secure/.tokens.json")
    print(f"\nFiles generated: {len(PRODUCTS)} secure download pages + 1 thank-you page + {len(PRODUCTS)} file redirects")


if __name__ == "__main__":
    main()
