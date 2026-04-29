#!/usr/bin/env python3
"""Generate Pokemon-card-style product covers for Girl Gone AI."""

import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1280, 720
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Brand palette
PINK = (255, 59, 139)
PURPLE = (139, 92, 246)
BLUE = (59, 130, 246)
DARK = (15, 15, 30)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_gradient(draw, bbox, c1, c2, direction="vertical"):
    x0, y0, x1, y1 = bbox
    if direction == "vertical":
        for y in range(y0, y1):
            t = (y - y0) / max(1, y1 - y0)
            draw.line([(x0, y), (x1, y)], fill=lerp_color(c1, c2, t))
    else:
        for x in range(x0, x1):
            t = (x - x0) / max(1, x1 - x0)
            draw.line([(x, y0), (x, y1)], fill=lerp_color(c1, c2, t))


def draw_star(draw, cx, cy, r, color, points=5):
    coords = []
    for i in range(points * 2):
        angle = math.pi / 2 + i * math.pi / points
        rad = r if i % 2 == 0 else r * 0.4
        coords.append((cx + rad * math.cos(angle), cy - rad * math.sin(angle)))
    draw.polygon(coords, fill=color)


def draw_sparkle(draw, cx, cy, size, color):
    draw.line([(cx - size, cy), (cx + size, cy)], fill=color, width=2)
    draw.line([(cx, cy - size), (cx, cy + size)], fill=color, width=2)
    s2 = size * 0.6
    draw.line([(cx - s2, cy - s2), (cx + s2, cy + s2)], fill=color, width=1)
    draw.line([(cx - s2, cy + s2), (cx + s2, cy - s2)], fill=color, width=1)


def draw_diamond(draw, cx, cy, w, h, color):
    draw.polygon([(cx, cy - h), (cx + w, cy), (cx, cy + h), (cx - w, cy)], fill=color)


def draw_energy_circles(draw, cx, cy, r, color, alpha=80):
    for i in range(3):
        ri = r + i * 8
        c = (*color, max(10, alpha - i * 25))
        draw.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], outline=c, width=2)


def draw_lightning(draw, x, y, length, color, width=3):
    pts = [(x, y)]
    cx, cy = x, y
    seg = length // 5
    for i in range(5):
        cx += random.randint(-15, 15)
        cy += seg
        pts.append((cx, cy))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=color, width=width)


def draw_hex_pattern(draw, x0, y0, x1, y1, size, color):
    """Draw a subtle hexagonal grid pattern."""
    h = size * math.sqrt(3)
    row = 0
    y = y0
    while y < y1:
        offset = (size * 1.5) if row % 2 else 0
        x = x0 + offset
        while x < x1:
            pts = []
            for i in range(6):
                angle = math.pi / 3 * i + math.pi / 6
                pts.append((x + size * 0.8 * math.cos(angle), y + size * 0.8 * math.sin(angle)))
            draw.polygon(pts, outline=(*color, 30), fill=None)
            x += size * 3
        y += h
        row += 1


def draw_card_border(draw, margin, border_color, accent_color):
    """Draw a double-border card frame like a Pokemon/trading card."""
    # Outer border
    draw.rounded_rectangle(
        [margin, margin, W - margin, H - margin],
        radius=20, outline=border_color, width=4
    )
    # Inner border
    inner = margin + 8
    draw.rounded_rectangle(
        [inner, inner, W - inner, H - inner],
        radius=16, outline=accent_color, width=2
    )
    # Corner diamonds
    for cx, cy in [(margin + 20, margin + 20), (W - margin - 20, margin + 20),
                   (margin + 20, H - margin - 20), (W - margin - 20, H - margin - 20)]:
        draw_diamond(draw, cx, cy, 8, 6, accent_color)


def draw_badge(draw, x, y, text, bg_color, text_color=WHITE):
    font = ImageFont.truetype(FONT_BOLD, 16)
    bbox = font.getbbox(text)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad = 10
    draw.rounded_rectangle(
        [x, y, x + tw + pad * 2, y + th + pad * 2 - 4],
        radius=8, fill=bg_color
    )
    draw.text((x + pad, y + pad - 4), text, fill=text_color, font=font)


def draw_holographic_stripe(img, y_start, height, alpha=40):
    """Draw a rainbow holographic stripe effect."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    colors = [(255, 0, 100), (255, 100, 0), (255, 255, 0), (0, 255, 100), (0, 100, 255), (100, 0, 255)]
    stripe_w = W // len(colors)
    for i, c in enumerate(colors):
        d.rectangle([i * stripe_w, y_start, (i + 1) * stripe_w, y_start + height],
                     fill=(*c, alpha))
    img.paste(Image.alpha_composite(Image.new("RGBA", img.size, (0, 0, 0, 0)), overlay), (0, 0), overlay)


def draw_scattered_elements(draw, count, area, element_type="star"):
    """Scatter decorative elements in an area."""
    x0, y0, x1, y1 = area
    random.seed(42)
    for _ in range(count):
        cx = random.randint(x0, x1)
        cy = random.randint(y0, y1)
        size = random.randint(4, 12)
        alpha = random.randint(60, 180)
        color = random.choice([
            (*PINK, alpha), (*GOLD, alpha), (*WHITE, alpha), (*PURPLE, alpha)
        ])
        rgb = color[:3]
        if element_type == "star":
            draw_star(draw, cx, cy, size, rgb)
        elif element_type == "sparkle":
            draw_sparkle(draw, cx, cy, size, rgb)
        elif element_type == "diamond":
            draw_diamond(draw, cx, cy, size, size, rgb)


def generate_cover(title, subtitle, icon_emoji, category, color_scheme, style, filename):
    """Generate a single Pokemon-card-style cover."""
    c1, c2, c3 = color_scheme  # gradient start, gradient end, accent
    img = Image.new("RGBA", (W, H), DARK)
    draw = ImageDraw.Draw(img)

    # Background gradient
    draw_gradient(draw, (0, 0, W, H), c1, c2)

    if style == "holographic":
        # Holographic diagonal lines
        for i in range(-H, W + H, 6):
            alpha = 15 + (i % 30)
            draw.line([(i, 0), (i - H, H)], fill=(*WHITE, min(alpha, 40)), width=1)
        # Hex pattern overlay
        draw_hex_pattern(draw, 0, 0, W, H, 30, WHITE)

    elif style == "energy":
        # Energy burst lines from center
        cx, cy = W // 2, H // 2
        for angle_deg in range(0, 360, 8):
            angle = math.radians(angle_deg)
            length = max(W, H)
            ex = cx + length * math.cos(angle)
            ey = cy + length * math.sin(angle)
            draw.line([(cx, cy), (ex, ey)], fill=(*c3, 20), width=2)

    elif style == "circuit":
        # Circuit board pattern
        random.seed(hash(title))
        for _ in range(40):
            x = random.randint(0, W)
            y = random.randint(0, H)
            length = random.randint(40, 200)
            if random.random() > 0.5:
                draw.line([(x, y), (x + length, y)], fill=(*c3, 35), width=2)
                draw.ellipse([x + length - 4, y - 4, x + length + 4, y + 4], fill=(*c3, 50))
            else:
                draw.line([(x, y), (x, y + length)], fill=(*c3, 35), width=2)
                draw.ellipse([x - 4, y + length - 4, x + 4, y + length + 4], fill=(*c3, 50))

    elif style == "cosmic":
        # Scattered star field
        random.seed(hash(title) + 1)
        for _ in range(80):
            sx = random.randint(0, W)
            sy = random.randint(0, H)
            sr = random.randint(1, 3)
            sa = random.randint(80, 255)
            draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(*WHITE, sa))

    elif style == "wave":
        # Wave pattern
        for wave_y in range(0, H, 4):
            offset = math.sin(wave_y / 30) * 40
            for x in range(0, W, 3):
                y = wave_y + math.sin((x + offset) / 50) * 15
                draw.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(*c3, 20))

    # === CARD FRAME ===
    margin = 24
    # Main card body (semi-transparent dark)
    card_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    card_draw = ImageDraw.Draw(card_bg)
    card_draw.rounded_rectangle(
        [margin + 12, margin + 12, W - margin - 12, H - margin - 12],
        radius=16, fill=(10, 10, 25, 180)
    )
    img = Image.alpha_composite(img, card_bg)
    draw = ImageDraw.Draw(img)

    # Outer gold/accent border
    draw.rounded_rectangle(
        [margin, margin, W - margin, H - margin],
        radius=20, outline=c3, width=4
    )
    # Inner border
    draw.rounded_rectangle(
        [margin + 8, margin + 8, W - margin - 8, H - margin - 8],
        radius=16, outline=(*c3[:3], 120) if len(c3) == 4 else c3, width=2
    )

    # Corner accents
    corner_size = 30
    corners = [
        (margin + 6, margin + 6),
        (W - margin - 6 - corner_size, margin + 6),
        (margin + 6, H - margin - 6 - corner_size),
        (W - margin - 6 - corner_size, H - margin - 6 - corner_size)
    ]
    for cx, cy in corners:
        draw_star(draw, cx + corner_size // 2, cy + corner_size // 2, 10, c3)

    # === TOP BAR with category ===
    bar_y = margin + 20
    draw.rounded_rectangle(
        [margin + 20, bar_y, W - margin - 20, bar_y + 40],
        radius=8, fill=(*c1, 200) if len(c1) < 4 else c1
    )
    cat_font = ImageFont.truetype(FONT_BOLD, 14)
    draw.text((margin + 35, bar_y + 10), category.upper(), fill=WHITE, font=cat_font)
    # Right side: decorative dots
    for i in range(5):
        dx = W - margin - 50 - i * 18
        draw.ellipse([dx, bar_y + 13, dx + 14, bar_y + 27], fill=c3)

    # === ICON AREA (left side, inside card frame) ===
    icon_x = margin + 100
    icon_y = H // 2 + 20
    # Icon background circle with glow
    for r in range(70, 30, -5):
        alpha = 30 + (70 - r) * 3
        glow_color = lerp_color(c1, c3, (70 - r) / 40)
        draw.ellipse([icon_x - r, icon_y - r, icon_x + r, icon_y + r],
                     fill=(*glow_color, alpha))
    # Inner circle
    draw.ellipse([icon_x - 35, icon_y - 35, icon_x + 35, icon_y + 35], fill=c2, outline=c3, width=3)
    # Icon text (emoji placeholder — rendered as text)
    icon_font = ImageFont.truetype(FONT_BOLD, 36)
    ibbox = icon_font.getbbox(icon_emoji)
    iw = ibbox[2] - ibbox[0]
    ih = ibbox[3] - ibbox[1]
    draw.text((icon_x - iw // 2, icon_y - ih // 2 - 4), icon_emoji, fill=WHITE, font=icon_font)

    # Energy rings around icon
    for i in range(3):
        ri = 50 + i * 12
        draw.ellipse([icon_x - ri, icon_y - ri, icon_x + ri, icon_y + ri],
                     outline=(*c3, 50 - i * 15), width=1)

    # === TITLE (center-right) ===
    title_x = 240
    title_y = 110
    title_font = ImageFont.truetype(FONT_BOLD, 48)
    # Measure multi-line title height
    title_lines = title.split("\n")
    line_height = 56
    total_title_h = line_height * len(title_lines)

    # Text shadow + draw each line
    for li, line in enumerate(title_lines):
        ly = title_y + li * line_height
        draw.text((title_x + 2, ly + 2), line, fill=(0, 0, 0, 150), font=title_font)
        draw.text((title_x, ly), line, fill=WHITE, font=title_font)

    # Underline accent below last title line
    last_line = title_lines[-1]
    lbbox = title_font.getbbox(last_line)
    lw = lbbox[2] - lbbox[0]
    lines_y = title_y + total_title_h + 4
    draw_gradient(draw, (title_x, lines_y, title_x + min(lw, 500), lines_y + 4), c3, c1)

    # === SUBTITLE ===
    sub_font = ImageFont.truetype(FONT_REG, 22)
    draw.text((title_x, lines_y + 14), subtitle, fill=(200, 210, 230), font=sub_font)

    # === FEATURE BULLETS ===
    bullet_font = ImageFont.truetype(FONT_REG, 16)
    features = get_features(title)
    bullet_y = lines_y + 46
    for feat in features[:3]:
        draw.ellipse([title_x, bullet_y + 4, title_x + 8, bullet_y + 12], fill=c3)
        draw.text((title_x + 16, bullet_y), feat, fill=(180, 190, 210), font=bullet_font)
        bullet_y += 26

    # === BOTTOM BAR ===
    bottom_y = H - margin - 55
    draw.rounded_rectangle(
        [margin + 20, bottom_y, W - margin - 20, bottom_y + 35],
        radius=8, fill=(*c2, 150) if len(c2) < 4 else c2
    )
    brand_font = ImageFont.truetype(FONT_BOLD, 16)
    draw.text((margin + 40, bottom_y + 8), "GIRL GONE AI", fill=c3, font=brand_font)

    # Power badge (right side of bottom bar)
    badge_text = get_power_label(title)
    badge_font = ImageFont.truetype(FONT_BOLD, 14)
    bbbox = badge_font.getbbox(badge_text)
    bw = bbbox[2] - bbbox[0]
    badge_x = W - margin - 40 - bw
    draw.rounded_rectangle([badge_x - 10, bottom_y + 4, badge_x + bw + 10, bottom_y + 30],
                           radius=6, fill=c3)
    draw.text((badge_x, bottom_y + 7), badge_text, fill=DARK, font=badge_font)

    # === SCATTERED DECORATIVE ELEMENTS ===
    random.seed(hash(title) + 99)
    # Stars in corners
    for _ in range(6):
        sx = random.choice([random.randint(margin + 20, 180), random.randint(W - 200, W - margin - 20)])
        sy = random.choice([random.randint(margin + 60, 200), random.randint(H - 180, H - margin - 60)])
        draw_sparkle(draw, sx, sy, random.randint(6, 14), c3)

    # Small floating diamonds
    for _ in range(8):
        dx = random.randint(180, W - 60)
        dy = random.randint(margin + 70, H - margin - 70)
        draw_diamond(draw, dx, dy, random.randint(3, 7), random.randint(4, 8),
                     lerp_color(c3, WHITE, random.random() * 0.5))

    # === SAVE ===
    final = img.convert("RGB")
    final.save(f"/home/boogarweed/girl-gone-ai/covers/{filename}", quality=95)
    print(f"  Saved {filename}")


def get_features(title):
    features_map = {
        "Podcast\nLaunch Kit": ["30-day launch roadmap", "Episode templates & scripts", "Growth strategy playbook"],
        "Side Hustle\nIncome Tracker": ["Revenue & expense dashboards", "Goal tracking & milestones", "Tax-ready export reports"],
        "Meal Prep\nPlanner": ["Weekly meal templates", "Smart grocery lists", "Nutrition tracking built-in"],
        "Midjourney\nPrompt Pack": ["500+ curated prompts", "Style & mood categories", "Commercial-use ready"],
        "Student Study\nPlanner": ["Assignment tracker", "Exam countdown timers", "GPA calculator included"],
        "Teacher\nPlanner": ["Lesson plan templates", "Grade book system", "Parent comm templates"],
        "Wedding\nPlanner": ["Timeline & checklist", "Budget tracker", "Vendor management"],
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


def get_power_label(title):
    labels = {
        "Podcast": "CREATOR PRO",
        "Side Hustle": "MONEY MAKER",
        "Meal Prep": "LIFE HACK",
        "Midjourney": "AI MASTER",
        "Student": "STUDY ACE",
        "Teacher": "EDU POWER",
        "Wedding": "DREAM DAY",
        "Invoice": "BIZ TOOLS",
        "Product Launch": "LAUNCH GO",
        "Client": "DEAL CLOSER",
        "Content": "VIRAL READY",
        "Social Media": "INFLUENCE+",
        "AI Productivity": "AI POWER",
        "Budget": "MONEY WISE",
        "Fitness": "FIT LIFE",
        "Resume": "CAREER UP",
    }
    for key, label in labels.items():
        if key.lower() in title.replace("\n", " ").lower():
            return label
    return "PREMIUM"


# ── COVER DEFINITIONS ──

covers = [
    # Original products (redesigned)
    {
        "title": "Podcast\nLaunch Kit",
        "subtitle": "Your complete 30-day podcast launch system",
        "icon": "MIC",
        "category": "Creator Tools",
        "colors": (PURPLE, (80, 40, 160), GOLD),
        "style": "energy",
        "file": "podcast-launch-kit.png"
    },
    {
        "title": "Side Hustle\nIncome Tracker",
        "subtitle": "Track every dollar from side gig to empire",
        "icon": "$$$",
        "category": "Finance",
        "colors": ((40, 100, 60), (20, 60, 40), GOLD),
        "style": "circuit",
        "file": "side-hustle.png"
    },
    {
        "title": "Meal Prep\nPlanner",
        "subtitle": "Eat smart, save time, crush your goals",
        "icon": "NOM",
        "category": "Lifestyle",
        "colors": ((200, 60, 80), (120, 30, 60), (255, 180, 50)),
        "style": "wave",
        "file": "meal-prep.png"
    },
    {
        "title": "Midjourney\nPrompt Pack",
        "subtitle": "500+ prompts to create stunning AI art",
        "icon": "ART",
        "category": "AI Tools",
        "colors": ((60, 20, 140), (30, 10, 80), PINK),
        "style": "cosmic",
        "file": "midjourney-prompts.png"
    },
    {
        "title": "Student Study\nPlanner",
        "subtitle": "Ace every class with the ultimate study system",
        "icon": "GPA",
        "category": "Education",
        "colors": (BLUE, (30, 60, 160), (100, 220, 255)),
        "style": "holographic",
        "file": "student-study.png"
    },
    {
        "title": "Teacher\nPlanner",
        "subtitle": "Plan, grade, and communicate like a pro",
        "icon": "EDU",
        "category": "Education",
        "colors": ((40, 120, 100), (20, 70, 60), (0, 230, 180)),
        "style": "circuit",
        "file": "teacher-planner.png"
    },
    {
        "title": "Wedding\nPlanner",
        "subtitle": "Plan your dream day without the stress",
        "icon": "VOW",
        "category": "Life Events",
        "colors": (PINK, (160, 30, 80), GOLD),
        "style": "holographic",
        "file": "wedding-planning.png"
    },
    {
        "title": "Invoice\nGenerator",
        "subtitle": "Professional invoices in seconds",
        "icon": "BIZ",
        "category": "Business",
        "colors": ((50, 50, 70), (25, 25, 45), (0, 200, 255)),
        "style": "circuit",
        "file": "invoice-generator.png"
    },
    {
        "title": "Product Launch\nPlaybook",
        "subtitle": "Launch with confidence, scale with data",
        "icon": "GO!",
        "category": "Business",
        "colors": ((180, 40, 40), (100, 20, 20), GOLD),
        "style": "energy",
        "file": "product-launch.png"
    },
    {
        "title": "Client Proposal\nTemplate",
        "subtitle": "Win clients with polished proposals",
        "icon": "WIN",
        "category": "Business",
        "colors": ((30, 50, 100), (15, 25, 60), (200, 170, 100)),
        "style": "holographic",
        "file": "client-proposal.png"
    },
    # NEW COVERS
    {
        "title": "Content\nCalendar",
        "subtitle": "30 days of content, planned and ready to post",
        "icon": "CAL",
        "category": "Social Media",
        "colors": (PINK, PURPLE, (255, 220, 100)),
        "style": "wave",
        "file": "content-calendar.png"
    },
    {
        "title": "Social Media\nBundle",
        "subtitle": "200+ templates for every platform",
        "icon": "SOC",
        "category": "Marketing",
        "colors": ((220, 50, 120), (140, 20, 80), (100, 200, 255)),
        "style": "cosmic",
        "file": "social-media-bundle.png"
    },
    {
        "title": "AI Productivity\nStarter Kit",
        "subtitle": "Work smarter with AI-powered workflows",
        "icon": "AI+",
        "category": "AI Tools",
        "colors": ((20, 20, 60), (60, 20, 100), (0, 255, 200)),
        "style": "circuit",
        "file": "ai-productivity-kit.png"
    },
    {
        "title": "Budget\nPlanner",
        "subtitle": "Take control of your money, one week at a time",
        "icon": "FIN",
        "category": "Finance",
        "colors": ((30, 80, 50), (15, 50, 30), (255, 215, 0)),
        "style": "holographic",
        "file": "budget-planner.png"
    },
    {
        "title": "Fitness\nTracker",
        "subtitle": "Crush your fitness goals with daily tracking",
        "icon": "FIT",
        "category": "Health",
        "colors": ((200, 50, 50), (100, 20, 40), (255, 150, 50)),
        "style": "energy",
        "file": "fitness-tracker.png"
    },
    {
        "title": "Resume\nBuilder",
        "subtitle": "Land your dream job with a standout resume",
        "icon": "CV+",
        "category": "Career",
        "colors": ((40, 40, 80), (20, 20, 50), (100, 180, 255)),
        "style": "holographic",
        "file": "resume-builder.png"
    },
]


if __name__ == "__main__":
    print(f"Generating {len(covers)} Pokemon-card-style covers...")
    for c in covers:
        generate_cover(
            title=c["title"],
            subtitle=c["subtitle"],
            icon_emoji=c["icon"],
            category=c["category"],
            color_scheme=c["colors"],
            style=c["style"],
            filename=c["file"]
        )
    print("Done!")
