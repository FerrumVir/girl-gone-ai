#!/usr/bin/env python3
"""Generate missing 90s-vibe covers for ALL Gumroad products and push to Gumroad."""

import os
import sys
import math
import random
import json
import urllib.request
import urllib.parse

# Import the cover generation functions from the existing script
sys.path.insert(0, "/home/boogarweed/girl-gone-ai/covers2")
from generate_edgy_90s import (
    draw_90s_edgy_cover, HOT_PINK, TEAL, ELECTRIC_PURPLE, LIME,
    NEON_YELLOW, BRIGHT_ORANGE, CORAL, LAVENDER, BABY_BLUE, MINT
)

OUT_DIR = "/home/boogarweed/girl-gone-ai/covers2"
GUMROAD_TOKEN = "45VytzHmDU81KleNEbwqO16iOAlifbcMg_GIMrGWS5I"

# Map Gumroad product names to cover definitions
# Format: product_name_substring -> {cover params}
PRODUCT_COVERS = {
    "Salary Negotiation Playbook": {
        "title": "Salary\nNegotiation", "subtitle": "Scripts, templates & strategies to earn more",
        "category": "Career", "bg": ((100, 30, 20), (45, 12, 8)),
        "accent": BRIGHT_ORANGE, "icon": "dollar", "file": "salary-negotiation.png"
    },
    "Habit Streak Tracker": {
        "title": "Habit Streak\nTracker", "subtitle": "Build habits that actually stick",
        "category": "Productivity", "bg": ((80, 20, 90), (35, 8, 40)),
        "accent": LIME, "icon": "calendar", "file": "habit-streak-tracker.png"
    },
    "Coding Assistant AI Prompt Pack": {
        "title": "Coding AI\nPrompt Pack", "subtitle": "200+ prompts for developers",
        "category": "AI Tools", "bg": ((15, 30, 70), (5, 12, 30)),
        "accent": TEAL, "icon": "cpu", "file": "coding-assistant-prompts.png"
    },
    "Job Search Command Center": {
        "title": "Job Search\nCommand Center", "subtitle": "Track every application & follow-up",
        "category": "Career", "bg": ((20, 40, 90), (8, 18, 40)),
        "accent": BABY_BLUE, "icon": "briefcase", "file": "job-search-command-center.png"
    },
    "Freelance Contract & Scope Template Kit": {
        "title": "Freelance\nContracts", "subtitle": "Professional contract templates for freelancers",
        "category": "Business", "bg": ((40, 30, 80), (18, 12, 35)),
        "accent": LAVENDER, "icon": "invoice", "file": "freelance-contracts.png"
    },
    "Home Renovation Budget Tracker": {
        "title": "Home Reno\nBudget", "subtitle": "Track every dollar of your renovation",
        "category": "Finance", "bg": ((80, 50, 20), (35, 22, 8)),
        "accent": NEON_YELLOW, "icon": "piggybank", "file": "home-renovation-budget.png"
    },
    "AI Business Prompts Pack": {
        "title": "AI Business\nPrompts", "subtitle": "Scale your business with AI-powered prompts",
        "category": "AI Tools", "bg": ((25, 15, 60), (10, 5, 28)),
        "accent": MINT, "icon": "cpu", "file": "ai-business-prompts.png"
    },
    "Airbnb Host Management Dashboard": {
        "title": "Airbnb Host\nDashboard", "subtitle": "Manage listings, bookings & revenue",
        "category": "Business", "bg": ((100, 25, 50), (45, 10, 22)),
        "accent": CORAL, "icon": "calendar", "file": "airbnb-host-dashboard.png"
    },
    "YouTube Channel Growth System": {
        "title": "YouTube\nGrowth System", "subtitle": "Grow your channel with data-driven strategy",
        "category": "Creator Tools", "bg": ((100, 15, 15), (45, 5, 5)),
        "accent": HOT_PINK, "icon": "phone", "file": "youtube-growth-system.png"
    },
    "Pet Business Planner": {
        "title": "Pet Business\nPlanner", "subtitle": "Launch & grow your pet care business",
        "category": "Business", "bg": ((60, 80, 20), (28, 35, 8)),
        "accent": LIME, "icon": "briefcase", "file": "pet-business-planner.png"
    },
    "Remote Team Meeting System": {
        "title": "Remote Team\nMeeting System", "subtitle": "Run productive meetings, every time",
        "category": "Productivity", "bg": ((20, 50, 80), (8, 22, 35)),
        "accent": TEAL, "icon": "calendar", "file": "remote-team-meetings.png"
    },
    "Personal Finance Dashboard": {
        "title": "Personal\nFinance", "subtitle": "Your complete money management system",
        "category": "Finance", "bg": ((15, 60, 50), (5, 28, 22)),
        "accent": NEON_YELLOW, "icon": "piggybank", "file": "personal-finance-dashboard.png"
    },
    "Etsy Seller Toolkit": {
        "title": "Etsy Seller\nToolkit", "subtitle": "Everything you need to crush it on Etsy",
        "category": "Business", "bg": ((100, 50, 15), (45, 22, 5)),
        "accent": BRIGHT_ORANGE, "icon": "dollar", "file": "etsy-seller-toolkit.png"
    },
    "Email Marketing Workflow Kit": {
        "title": "Email Marketing\nWorkflow", "subtitle": "Automated email sequences that convert",
        "category": "Marketing", "bg": ((80, 20, 60), (35, 8, 28)),
        "accent": HOT_PINK, "icon": "invoice", "file": "email-marketing-workflow.png"
    },
    "Fitness Coach Business Planner": {
        "title": "Fitness Coach\nBiz Planner", "subtitle": "Build your fitness coaching empire",
        "category": "Health & Wellness", "bg": ((90, 25, 35), (40, 10, 15)),
        "accent": BRIGHT_ORANGE, "icon": "dumbbell", "file": "fitness-coach-biz-planner.png"
    },
    "Therapist Practice Manager": {
        "title": "Therapist\nPractice Mgr", "subtitle": "Manage clients, notes & scheduling",
        "category": "Health & Wellness", "bg": ((40, 60, 70), (18, 28, 30)),
        "accent": LAVENDER, "icon": "heart", "file": "therapist-practice-manager.png"
    },
    "Real Estate Agent Command Center": {
        "title": "Real Estate\nCommand Center", "subtitle": "Manage listings, leads & closings",
        "category": "Business", "bg": ((30, 35, 70), (12, 15, 30)),
        "accent": BABY_BLUE, "icon": "briefcase", "file": "real-estate-command-center.png"
    },
    "Social Media Content Planner": {
        "title": "Social Media\nPlanner", "subtitle": "Plan, create & schedule like a pro",
        "category": "Marketing", "bg": ((90, 20, 70), (40, 8, 30)),
        "accent": CORAL, "icon": "phone", "file": "social-media-planner.png"
    },
    "Project Manager Pro": {
        "title": "Project\nManager Pro", "subtitle": "Deliver projects on time, every time",
        "category": "Productivity", "bg": ((25, 40, 80), (10, 18, 35)),
        "accent": TEAL, "icon": "calendar", "file": "project-manager-pro.png"
    },
    "Client CRM & Pipeline Tracker": {
        "title": "Client CRM\n& Pipeline", "subtitle": "Track leads, deals & revenue",
        "category": "Business", "bg": ((35, 25, 75), (15, 10, 32)),
        "accent": ELECTRIC_PURPLE, "icon": "briefcase", "file": "client-crm-pipeline.png"
    },
    "Wellness & Habit Tracker": {
        "title": "Wellness &\nHabit Tracker", "subtitle": "Track your wellness journey daily",
        "category": "Health & Wellness", "bg": ((50, 70, 40), (22, 30, 18)),
        "accent": MINT, "icon": "sparkle", "file": "wellness-habit-tracker.png"
    },
    "Content Creator Editorial Calendar": {
        "title": "Editorial\nCalendar", "subtitle": "Plan content that gets engagement",
        "category": "Creator Tools", "bg": ((85, 25, 75), (38, 10, 32)),
        "accent": HOT_PINK, "icon": "calendar", "file": "editorial-calendar.png"
    },
    "Freelance Invoicing & Client Tracker": {
        "title": "Freelance\nInvoicing", "subtitle": "Invoice clients & track payments",
        "category": "Business", "bg": ((30, 35, 65), (12, 15, 28)),
        "accent": TEAL, "icon": "invoice", "file": "freelance-invoicing.png"
    },
    "ADHD Daily Planner & Focus System for Notion": {
        "title": "ADHD Planner\nfor Notion", "subtitle": "Focus system built for neurodivergent minds",
        "category": "Productivity", "bg": ((60, 15, 90), (28, 5, 40)),
        "accent": ELECTRIC_PURPLE, "icon": "sparkle", "file": "adhd-planner-notion.png"
    },
    "Med Spa & Aesthetics Business Launch Blueprint": {
        "title": "Med Spa\nLaunch Guide", "subtitle": "Launch your aesthetics business right",
        "category": "Beauty & Wellness", "bg": ((100, 20, 60), (45, 8, 28)),
        "accent": HOT_PINK, "icon": "sparkle", "file": "med-spa-launch.png"
    },
    "Daily Glow Planner": {
        "title": "Daily Glow\nPlanner", "subtitle": "Your daily glow-up routine, simplified",
        "category": "Beauty", "bg": ((110, 20, 70), (50, 8, 30)),
        "accent": HOT_PINK, "icon": "sparkle", "file": "daily-glow-planner.png"
    },
    "Simple Habit Tracker Bundle": {
        "title": "Simple Habit\nBundle", "subtitle": "Everything you need to build better habits",
        "category": "Productivity", "bg": ((70, 25, 85), (30, 10, 38)),
        "accent": LIME, "icon": "calendar", "file": "simple-habit-bundle.png"
    },
    "Morning Reset Checklist Pack": {
        "title": "Morning Reset\nChecklist", "subtitle": "Start every day with intention",
        "category": "Lifestyle", "bg": ((110, 60, 20), (50, 28, 8)),
        "accent": NEON_YELLOW, "icon": "sparkle", "file": "morning-reset-checklist.png"
    },
    "Productivity Flow Kit": {
        "title": "Productivity\nFlow Kit", "subtitle": "Get into flow state and stay there",
        "category": "Productivity", "bg": ((20, 45, 80), (8, 20, 35)),
        "accent": MINT, "icon": "cpu", "file": "productivity-flow-kit.png"
    },
    "Motivation Affirmation Deck": {
        "title": "Motivation\nAffirmations", "subtitle": "Daily affirmations to keep you going",
        "category": "Lifestyle", "bg": ((100, 30, 70), (45, 12, 30)),
        "accent": LAVENDER, "icon": "heart", "file": "motivation-affirmations.png"
    },
    "Free Morning Glow Checklist": {
        "title": "Morning Glow\nChecklist", "subtitle": "Your free daily glow-up routine",
        "category": "Beauty", "bg": ((110, 25, 65), (50, 10, 28)),
        "accent": CORAL, "icon": "sparkle", "file": "free-morning-glow.png"
    },
    "Therapist Client Management System": {
        "title": "Therapist\nClient System", "subtitle": "Manage your practice with ease",
        "category": "Health & Wellness", "bg": ((45, 55, 75), (20, 25, 32)),
        "accent": LAVENDER, "icon": "heart", "file": "therapist-client-system.png"
    },
    "Real Estate Agent Planner": {
        "title": "Real Estate\nPlanner", "subtitle": "Organize listings, showings & closings",
        "category": "Business", "bg": ((35, 40, 65), (15, 18, 28)),
        "accent": BABY_BLUE, "icon": "briefcase", "file": "real-estate-planner.png"
    },
    "Social Media Content Calendar": {
        "title": "Social Media\nCalendar", "subtitle": "30 days of content, ready to post",
        "category": "Marketing", "bg": ((85, 20, 75), (38, 8, 32)),
        "accent": CORAL, "icon": "phone", "file": "social-media-calendar.png"
    },
    "Personal CRM Template": {
        "title": "Personal CRM\nTemplate", "subtitle": "Never lose a contact or follow-up",
        "category": "Productivity", "bg": ((25, 35, 70), (10, 15, 30)),
        "accent": TEAL, "icon": "briefcase", "file": "personal-crm.png"
    },
    "Job Search Tracker": {
        "title": "Job Search\nTracker", "subtitle": "Track every application & interview",
        "category": "Career", "bg": ((20, 45, 85), (8, 20, 38)),
        "accent": BABY_BLUE, "icon": "briefcase", "file": "job-search-tracker.png"
    },
    "Freelancer Command Center": {
        "title": "Freelancer\nCommand Center", "subtitle": "Run your freelance biz like a boss",
        "category": "Business", "bg": ((30, 30, 70), (12, 12, 30)),
        "accent": ELECTRIC_PURPLE, "icon": "briefcase", "file": "freelancer-command-center.png"
    },
}

# Existing covers that map directly to products
EXISTING_COVER_MAP = {
    "Interview Prep System": "interview-prep-system.png",
    "Resume Builder Kit": "resume-builder.png",
    "Ultimate Side Hustle Launch Kit": "side-hustle.png",
    "Personal Budget Tracker": "budget-planner.png",
    "Content Creator AI Prompt Pack": "content-creator-prompts.png",
    "ADHD Daily Planner & Focus System": "adhd-daily-planner.png",
    "Podcast Launch Kit": "podcast-launch-kit.png",
    "Student Study System": "student-study.png",
    "Meal Prep & Recipe Planner": "meal-prep.png",
    "Midjourney & AI Art Prompt Pack": "midjourney-prompts.png",
    "Side Hustle Income & Expense Tracker": "side-hustle.png",
    "Wedding Planning Dashboard": "wedding-planning.png",
    "Teacher Lesson Planner & Classroom Manager": "teacher-planner.png",
    "Client Proposal Template Kit": "client-proposal.png",
    "Professional Invoice Generator": "invoice-generator.png",
    "Product Launch Playbook": "product-launch.png",
    "Esthetician Client Management System": "esthetician-client-crm.png",
    "AI Productivity Starter Kit (FREE)": "ai-productivity-kit.png",
}


def get_cover_for_product(product_name):
    """Return the cover filename for a product, checking existing and new maps."""
    # Check exact match in existing covers
    if product_name in EXISTING_COVER_MAP:
        return EXISTING_COVER_MAP[product_name]

    # Check in new covers to generate
    if product_name in PRODUCT_COVERS:
        return PRODUCT_COVERS[product_name]["file"]

    # Fuzzy match: check if product name contains a key
    for key, filename in EXISTING_COVER_MAP.items():
        if key.lower() in product_name.lower() or product_name.lower() in key.lower():
            return filename

    for key, cover_def in PRODUCT_COVERS.items():
        if key.lower() in product_name.lower() or product_name.lower() in key.lower():
            return cover_def["file"]

    return None


def generate_missing_covers():
    """Generate covers that don't exist yet."""
    generated = 0
    for name, cover_def in PRODUCT_COVERS.items():
        filepath = os.path.join(OUT_DIR, cover_def["file"])
        if not os.path.exists(filepath):
            print(f"Generating: {cover_def['file']} for '{name}'")
            draw_90s_edgy_cover(
                title=cover_def["title"],
                subtitle=cover_def["subtitle"],
                category=cover_def["category"],
                bg_colors=cover_def["bg"],
                accent=cover_def["accent"],
                icon_type=cover_def["icon"],
                filename=cover_def["file"]
            )
            generated += 1
        else:
            print(f"Exists: {cover_def['file']}")
    return generated


def push_cover_to_gumroad(product_id, cover_url):
    """Push a cover image to a Gumroad product using the covers endpoint."""
    data = urllib.parse.urlencode({
        "access_token": GUMROAD_TOKEN,
        "url": cover_url
    }).encode()

    url = f"https://api.gumroad.com/v2/products/{product_id}/covers"
    req = urllib.request.Request(url, data=data, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            return result.get("success", False)
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  ERROR {e.code}: {body[:200]}")
        return False


def get_all_products():
    """Get all Gumroad products across all pages."""
    all_products = []
    seen_ids = set()
    page_key = None

    while True:
        url = f"https://api.gumroad.com/v2/products?access_token={GUMROAD_TOKEN}"
        if page_key:
            url += f"&page_key={page_key}"

        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())

        products = data.get("products", [])
        new_count = 0
        for p in products:
            if p["id"] not in seen_ids:
                seen_ids.add(p["id"])
                all_products.append(p)
                new_count += 1

        if new_count == 0 or "next_page_key" not in data:
            break
        page_key = data["next_page_key"]

    return all_products


def main():
    print("=" * 60)
    print("STEP 1: Generate missing covers")
    print("=" * 60)
    generated = generate_missing_covers()
    print(f"\nGenerated {generated} new covers\n")

    print("=" * 60)
    print("STEP 2: Get all Gumroad products")
    print("=" * 60)
    products = get_all_products()
    print(f"Found {len(products)} products\n")

    print("=" * 60)
    print("STEP 3: Push covers to Gumroad")
    print("=" * 60)

    pushed = 0
    skipped = 0
    failed = 0
    unmapped = []

    for p in products:
        name = p["name"]
        pid = p["id"]
        cover_file = get_cover_for_product(name)

        if not cover_file:
            unmapped.append(name)
            print(f"  UNMAPPED: {name}")
            continue

        cover_url = f"https://girlgone.ai/covers2/{cover_file}"

        # Check if file exists locally
        local_path = os.path.join(OUT_DIR, cover_file)
        if not os.path.exists(local_path):
            print(f"  MISSING FILE: {cover_file} for {name}")
            failed += 1
            continue

        print(f"  Pushing: {cover_file} -> {name[:40]}...", end=" ")
        success = push_cover_to_gumroad(pid, cover_url)
        if success:
            pushed += 1
            print("OK")
        else:
            failed += 1
            print("FAIL")

    print(f"\n{'=' * 60}")
    print(f"RESULTS: {pushed} pushed, {failed} failed, {len(unmapped)} unmapped")
    if unmapped:
        print(f"\nUnmapped products:")
        for name in unmapped:
            print(f"  - {name}")


if __name__ == "__main__":
    main()
