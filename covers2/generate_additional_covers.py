#!/usr/bin/env python3
"""Generate additional 90s-vibe edgy covers for new Gumroad products.

Uses the same style as generate_edgy_90s.py (JC-353 approved design):
Bold geometric shapes, halftone patterns, Memphis-style elements,
grunge textures, and strong typography. No cartoon characters.
"""

import math
import random
import sys
import os

# Add parent dir so we can import from the existing script
sys.path.insert(0, os.path.dirname(__file__))
from generate_edgy_90s import (
    draw_90s_edgy_cover, get_features, get_power_label,
    HOT_PINK, TEAL, ELECTRIC_PURPLE, LIME, NEON_YELLOW,
    BRIGHT_ORANGE, CORAL, LAVENDER, BABY_BLUE, MINT, WHITE, BLACK,
    DARK_BG, CHARCOAL, W, H, OUT_DIR
)

# Extend features map for new products
_orig_get_features = get_features
def patched_get_features(title):
    extra = {
        "ADHD Daily\nPlanner": ["Focus session timer", "Task prioritization matrix", "Dopamine-friendly design"],
        "Esthetician\nClient CRM": ["Client history tracking", "Treatment protocols", "Rebooking automation"],
        "Lash Tech\nBusiness Planner": ["Appointment scheduling", "Supply inventory tracker", "Revenue goal setting"],
        "Interview Prep\nSystem": ["300+ practice questions", "STAR method templates", "Company research tracker"],
        "Content Creator\nPrompt Pack": ["500+ viral prompts", "Platform-specific hooks", "Content calendar included"],
        "Glow-Up\nTracker": ["90-day transformation plan", "Skincare routine builder", "Progress photo log"],
        "Notion\nLife OS": ["All-in-one dashboard", "Goal & habit tracking", "Weekly review templates"],
        "Gratitude\nJournal": ["Daily reflection prompts", "Mindfulness exercises", "Mood tracking system"],
        "Course Creator\nLaunch Kit": ["Course outline templates", "Launch timeline planner", "Student engagement tools"],
        "Pitch Deck\nBuilder": ["Investor-ready slides", "Financial model templates", "Pitch script guide"],
    }
    for key, feats in extra.items():
        if key.replace("\n", " ").lower() in title.replace("\n", " ").lower():
            return feats
    return _orig_get_features(title)

# Monkey-patch
import generate_edgy_90s
generate_edgy_90s.get_features = patched_get_features

# Also patch power labels
_orig_get_power_label = get_power_label
def patched_get_power_label(title):
    extra = {
        "ADHD": "FOCUS MODE",
        "Esthetician": "BOSS BABE",
        "Lash Tech": "GLAM SQUAD",
        "Interview": "HIRED!",
        "Content Creator": "VIRAL VIBES",
        "Glow-Up": "GLOW UP",
        "Notion": "ALL THAT",
        "Gratitude": "INNER PEACE",
        "Course Creator": "TEACH IT",
        "Pitch Deck": "MONEY TALK",
    }
    for key, label in extra.items():
        if key.lower() in title.replace("\n", " ").lower():
            return label
    return _orig_get_power_label(title)

generate_edgy_90s.get_power_label = patched_get_power_label

# ── NEW COVER DEFINITIONS ──
# These are the additional products queued/added beyond the original 16

ROSE_PINK = (255, 105, 180)
DEEP_TEAL = (0, 180, 180)
GOLD = (255, 215, 0)
PEACH = (255, 180, 128)
SAGE = (120, 200, 160)

new_covers = [
    {
        "title": "ADHD Daily\nPlanner",
        "subtitle": "Stay focused, crush tasks, own your day",
        "category": "Productivity",
        "bg": ((90, 25, 110), (35, 10, 50)),
        "accent": NEON_YELLOW,
        "icon": "sparkle",
        "file": "adhd-daily-planner.png"
    },
    {
        "title": "Esthetician\nClient CRM",
        "subtitle": "Manage clients, treatments, and rebookings",
        "category": "Beauty Business",
        "bg": ((110, 20, 70), (45, 8, 30)),
        "accent": ROSE_PINK,
        "icon": "heart",
        "file": "esthetician-client-crm.png"
    },
    {
        "title": "Lash Tech\nBusiness Planner",
        "subtitle": "Build your lash empire from day one",
        "category": "Beauty Business",
        "bg": ((80, 15, 90), (30, 5, 40)),
        "accent": LAVENDER,
        "icon": "sparkle",
        "file": "lash-tech-business-planner.png"
    },
    {
        "title": "Interview Prep\nSystem",
        "subtitle": "Walk in confident, walk out hired",
        "category": "Career",
        "bg": ((25, 40, 90), (10, 18, 40)),
        "accent": BABY_BLUE,
        "icon": "briefcase",
        "file": "interview-prep-system.png"
    },
    {
        "title": "Content Creator\nPrompt Pack",
        "subtitle": "Never run out of content ideas again",
        "category": "Creator Tools",
        "bg": ((100, 15, 60), (40, 5, 25)),
        "accent": CORAL,
        "icon": "phone",
        "file": "content-creator-prompts.png"
    },
    {
        "title": "Glow-Up\nTracker",
        "subtitle": "Track your 90-day transformation journey",
        "category": "Beauty & Wellness",
        "bg": ((120, 20, 90), (50, 8, 38)),
        "accent": HOT_PINK,
        "icon": "sparkle",
        "file": "glow-up-tracker.png"
    },
    {
        "title": "Notion\nLife OS",
        "subtitle": "Your entire life, organized in one dashboard",
        "category": "Productivity",
        "bg": ((20, 20, 60), (40, 15, 70)),
        "accent": MINT,
        "icon": "cpu",
        "file": "notion-life-os.png"
    },
    {
        "title": "Gratitude\nJournal",
        "subtitle": "Daily mindfulness for a more grateful life",
        "category": "Wellness",
        "bg": ((60, 25, 80), (25, 10, 35)),
        "accent": SAGE,
        "icon": "heart",
        "file": "gratitude-journal.png"
    },
    {
        "title": "Course Creator\nLaunch Kit",
        "subtitle": "Plan, build, and launch your online course",
        "category": "Business",
        "bg": ((85, 20, 35), (35, 8, 15)),
        "accent": BRIGHT_ORANGE,
        "icon": "rocket",
        "file": "course-creator-launch-kit.png"
    },
    {
        "title": "Pitch Deck\nBuilder",
        "subtitle": "Win investors with a killer pitch deck",
        "category": "Business",
        "bg": ((30, 35, 80), (12, 15, 35)),
        "accent": GOLD,
        "icon": "briefcase",
        "file": "pitch-deck-builder.png"
    },
]

if __name__ == "__main__":
    print(f"Generating {len(new_covers)} additional 90s-vibe covers...")
    for c in new_covers:
        draw_90s_edgy_cover(
            title=c["title"],
            subtitle=c["subtitle"],
            category=c["category"],
            bg_colors=c["bg"],
            accent=c["accent"],
            icon_type=c["icon"],
            filename=c["file"]
        )
    print(f"\nDone! {len(new_covers)} new covers generated in {OUT_DIR}/")
