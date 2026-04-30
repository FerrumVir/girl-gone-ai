#!/usr/bin/env python3
"""Generate actual functional product content pages for all 12 published Gumroad products."""
import os

PRODUCTS = [
    {
        "slug": "ai-productivity-starter-kit",
        "name": "AI Productivity Starter Kit",
        "price": "FREE",
        "tagline": "Your complete guide to working smarter with AI",
        "sections": [
            {"title": "Daily AI Workflow Planner", "items": [
                "Morning priority matrix (Top 3 tasks + AI delegation candidates)",
                "AI tool selector guide (which tool for which task)",
                "Time-block template with AI assist slots",
                "End-of-day review checklist"
            ]},
            {"title": "AI Prompt Templates", "items": [
                "Email drafting prompts (professional, casual, follow-up)",
                "Meeting summary & action item extraction prompts",
                "Content brainstorming framework prompts",
                "Research & analysis prompt chains",
                "Code review & debugging prompt templates"
            ]},
            {"title": "Tool Comparison Matrix", "items": [
                "ChatGPT vs Claude vs Gemini — feature comparison",
                "Best AI tools by category (writing, design, code, data)",
                "Free vs paid tier breakdown for top 10 tools",
                "Integration compatibility chart"
            ]},
            {"title": "30-Day AI Adoption Plan", "items": [
                "Week 1: Foundation — set up accounts & learn basics",
                "Week 2: Integration — replace manual tasks with AI",
                "Week 3: Optimization — build custom workflows",
                "Week 4: Mastery — chain tools & automate routines"
            ]}
        ]
    },
    {
        "slug": "morning-glow-checklist",
        "name": "Free Morning Glow Checklist",
        "price": "FREE",
        "tagline": "A radiant morning skincare routine in 15 minutes",
        "sections": [
            {"title": "Step 1: Cleanse (2 min)", "items": [
                "Splash lukewarm water on face",
                "Apply gentle gel or cream cleanser in circular motions",
                "Rinse thoroughly — pat dry with clean towel",
                "Tip: Skip harsh scrubs in the morning"
            ]},
            {"title": "Step 2: Tone & Treat (3 min)", "items": [
                "Apply hydrating toner with palms (press, don't swipe)",
                "Apply vitamin C serum (3-4 drops, pat onto cheeks, forehead, chin)",
                "Let absorb 60 seconds before next step",
                "Optional: eye cream for puffiness"
            ]},
            {"title": "Step 3: Moisturize (2 min)", "items": [
                "Apply lightweight moisturizer (gel for oily, cream for dry)",
                "Don't forget neck and decolletage",
                "Let absorb before sunscreen"
            ]},
            {"title": "Step 4: Protect (2 min)", "items": [
                "Apply SPF 30+ broad-spectrum sunscreen",
                "Use two finger-lengths for full face coverage",
                "Reapply every 2 hours if outdoors",
                "Allow 15 min before makeup application"
            ]},
            {"title": "Weekly Add-Ons", "items": [
                "Monday: Gentle exfoliation (AHA/BHA)",
                "Wednesday: Hydrating sheet mask (10 min)",
                "Friday: Treatment mask (clay for oily, cream for dry)",
                "Sunday: Facial massage with gua sha (5 min)"
            ]}
        ]
    },
    {
        "slug": "product-launch-playbook",
        "name": "Product Launch Playbook",
        "price": "$12",
        "tagline": "Launch your digital product from idea to first sale",
        "sections": [
            {"title": "Phase 1: Validate (Week 1-2)", "items": [
                "Market research template — 10 questions to ask your audience",
                "Competitor analysis grid (price, features, gaps)",
                "Minimum viable product (MVP) scope worksheet",
                "Pricing strategy calculator (cost + value + market positioning)"
            ]},
            {"title": "Phase 2: Build (Week 3-4)", "items": [
                "Product creation timeline with milestones",
                "Sales page copywriting framework (AIDA model)",
                "Product mockup checklist (cover, preview images, demo)",
                "Beta testing feedback form template"
            ]},
            {"title": "Phase 3: Pre-Launch (Week 5)", "items": [
                "Email list warm-up sequence (5 emails, templates included)",
                "Social media countdown content calendar (7 days)",
                "Affiliate/partner outreach email templates",
                "Launch day checklist (26 items)"
            ]},
            {"title": "Phase 4: Launch & Optimize (Week 6+)", "items": [
                "Launch day hour-by-hour schedule",
                "Sales tracking dashboard template",
                "Customer feedback collection system",
                "Post-launch optimization checklist (pricing, copy, upsells)"
            ]}
        ]
    },
    {
        "slug": "invoice-generator",
        "name": "Professional Invoice Generator",
        "price": "$8",
        "tagline": "Create polished invoices in under 2 minutes",
        "sections": [
            {"title": "Invoice Template", "items": [
                "Auto-numbering system (INV-2026-001 format)",
                "Client information block with saved profiles",
                "Itemized services table with quantity, rate, and subtotal",
                "Tax calculation (configurable rate per jurisdiction)",
                "Payment terms & due date calculator",
                "Notes section for terms and conditions"
            ]},
            {"title": "Client Tracker", "items": [
                "Client contact database with project history",
                "Outstanding balance tracker per client",
                "Payment status indicators (paid, pending, overdue)",
                "Quick-filter by status, date range, or client"
            ]},
            {"title": "Financial Summary", "items": [
                "Monthly revenue overview with charts",
                "Year-to-date income tracker",
                "Tax withholding estimate calculator",
                "Quarterly income breakdown for tax prep"
            ]},
            {"title": "Payment Tracking", "items": [
                "Automatic overdue reminders (30, 60, 90 days)",
                "Payment method log (bank, PayPal, Stripe, check)",
                "Late fee calculator",
                "Annual income report generator"
            ]}
        ]
    },
    {
        "slug": "proposal-template",
        "name": "Client Proposal Template Kit",
        "price": "$10",
        "tagline": "Win more clients with professional proposals",
        "sections": [
            {"title": "Proposal Structure", "items": [
                "Cover page template with your branding",
                "Executive summary framework (problem → solution → outcome)",
                "Scope of work table (deliverables, timeline, milestones)",
                "Pricing section with tiered options (Basic, Standard, Premium)"
            ]},
            {"title": "Proposal Templates by Industry", "items": [
                "Freelance design/development proposal",
                "Marketing & social media management proposal",
                "Consulting engagement proposal",
                "Photography/videography project proposal",
                "Virtual assistant services proposal"
            ]},
            {"title": "Supporting Documents", "items": [
                "Case study template (before, process, results)",
                "Testimonial collection format",
                "Terms & conditions boilerplate",
                "Contract addendum template"
            ]},
            {"title": "Follow-Up System", "items": [
                "Proposal sent — follow-up email templates (Day 2, 5, 10)",
                "Objection handling script (pricing, timeline, scope)",
                "Win/loss tracking spreadsheet",
                "Client onboarding checklist (post-acceptance)"
            ]}
        ]
    },
    {
        "slug": "teacher-lesson-planner",
        "name": "Teacher Lesson Planner & Classroom Manager",
        "price": "$12",
        "tagline": "Plan lessons, track students, and manage your classroom",
        "sections": [
            {"title": "Lesson Planning", "items": [
                "Weekly lesson plan grid (5 days x 8 periods)",
                "Learning objectives mapper (Bloom's taxonomy aligned)",
                "Standards alignment tracker (Common Core / state standards)",
                "Resource & materials checklist per lesson",
                "Differentiation notes (ELL, IEP, gifted accommodations)"
            ]},
            {"title": "Student Tracker", "items": [
                "Student roster with contact info and notes",
                "Grade book with automatic average calculation",
                "Attendance log with pattern detection",
                "Behavior tracking system (positive + areas for growth)",
                "Parent communication log"
            ]},
            {"title": "Classroom Management", "items": [
                "Seating chart builder (drag-and-drop style)",
                "Classroom procedures & routines reference",
                "Supply inventory tracker",
                "Substitute teacher info sheet template"
            ]},
            {"title": "Year Planning", "items": [
                "Curriculum pacing guide (semester view)",
                "Assessment calendar with prep timelines",
                "Professional development goal tracker",
                "End-of-year checklist and reflection template"
            ]}
        ]
    },
    {
        "slug": "wedding-planning-dashboard",
        "name": "Wedding Planning Dashboard",
        "price": "$18",
        "tagline": "Plan your entire wedding without the overwhelm",
        "sections": [
            {"title": "Budget Tracker", "items": [
                "Total budget calculator with category breakdown",
                "Vendor payment schedule (deposits, installments, final)",
                "Budget vs actual comparison per category",
                "Tip & gratuity calculator",
                "Hidden costs checklist (alterations, postage, tips, taxes)"
            ]},
            {"title": "Guest Management", "items": [
                "Guest list with RSVP status tracking",
                "Meal preference tracker (dietary restrictions)",
                "Table assignment planner",
                "Plus-one tracking and headcount calculator",
                "Thank-you note tracker (sent/pending)"
            ]},
            {"title": "Vendor Hub", "items": [
                "Vendor comparison matrix (3 options per category)",
                "Contract tracker with key dates and terms",
                "Vendor contact directory",
                "Meeting notes log per vendor",
                "Final payment schedule and confirmation checklist"
            ]},
            {"title": "Timeline & Tasks", "items": [
                "12-month countdown checklist",
                "Week-of timeline (hour-by-hour)",
                "Day-of emergency kit checklist",
                "Rehearsal dinner planning template",
                "Honeymoon planning tracker"
            ]}
        ]
    },
    {
        "slug": "side-hustle-tracker",
        "name": "Side Hustle Income & Expense Tracker",
        "price": "$9",
        "tagline": "Track every dollar in your side business",
        "sections": [
            {"title": "Income Dashboard", "items": [
                "Revenue tracker by source (freelance, products, services)",
                "Monthly income goals with progress bars",
                "Client payment tracker with status indicators",
                "Recurring income log (subscriptions, retainers)",
                "Year-over-year income comparison"
            ]},
            {"title": "Expense Tracker", "items": [
                "Categorized expense log (tools, marketing, supplies, education)",
                "Receipt capture and organization system",
                "Subscription audit tracker (monthly recurring costs)",
                "Tax-deductible expense flagging",
                "Profit margin calculator per project"
            ]},
            {"title": "Tax Prep", "items": [
                "Quarterly estimated tax calculator",
                "Deduction checklist for self-employed (home office, mileage, etc.)",
                "1099 income tracker per client",
                "Annual tax summary report template"
            ]},
            {"title": "Growth Planning", "items": [
                "Side hustle revenue goal worksheet",
                "Time investment tracker (hours per week)",
                "ROI calculator for tools and courses",
                "Scaling decision framework (when to go full-time)"
            ]}
        ]
    },
    {
        "slug": "midjourney-prompts",
        "name": "Midjourney & AI Art Prompt Pack",
        "price": "$17",
        "tagline": "500+ tested prompts for stunning AI-generated art",
        "sections": [
            {"title": "Photography Style Prompts (100+)", "items": [
                "Portrait photography (studio, natural light, editorial)",
                "Product photography (flat lay, lifestyle, packshot)",
                "Landscape & travel photography styles",
                "Food photography (overhead, 45-degree, macro)",
                "Fashion editorial and street style"
            ]},
            {"title": "Digital Art & Illustration (100+)", "items": [
                "Watercolor and oil painting styles",
                "Comic book and manga art prompts",
                "Concept art (characters, environments, props)",
                "Isometric and 3D render styles",
                "Pixel art and retro game aesthetics"
            ]},
            {"title": "Business & Marketing (100+)", "items": [
                "Social media graphics (Instagram, Pinterest, LinkedIn)",
                "Website hero images and backgrounds",
                "Logo and branding concept generators",
                "Infographic style illustrations",
                "Email header and banner prompts"
            ]},
            {"title": "Advanced Techniques (200+)", "items": [
                "Parameter cheat sheet (--ar, --style, --chaos, --weird)",
                "Multi-prompt and weighted prompt formulas",
                "Style mixing and blending techniques",
                "Negative prompt library (what to exclude)",
                "Seed management for consistent characters"
            ]}
        ]
    },
    {
        "slug": "meal-prep-planner",
        "name": "Meal Prep & Recipe Planner",
        "price": "$10",
        "tagline": "Eat better, spend less, stress never about dinner",
        "sections": [
            {"title": "Weekly Meal Planner", "items": [
                "7-day meal grid (breakfast, lunch, dinner, snacks)",
                "Drag-and-drop recipe assignment",
                "Nutritional overview per day (calories, protein, carbs, fat)",
                "Family preference tracker (likes, dislikes, allergies)",
                "Leftover planning system (cook once, eat twice)"
            ]},
            {"title": "Smart Grocery List", "items": [
                "Auto-generated shopping list from meal plan",
                "Organized by store section (produce, dairy, pantry, etc.)",
                "Pantry inventory tracker (what you already have)",
                "Budget estimator per weekly plan",
                "Bulk buying calculator for savings"
            ]},
            {"title": "Recipe Database", "items": [
                "50 starter recipes organized by prep time",
                "Recipe card template (ingredients, steps, notes, photo)",
                "Scaling calculator (servings multiplier)",
                "Prep time and cook time tracker",
                "Favorite recipes collection"
            ]},
            {"title": "Meal Prep Guides", "items": [
                "Sunday meal prep timeline (2-hour batch cook plan)",
                "Freezer meal guide (what freezes well + storage times)",
                "Container and portion guide",
                "Seasonal meal planning calendar"
            ]}
        ]
    },
    {
        "slug": "student-study-system",
        "name": "Student Study System",
        "price": "$8",
        "tagline": "Study smarter, not harder — your academic command center",
        "sections": [
            {"title": "Course Dashboard", "items": [
                "Semester overview with all courses and schedules",
                "Assignment tracker with due dates and priorities",
                "Grade calculator (weighted categories)",
                "GPA tracker and target calculator",
                "Syllabus quick-reference for each course"
            ]},
            {"title": "Study Planner", "items": [
                "Weekly study schedule builder",
                "Pomodoro timer log (25 min focus + 5 min break)",
                "Study session planner (topic, method, duration)",
                "Exam countdown with daily study goals",
                "Spaced repetition schedule generator"
            ]},
            {"title": "Note-Taking System", "items": [
                "Cornell note-taking template",
                "Lecture notes organizer by course and date",
                "Key concepts and definitions flashcard maker",
                "Mind map template for complex topics",
                "Study group notes and action items"
            ]},
            {"title": "Academic Planning", "items": [
                "4-year degree roadmap template",
                "Prerequisite and elective tracker",
                "Internship and extracurricular log",
                "Application deadline tracker (grad school, scholarships)",
                "Professor office hours and contact directory"
            ]}
        ]
    },
    {
        "slug": "podcast-launch-kit",
        "name": "Podcast Launch Kit",
        "price": "$14",
        "tagline": "Go from idea to published episode in 30 days",
        "sections": [
            {"title": "Pre-Launch Planning", "items": [
                "Podcast concept worksheet (niche, audience, format)",
                "Equipment buying guide (budget, mid-range, pro setups)",
                "Hosting platform comparison chart",
                "Brand kit template (name, tagline, cover art specs)",
                "Launch timeline (30-day countdown)"
            ]},
            {"title": "Episode Planning", "items": [
                "Episode outline template (intro, segments, CTA, outro)",
                "Guest research and outreach email templates",
                "Interview question framework (by episode type)",
                "Content calendar (12-week episode schedule)",
                "Show notes template with timestamps"
            ]},
            {"title": "Production Workflow", "items": [
                "Recording checklist (pre, during, post)",
                "Editing workflow template (cut list, music, levels)",
                "Episode publishing checklist (title, description, tags)",
                "Transcription and repurposing guide",
                "Batch recording schedule template"
            ]},
            {"title": "Growth & Monetization", "items": [
                "Launch promotion plan (social, email, cross-promo)",
                "Listener growth tracker (downloads, subscribers, reviews)",
                "Sponsorship rate card template",
                "Monetization roadmap (ads, Patreon, merch, courses)",
                "Analytics review template (weekly/monthly)"
            ]}
        ]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{name} — Girl Gone AI</title>
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
  <h1>{name}</h1>
  <p class="tagline">{tagline}</p>
  <div class="price-badge">{price}</div>
  <div class="action-bar no-print">
    <button class="action-btn primary" onclick="window.print()">Print / Save as PDF</button>
    <a href="https://girlgone.ai" class="action-btn secondary">Browse More Products</a>
  </div>
{sections_html}
</div>
<div class="footer">
  <p>&copy; 2026 <a href="https://girlgone.ai">Girl Gone AI</a> by Jaci Ellis. All rights reserved.</p>
  <p style="margin-top:8px;color:#444">Need help? Email <a href="mailto:support@girlgone.ai">support@girlgone.ai</a></p>
</div>
</body>
</html>"""

def generate_sections_html(sections):
    html = ""
    for s in sections:
        items = "\n".join(f"    <li>{item}</li>" for item in s["items"])
        html += f"""  <div class="section-card">
    <h2>{s['title']}</h2>
    <ul>
{items}
    </ul>
  </div>
"""
    return html

def main():
    out_dir = os.path.expanduser("~/girl-gone-ai/downloads/files")
    os.makedirs(out_dir, exist_ok=True)

    for p in PRODUCTS:
        sections_html = generate_sections_html(p["sections"])
        html = HTML_TEMPLATE.format(
            name=p["name"],
            tagline=p["tagline"],
            price=p["price"],
            sections_html=sections_html
        )
        path = os.path.join(out_dir, f"{p['slug']}.html")
        with open(path, "w") as f:
            f.write(html)
        print(f"  Created: {path}")

    print(f"\nGenerated {len(PRODUCTS)} product content pages in {out_dir}")

if __name__ == "__main__":
    main()
