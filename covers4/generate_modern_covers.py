#!/usr/bin/env python3
"""Generate modern, sleek, clean product covers for Girl Gone AI.

Minimalist design with large bold typography, clean gradients,
subtle geometric accents, and generous whitespace.
"""

import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
OUT_DIR = "/home/boogarweed/girl-gone-ai/covers4"

# Modern muted palette
WHITE = (255, 255, 255)
OFF_WHITE = (248, 248, 252)
LIGHT_GRAY = (230, 232, 238)
MID_GRAY = (160, 165, 180)
DARK = (18, 18, 28)
NEAR_BLACK = (30, 30, 45)

# Accent colors — modern, desaturated
BLUSH = (240, 165, 175)
SOFT_CORAL = (235, 140, 130)
SAGE = (145, 190, 160)
SKY = (140, 185, 235)
LAVENDER = (175, 160, 225)
WARM_GOLD = (225, 195, 120)
SOFT_TEAL = (120, 200, 195)
DUSTY_ROSE = (195, 140, 155)
PEACH = (245, 195, 160)
SLATE_BLUE = (120, 140, 190)
MINT = (160, 220, 195)
MAUVE = (185, 150, 195)


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_gradient_bg(draw, c1, c2):
    for y in range(H):
        t = y / H
        draw.line([(0, y), (W, y)], fill=lerp_color(c1, c2, t))


def draw_soft_circle(draw, cx, cy, radius, color, alpha):
    """Draw a soft gradient circle (glow)."""
    for r in range(radius, 0, -2):
        a = int(alpha * (r / radius) * 0.6)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))


def draw_thin_ring(draw, cx, cy, radius, color, alpha=60, width=1):
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 outline=(*color, alpha), width=width)


def draw_accent_line(draw, x1, y1, x2, y2, color, alpha=80, width=2):
    draw.line([(x1, y1), (x2, y2)], fill=(*color, alpha), width=width)


def draw_dot_grid(draw, area, color, spacing=40, radius=2, alpha=30):
    """Subtle dot grid pattern."""
    x0, y0, x1, y1 = area
    for y in range(y0, y1, spacing):
        for x in range(x0, x1, spacing):
            draw.ellipse([x - radius, y - radius, x + radius, y + radius],
                         fill=(*color, alpha))


def draw_minimal_icon(draw, cx, cy, icon_type, color, size=90):
    """Draw clean minimal line icons."""
    s = size / 90

    if icon_type == "mic":
        draw.rounded_rectangle([cx - int(14 * s), cy - int(32 * s), cx + int(14 * s), cy + int(8 * s)],
                               radius=int(14 * s), outline=color, width=int(3 * s))
        draw.line([(cx, cy + int(8 * s)), (cx, cy + int(28 * s))], fill=color, width=int(3 * s))
        draw.arc([cx - int(22 * s), cy - int(2 * s), cx + int(22 * s), cy + int(18 * s)],
                 start=0, end=180, fill=color, width=int(2 * s))

    elif icon_type == "dollar":
        draw.ellipse([cx - int(32 * s), cy - int(32 * s), cx + int(32 * s), cy + int(32 * s)],
                     outline=color, width=int(3 * s))
        font = ImageFont.truetype(FONT_BOLD, int(42 * s))
        bb = font.getbbox("$")
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        draw.text((cx - tw // 2, cy - th // 2 - int(4 * s)), "$", fill=color, font=font)

    elif icon_type == "fork_knife":
        draw.line([(cx - int(12 * s), cy - int(30 * s)), (cx - int(12 * s), cy + int(30 * s))],
                  fill=color, width=int(3 * s))
        draw.line([(cx + int(12 * s), cy - int(10 * s)), (cx + int(12 * s), cy + int(30 * s))],
                  fill=color, width=int(3 * s))
        draw.arc([cx + int(2 * s), cy - int(30 * s), cx + int(22 * s), cy - int(10 * s)],
                 start=180, end=360, fill=color, width=int(3 * s))

    elif icon_type == "palette":
        draw.arc([cx - int(28 * s), cy - int(28 * s), cx + int(28 * s), cy + int(28 * s)],
                 start=20, end=340, fill=color, width=int(3 * s))
        for i, angle in enumerate([70, 150, 230, 310]):
            r = int(6 * s)
            dx = int(16 * s) * math.cos(math.radians(angle))
            dy = int(16 * s) * math.sin(math.radians(angle))
            draw.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=color)

    elif icon_type == "book":
        draw.arc([cx - int(28 * s), cy - int(8 * s), cx, cy + int(18 * s)],
                 start=180, end=360, fill=color, width=int(2 * s))
        draw.arc([cx, cy - int(8 * s), cx + int(28 * s), cy + int(18 * s)],
                 start=180, end=360, fill=color, width=int(2 * s))
        draw.line([(cx, cy - int(28 * s)), (cx, cy + int(18 * s))], fill=color, width=int(2 * s))

    elif icon_type == "heart":
        pts = []
        for t_val in range(0, 360, 3):
            rad = math.radians(t_val)
            x = 16 * (math.sin(rad) ** 3)
            y = -(13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
            pts.append((cx + int(x * 1.8 * s), cy + int(y * 1.8 * s) - int(4 * s)))
        for i in range(len(pts) - 1):
            draw.line([pts[i], pts[i + 1]], fill=color, width=int(3 * s))

    elif icon_type == "invoice":
        draw.rounded_rectangle([cx - int(20 * s), cy - int(28 * s), cx + int(20 * s), cy + int(28 * s)],
                               radius=int(4 * s), outline=color, width=int(2 * s))
        for i in range(4):
            ly = cy - int(16 * s) + i * int(11 * s)
            lw = int(26 * s) if i < 3 else int(16 * s)
            draw.line([(cx - int(12 * s), ly), (cx - int(12 * s) + lw, ly)], fill=color, width=int(2 * s))

    elif icon_type == "rocket":
        draw.polygon([
            (cx, cy - int(32 * s)),
            (cx - int(12 * s), cy + int(10 * s)),
            (cx + int(12 * s), cy + int(10 * s))
        ], outline=color, width=int(2 * s))
        draw.ellipse([cx - int(5 * s), cy - int(8 * s), cx + int(5 * s), cy + int(2 * s)],
                     outline=color, width=int(2 * s))

    elif icon_type == "briefcase":
        draw.rounded_rectangle([cx - int(26 * s), cy - int(16 * s), cx + int(26 * s), cy + int(16 * s)],
                               radius=int(4 * s), outline=color, width=int(2 * s))
        draw.arc([cx - int(10 * s), cy - int(26 * s), cx + int(10 * s), cy - int(12 * s)],
                 start=180, end=360, fill=color, width=int(2 * s))

    elif icon_type == "calendar":
        draw.rounded_rectangle([cx - int(24 * s), cy - int(24 * s), cx + int(24 * s), cy + int(24 * s)],
                               radius=int(4 * s), outline=color, width=int(2 * s))
        draw.line([(cx - int(24 * s), cy - int(12 * s)), (cx + int(24 * s), cy - int(12 * s))],
                  fill=color, width=int(2 * s))

    elif icon_type == "phone":
        draw.rounded_rectangle([cx - int(14 * s), cy - int(26 * s), cx + int(14 * s), cy + int(26 * s)],
                               radius=int(6 * s), outline=color, width=int(2 * s))

    elif icon_type == "cpu":
        draw.rounded_rectangle([cx - int(20 * s), cy - int(20 * s), cx + int(20 * s), cy + int(20 * s)],
                               radius=int(4 * s), outline=color, width=int(2 * s))
        for pos in [-int(12 * s), 0, int(12 * s)]:
            draw.line([(cx + pos, cy - int(20 * s)), (cx + pos, cy - int(28 * s))], fill=color, width=int(2 * s))
            draw.line([(cx + pos, cy + int(20 * s)), (cx + pos, cy + int(28 * s))], fill=color, width=int(2 * s))

    elif icon_type == "piggybank":
        draw.ellipse([cx - int(26 * s), cy - int(18 * s), cx + int(18 * s), cy + int(14 * s)],
                     outline=color, width=int(2 * s))
        draw.line([(cx - int(18 * s), cy + int(14 * s)), (cx - int(18 * s), cy + int(22 * s))],
                  fill=color, width=int(2 * s))
        draw.line([(cx + int(8 * s), cy + int(14 * s)), (cx + int(8 * s), cy + int(22 * s))],
                  fill=color, width=int(2 * s))

    elif icon_type == "dumbbell":
        draw.line([(cx - int(28 * s), cy), (cx + int(28 * s), cy)], fill=color, width=int(3 * s))
        for side in [-1, 1]:
            wx = cx + side * int(28 * s)
            draw.rounded_rectangle([wx - int(7 * s), cy - int(14 * s), wx + int(7 * s), cy + int(14 * s)],
                                   radius=int(3 * s), outline=color, width=int(2 * s))

    elif icon_type == "resume":
        draw.rounded_rectangle([cx - int(20 * s), cy - int(28 * s), cx + int(20 * s), cy + int(28 * s)],
                               radius=int(4 * s), outline=color, width=int(2 * s))
        for i in range(3):
            ly = cy - int(14 * s) + i * int(12 * s)
            draw.line([(cx - int(12 * s), ly), (cx + int(12 * s), ly)], fill=color, width=int(2 * s))


def draw_modern_cover(title, subtitle, category, bg_colors, accent, icon_type, filename):
    """Generate a single modern, sleek cover with large bold typography."""
    bg1, bg2 = bg_colors
    img = Image.new("RGBA", (W, H), DARK)
    draw = ImageDraw.Draw(img)

    # Clean gradient background
    draw_gradient_bg(draw, bg1, bg2)

    seed = hash(title)
    random.seed(seed)

    # Subtle dot grid in background
    draw_dot_grid(draw, (40, 40, W - 40, H - 40), accent, spacing=50, radius=1, alpha=20)

    # Large soft glow circle (background element)
    glow_x = random.randint(W // 2 - 100, W // 2 + 200)
    glow_y = random.randint(H // 2 - 100, H // 2 + 50)
    draw_soft_circle(draw, glow_x, glow_y, 280, accent, 25)

    # Second smaller glow
    draw_soft_circle(draw, 120, H - 150, 180, bg1, 20)

    # Subtle thin rings
    draw_thin_ring(draw, glow_x + 60, glow_y - 40, 160, accent, alpha=25, width=1)
    draw_thin_ring(draw, 100, 100, 200, accent, alpha=15, width=1)

    # === CLEAN BORDER ===
    m = 32
    # Single thin border with rounded corners
    draw.rounded_rectangle([m, m, W - m, H - m], radius=16, outline=(*accent, 60), width=2)

    # Thin accent line at top
    draw.line([(m + 20, m + 52), (W - m - 20, m + 52)], fill=(*accent, 40), width=1)

    # === TOP BAR — category + brand ===
    cat_font = ImageFont.truetype(FONT_BOLD, 13)
    draw.text((m + 28, m + 16), category.upper(), fill=(*accent, 220), font=cat_font)

    # Spacing dots
    cat_bb = cat_font.getbbox(category.upper())
    dot_start = m + 28 + (cat_bb[2] - cat_bb[0]) + 16
    for i in range(3):
        draw.ellipse([dot_start + i * 10, m + 24, dot_start + i * 10 + 4, m + 28],
                     fill=(*accent, 80))

    brand_font = ImageFont.truetype(FONT_BOLD, 12)
    brand_text = "GIRL GONE AI"
    bb = brand_font.getbbox(brand_text)
    draw.text((W - m - 28 - (bb[2] - bb[0]), m + 18), brand_text,
              fill=(*WHITE, 160), font=brand_font)

    # === ICON (left side, clean) ===
    icon_cx = 170
    icon_cy = H // 2 + 20

    # Soft circular backdrop
    draw_soft_circle(draw, icon_cx, icon_cy, 80, accent, 30)

    # Clean ring
    draw.ellipse([icon_cx - 52, icon_cy - 52, icon_cx + 52, icon_cy + 52],
                 outline=(*accent, 100), width=2)

    draw_minimal_icon(draw, icon_cx, icon_cy, icon_type, WHITE, size=90)

    # === LARGE TITLE (right side, BIG fonts) ===
    title_x = 300
    title_y = 100
    # BIGGER font — 72pt for main title
    title_font = ImageFont.truetype(FONT_BOLD, 72)
    title_lines = title.split("\n")
    line_h = 84

    # Subtle text panel background
    panel_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel_bg)
    total_h = line_h * len(title_lines) + 130
    pd.rounded_rectangle([title_x - 24, title_y - 20, W - m - 16, title_y + total_h],
                         radius=12, fill=(0, 0, 0, 60))
    img = Image.alpha_composite(img, panel_bg)
    draw = ImageDraw.Draw(img)

    # Thin vertical accent bar
    bar_top = title_y - 10
    bar_bottom = title_y + line_h * len(title_lines) + 5
    draw.rounded_rectangle([title_x - 20, bar_top, title_x - 14, bar_bottom],
                           radius=3, fill=accent)

    # Title text with subtle shadow
    for li, line in enumerate(title_lines):
        ly = title_y + li * line_h
        # Soft shadow
        draw.text((title_x + 2, ly + 2), line, fill=(0, 0, 0, 100), font=title_font)
        draw.text((title_x, ly), line, fill=WHITE, font=title_font)

    # Subtitle — clean, lighter weight
    sub_y = title_y + len(title_lines) * line_h + 12
    sub_font = ImageFont.truetype(FONT_REG, 22)
    draw.text((title_x, sub_y), subtitle, fill=(*accent, 240), font=sub_font)

    # Feature bullets — minimal dots
    bullet_font = ImageFont.truetype(FONT_REG, 15)
    features = get_features(title)
    bullet_y = sub_y + 38
    for feat in features[:3]:
        draw.ellipse([title_x + 2, bullet_y + 5, title_x + 8, bullet_y + 11],
                     fill=(*accent, 180))
        draw.text((title_x + 16, bullet_y), feat, fill=(*WHITE, 180), font=bullet_font)
        bullet_y += 24

    # === BOTTOM BAR — minimal ===
    bottom_y = H - m - 44
    # Thin separator line
    draw.line([(m + 20, bottom_y - 4), (W - m - 20, bottom_y - 4)],
              fill=(*accent, 30), width=1)

    ed_font = ImageFont.truetype(FONT_BOLD, 11)
    draw.text((m + 28, bottom_y + 8), "MODERN EDITION", fill=(*WHITE, 100), font=ed_font)

    # Badge right side
    badge_text = get_badge_label(title)
    badge_font = ImageFont.truetype(FONT_BOLD, 12)
    bb_bbox = badge_font.getbbox(badge_text)
    bw = bb_bbox[2] - bb_bbox[0]
    badge_x = W - m - 28 - bw
    draw.rounded_rectangle([badge_x - 12, bottom_y + 2, badge_x + bw + 12, bottom_y + 28],
                           radius=14, fill=(*accent, 200))
    draw.text((badge_x, bottom_y + 6), badge_text, fill=DARK, font=badge_font)

    # === SAVE ===
    final = img.convert("RGB")
    final.save(f"{OUT_DIR}/{filename}", quality=95)
    print(f"  Saved {filename}")


def get_features(title):
    features_map = {
        "Podcast\nLaunch Kit": ["30-day launch roadmap", "Episode templates & scripts", "Growth strategy playbook"],
        "Side Hustle\nIncome Tracker": ["Revenue & expense dashboards", "Goal tracking & milestones", "Tax-ready export reports"],
        "Meal Prep\nPlanner": ["Weekly meal templates", "Smart grocery lists", "Nutrition tracking built-in"],
        "Midjourney\nPrompt Pack": ["500+ curated prompts", "Style & mood categories", "Commercial-use ready"],
        "Student Study\nPlanner": ["Assignment tracker", "Exam countdown timers", "GPA calculator included"],
        "Teacher\nPlanner": ["Lesson plan templates", "Grade book system", "Parent comm templates"],
        "Wedding\nPlanner": ["Timeline & checklist", "Budget tracker included", "Vendor management"],
        "Invoice\nGenerator": ["Professional templates", "Auto-calculations", "PDF export ready"],
        "Product Launch\nPlaybook": ["Pre-launch checklist", "Marketing timeline", "KPI tracking dashboard"],
        "Client Proposal\nTemplate": ["Customizable layouts", "Pricing tables", "E-sign ready format"],
        "Content\nCalendar": ["30-day content plans", "Platform-specific templates", "Analytics tracker"],
        "Social Media\nBundle": ["200+ post templates", "Story & reel formats", "Hashtag strategy guide"],
        "AI Productivity\nStarter Kit": ["Prompt library", "Workflow automations", "Tool comparison guide"],
        "Budget\nPlanner": ["Income & expense tracking", "Savings goals", "Debt payoff calculator"],
        "Fitness\nTracker": ["Workout templates", "Progress photos log", "Macro tracking"],
        "Resume\nBuilder": ["ATS-optimized layouts", "Cover letter templates", "Interview prep guide"],
    }
    for key, feats in features_map.items():
        if key.replace("\n", " ").lower() in title.replace("\n", " ").lower():
            return feats
    return ["Premium digital template", "Instant download", "Fully customizable"]


def get_badge_label(title):
    labels = {
        "Podcast": "CREATOR",
        "Side Hustle": "FINANCE",
        "Meal Prep": "LIFESTYLE",
        "Midjourney": "AI TOOLS",
        "Student": "EDUCATION",
        "Teacher": "EDUCATION",
        "Wedding": "PLANNING",
        "Invoice": "BUSINESS",
        "Product Launch": "STRATEGY",
        "Client": "BUSINESS",
        "Content": "SOCIAL",
        "Social Media": "MARKETING",
        "AI Productivity": "AI TOOLS",
        "Budget": "FINANCE",
        "Fitness": "WELLNESS",
        "Resume": "CAREER",
    }
    for key, label in labels.items():
        if key.lower() in title.replace("\n", " ").lower():
            return label
    return "PREMIUM"


# Modern color schemes: (bg_top, bg_bottom), accent
covers = [
    {
        "title": "Podcast\nLaunch Kit",
        "subtitle": "Your complete 30-day podcast launch system",
        "category": "Creator Tools",
        "bg": ((35, 25, 55), (18, 14, 32)),
        "accent": LAVENDER,
        "icon": "mic",
        "file": "podcast-launch-kit.png"
    },
    {
        "title": "Side Hustle\nIncome Tracker",
        "subtitle": "Track every dollar from side gig to empire",
        "category": "Finance",
        "bg": ((22, 42, 35), (12, 24, 20)),
        "accent": SAGE,
        "icon": "dollar",
        "file": "side-hustle.png"
    },
    {
        "title": "Meal Prep\nPlanner",
        "subtitle": "Eat smart, save time, crush your goals",
        "category": "Lifestyle",
        "bg": ((48, 28, 32), (26, 16, 20)),
        "accent": SOFT_CORAL,
        "icon": "fork_knife",
        "file": "meal-prep.png"
    },
    {
        "title": "Midjourney\nPrompt Pack",
        "subtitle": "500+ prompts to create stunning AI art",
        "category": "AI Tools",
        "bg": ((32, 22, 52), (18, 12, 30)),
        "accent": MAUVE,
        "icon": "palette",
        "file": "midjourney-prompts.png"
    },
    {
        "title": "Student Study\nPlanner",
        "subtitle": "Ace every class with the ultimate study system",
        "category": "Education",
        "bg": ((22, 32, 52), (12, 18, 30)),
        "accent": SKY,
        "icon": "book",
        "file": "student-study.png"
    },
    {
        "title": "Teacher\nPlanner",
        "subtitle": "Plan, grade, and communicate like a pro",
        "category": "Education",
        "bg": ((22, 40, 38), (12, 22, 22)),
        "accent": SOFT_TEAL,
        "icon": "book",
        "file": "teacher-planner.png"
    },
    {
        "title": "Wedding\nPlanner",
        "subtitle": "Plan your dream day without the stress",
        "category": "Life Events",
        "bg": ((48, 28, 38), (28, 16, 22)),
        "accent": BLUSH,
        "icon": "heart",
        "file": "wedding-planning.png"
    },
    {
        "title": "Invoice\nGenerator",
        "subtitle": "Professional invoices in seconds",
        "category": "Business",
        "bg": ((28, 28, 42), (16, 16, 26)),
        "accent": SLATE_BLUE,
        "icon": "invoice",
        "file": "invoice-generator.png"
    },
    {
        "title": "Product Launch\nPlaybook",
        "subtitle": "Launch with confidence, scale with data",
        "category": "Business",
        "bg": ((45, 25, 25), (25, 14, 14)),
        "accent": PEACH,
        "icon": "rocket",
        "file": "product-launch.png"
    },
    {
        "title": "Client Proposal\nTemplate",
        "subtitle": "Win clients with polished proposals",
        "category": "Business",
        "bg": ((30, 28, 45), (16, 14, 26)),
        "accent": LAVENDER,
        "icon": "briefcase",
        "file": "client-proposal.png"
    },
    {
        "title": "Content\nCalendar",
        "subtitle": "30 days of content, planned and ready to post",
        "category": "Social Media",
        "bg": ((42, 24, 38), (24, 14, 22)),
        "accent": DUSTY_ROSE,
        "icon": "calendar",
        "file": "content-calendar.png"
    },
    {
        "title": "Social Media\nBundle",
        "subtitle": "200+ templates for every platform",
        "category": "Marketing",
        "bg": ((38, 22, 42), (22, 12, 24)),
        "accent": BLUSH,
        "icon": "phone",
        "file": "social-media-bundle.png"
    },
    {
        "title": "AI Productivity\nStarter Kit",
        "subtitle": "Work smarter with AI-powered workflows",
        "category": "AI Tools",
        "bg": ((18, 28, 42), (10, 16, 26)),
        "accent": MINT,
        "icon": "cpu",
        "file": "ai-productivity-kit.png"
    },
    {
        "title": "Budget\nPlanner",
        "subtitle": "Take control of your money, one week at a time",
        "category": "Finance",
        "bg": ((28, 38, 30), (16, 22, 18)),
        "accent": WARM_GOLD,
        "icon": "piggybank",
        "file": "budget-planner.png"
    },
    {
        "title": "Fitness\nTracker",
        "subtitle": "Crush your fitness goals with daily tracking",
        "category": "Health & Wellness",
        "bg": ((42, 24, 28), (24, 14, 16)),
        "accent": SOFT_CORAL,
        "icon": "dumbbell",
        "file": "fitness-tracker.png"
    },
    {
        "title": "Resume\nBuilder",
        "subtitle": "Land your dream job with a standout resume",
        "category": "Career",
        "bg": ((24, 28, 42), (14, 16, 26)),
        "accent": SKY,
        "icon": "resume",
        "file": "resume-builder.png"
    },
]


if __name__ == "__main__":
    print(f"Generating {len(covers)} modern sleek covers...")
    for c in covers:
        draw_modern_cover(
            title=c["title"],
            subtitle=c["subtitle"],
            category=c["category"],
            bg_colors=c["bg"],
            accent=c["accent"],
            icon_type=c["icon"],
            filename=c["file"]
        )
    print(f"\nDone! {len(covers)} covers generated in {OUT_DIR}/")
