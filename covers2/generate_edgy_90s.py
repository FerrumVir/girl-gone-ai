#!/usr/bin/env python3
"""Generate 90s-vibe edgy covers for Girl Gone AI — NO cartoon characters.

Uses bold geometric shapes, halftone patterns, Memphis-style elements,
grunge textures, and strong typography for an authentic 90s aesthetic.
"""

import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
OUT_DIR = "/home/boogarweed/girl-gone-ai/covers2"

# 90s neon palette
HOT_PINK = (255, 20, 147)
TEAL = (0, 206, 209)
ELECTRIC_PURPLE = (148, 0, 211)
LIME = (50, 205, 50)
NEON_YELLOW = (255, 255, 0)
BRIGHT_ORANGE = (255, 140, 0)
CORAL = (255, 127, 80)
LAVENDER = (200, 160, 255)
BABY_BLUE = (135, 206, 250)
MINT = (152, 255, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BG = (15, 10, 30)
CHARCOAL = (35, 30, 50)


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_gradient_bg(draw, c1, c2):
    for y in range(H):
        t = y / H
        draw.line([(0, y), (W, y)], fill=lerp_color(c1, c2, t))


def draw_halftone(draw, area, color, density=12, max_r=6):
    """Draw halftone dot pattern — classic 90s print effect."""
    x0, y0, x1, y1 = area
    for y in range(y0, y1, density):
        for x in range(x0, x1, density):
            dist_center = math.sqrt((x - (x0+x1)/2)**2 + (y - (y0+y1)/2)**2)
            max_dist = math.sqrt(((x1-x0)/2)**2 + ((y1-y0)/2)**2)
            t = max(0, 1 - dist_center / max_dist)
            r = int(max_r * t * (0.5 + random.random() * 0.5))
            if r > 0:
                draw.ellipse([x-r, y-r, x+r, y+r], fill=(*color, 60))


def draw_memphis_shapes(draw, seed, accent1, accent2):
    """Scatter bold Memphis-style geometric elements."""
    random.seed(seed)
    shapes = []
    for _ in range(18):
        x = random.randint(-30, W + 30)
        y = random.randint(-30, H + 30)
        size = random.randint(15, 70)
        c = random.choice([accent1, accent2, HOT_PINK, TEAL, NEON_YELLOW, LIME, ELECTRIC_PURPLE])
        shape_type = random.choice(["triangle", "circle_outline", "cross", "zigzag", "squiggle", "diamond"])
        shapes.append((x, y, size, c, shape_type))

    for x, y, size, c, shape_type in shapes:
        if shape_type == "triangle":
            angle = random.random() * math.pi * 2
            pts = []
            for i in range(3):
                a = angle + i * (2 * math.pi / 3)
                pts.append((x + size * math.cos(a), y + size * math.sin(a)))
            draw.polygon(pts, outline=(*c, 120), width=3)
        elif shape_type == "circle_outline":
            draw.ellipse([x-size, y-size, x+size, y+size], outline=(*c, 100), width=3)
        elif shape_type == "cross":
            arm = size
            draw.line([(x-arm, y), (x+arm, y)], fill=(*c, 100), width=4)
            draw.line([(x, y-arm), (x, y+arm)], fill=(*c, 100), width=4)
        elif shape_type == "zigzag":
            pts = [(x, y)]
            for seg in range(6):
                pts.append((pts[-1][0] + random.randint(12, 30),
                            pts[-1][1] + (18 if seg % 2 == 0 else -18)))
            for i in range(len(pts) - 1):
                draw.line([pts[i], pts[i+1]], fill=(*c, 80), width=3)
        elif shape_type == "squiggle":
            prev = None
            for t in range(30):
                sx = x + t * 4
                sy = y + math.sin(t * 0.5) * 15
                if prev:
                    draw.line([prev, (sx, sy)], fill=(*c, 70), width=3)
                prev = (sx, sy)
        elif shape_type == "diamond":
            draw.polygon([(x, y-size), (x+size*0.6, y), (x, y+size), (x-size*0.6, y)],
                         outline=(*c, 110), width=3)


def draw_starburst(draw, cx, cy, r, color, points=8):
    """Draw a starburst / asterisk shape."""
    pts = []
    for i in range(points * 2):
        angle = i * math.pi / points - math.pi / 2
        rad = r if i % 2 == 0 else r * 0.3
        pts.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    draw.polygon(pts, fill=color)


def draw_grunge_dots(draw, seed, count=100):
    """Scatter grunge-style random dots."""
    random.seed(seed + 999)
    for _ in range(count):
        x = random.randint(0, W)
        y = random.randint(0, H)
        r = random.randint(1, 4)
        a = random.randint(20, 60)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(255, 255, 255, a))


def draw_stripe_band(draw, y_start, height, color, angle_offset=0):
    """Draw diagonal stripe band — 90s graphic element."""
    stripe_w = 12
    for x in range(-H, W + H, stripe_w * 2):
        pts = [
            (x + angle_offset, y_start),
            (x + angle_offset + stripe_w, y_start),
            (x + angle_offset + stripe_w + height//3, y_start + height),
            (x + angle_offset + height//3, y_start + height),
        ]
        draw.polygon(pts, fill=(*color, 40))


def draw_themed_icon(draw, cx, cy, icon_type, color, size=80):
    """Draw a bold abstract icon for each product theme — no characters."""
    s = size / 80  # scale factor

    if icon_type == "mic":
        # Stylized microphone silhouette
        draw.rounded_rectangle([cx-int(12*s), cy-int(30*s), cx+int(12*s), cy+int(5*s)],
                               radius=int(12*s), outline=color, width=int(4*s))
        draw.line([(cx, cy+int(5*s)), (cx, cy+int(25*s))], fill=color, width=int(4*s))
        draw.arc([cx-int(20*s), cy-int(5*s), cx+int(20*s), cy+int(15*s)],
                 start=0, end=180, fill=color, width=int(3*s))
        draw.line([(cx-int(15*s), cy+int(25*s)), (cx+int(15*s), cy+int(25*s))],
                  fill=color, width=int(3*s))

    elif icon_type == "dollar":
        # Bold dollar sign with circle
        draw.ellipse([cx-int(35*s), cy-int(35*s), cx+int(35*s), cy+int(35*s)],
                     outline=color, width=int(4*s))
        font = ImageFont.truetype(FONT_BOLD, int(50*s))
        bb = font.getbbox("$")
        tw, th = bb[2]-bb[0], bb[3]-bb[1]
        draw.text((cx - tw//2, cy - th//2 - int(5*s)), "$", fill=color, font=font)

    elif icon_type == "fork_knife":
        # Crossed utensils
        draw.line([(cx-int(20*s), cy-int(30*s)), (cx+int(20*s), cy+int(30*s))],
                  fill=color, width=int(4*s))
        draw.line([(cx+int(20*s), cy-int(30*s)), (cx-int(20*s), cy+int(30*s))],
                  fill=color, width=int(4*s))
        draw.ellipse([cx-int(6*s), cy-int(6*s), cx+int(6*s), cy+int(6*s)], fill=color)

    elif icon_type == "palette":
        # Artist palette / abstract swirl
        draw.arc([cx-int(30*s), cy-int(30*s), cx+int(30*s), cy+int(30*s)],
                 start=30, end=330, fill=color, width=int(5*s))
        for i, angle in enumerate([60, 140, 220, 300]):
            r = int(8*s)
            dx = int(18*s) * math.cos(math.radians(angle))
            dy = int(18*s) * math.sin(math.radians(angle))
            c2 = [HOT_PINK, NEON_YELLOW, TEAL, LIME][i]
            draw.ellipse([cx+dx-r, cy+dy-r, cx+dx+r, cy+dy+r], fill=c2)

    elif icon_type == "book":
        # Open book
        draw.arc([cx-int(30*s), cy-int(10*s), cx, cy+int(20*s)],
                 start=180, end=360, fill=color, width=int(3*s))
        draw.arc([cx, cy-int(10*s), cx+int(30*s), cy+int(20*s)],
                 start=180, end=360, fill=color, width=int(3*s))
        draw.line([(cx, cy-int(25*s)), (cx, cy+int(20*s))], fill=color, width=int(3*s))
        draw.line([(cx-int(30*s), cy-int(10*s)), (cx-int(30*s), cy+int(20*s))], fill=color, width=int(3*s))
        draw.line([(cx+int(30*s), cy-int(10*s)), (cx+int(30*s), cy+int(20*s))], fill=color, width=int(3*s))

    elif icon_type == "heart":
        # Bold heart outline
        pts = []
        for t_val in range(0, 360, 3):
            rad = math.radians(t_val)
            x = 16 * (math.sin(rad) ** 3)
            y = -(13*math.cos(rad) - 5*math.cos(2*rad) - 2*math.cos(3*rad) - math.cos(4*rad))
            pts.append((cx + int(x * 2 * s), cy + int(y * 2 * s) - int(5*s)))
        for i in range(len(pts) - 1):
            draw.line([pts[i], pts[i+1]], fill=color, width=int(4*s))

    elif icon_type == "invoice":
        # Document / receipt
        draw.rounded_rectangle([cx-int(22*s), cy-int(30*s), cx+int(22*s), cy+int(30*s)],
                               radius=int(3*s), outline=color, width=int(3*s))
        for i in range(4):
            ly = cy - int(18*s) + i * int(12*s)
            lw = int(30*s) if i < 3 else int(18*s)
            draw.line([(cx-int(14*s), ly), (cx-int(14*s)+lw, ly)], fill=color, width=int(2*s))

    elif icon_type == "rocket":
        # Rocket silhouette
        draw.polygon([
            (cx, cy-int(35*s)),
            (cx-int(14*s), cy+int(10*s)),
            (cx+int(14*s), cy+int(10*s))
        ], outline=color, width=int(3*s))
        draw.polygon([
            (cx-int(14*s), cy+int(5*s)),
            (cx-int(22*s), cy+int(20*s)),
            (cx-int(8*s), cy+int(10*s))
        ], outline=color, width=int(2*s))
        draw.polygon([
            (cx+int(14*s), cy+int(5*s)),
            (cx+int(22*s), cy+int(20*s)),
            (cx+int(8*s), cy+int(10*s))
        ], outline=color, width=int(2*s))
        draw.ellipse([cx-int(5*s), cy-int(10*s), cx+int(5*s), cy], outline=color, width=int(2*s))

    elif icon_type == "briefcase":
        # Briefcase
        draw.rounded_rectangle([cx-int(28*s), cy-int(18*s), cx+int(28*s), cy+int(18*s)],
                               radius=int(4*s), outline=color, width=int(3*s))
        draw.arc([cx-int(10*s), cy-int(28*s), cx+int(10*s), cy-int(14*s)],
                 start=180, end=360, fill=color, width=int(3*s))

    elif icon_type == "calendar":
        # Calendar grid
        draw.rounded_rectangle([cx-int(26*s), cy-int(26*s), cx+int(26*s), cy+int(26*s)],
                               radius=int(3*s), outline=color, width=int(3*s))
        draw.line([(cx-int(26*s), cy-int(14*s)), (cx+int(26*s), cy-int(14*s))],
                  fill=color, width=int(2*s))
        for row in range(3):
            for col in range(4):
                bx = cx - int(20*s) + col * int(13*s)
                by = cy - int(8*s) + row * int(11*s)
                draw.rounded_rectangle([bx, by, bx+int(8*s), by+int(7*s)],
                                       radius=1, outline=(*color, 150), width=1)

    elif icon_type == "phone":
        # Smartphone
        draw.rounded_rectangle([cx-int(15*s), cy-int(28*s), cx+int(15*s), cy+int(28*s)],
                               radius=int(5*s), outline=color, width=int(3*s))
        draw.rounded_rectangle([cx-int(12*s), cy-int(22*s), cx+int(12*s), cy+int(18*s)],
                               radius=int(2*s), outline=(*color, 80), width=int(1*s))
        draw.ellipse([cx-int(3*s), cy+int(21*s), cx+int(3*s), cy+int(24*s)], outline=color, width=int(2*s))

    elif icon_type == "cpu":
        # CPU / AI chip
        draw.rounded_rectangle([cx-int(22*s), cy-int(22*s), cx+int(22*s), cy+int(22*s)],
                               radius=int(3*s), outline=color, width=int(3*s))
        draw.rounded_rectangle([cx-int(14*s), cy-int(14*s), cx+int(14*s), cy+int(14*s)],
                               radius=int(2*s), outline=color, width=int(2*s))
        for side_pos in [-int(16*s), -int(8*s), 0, int(8*s), int(16*s)]:
            draw.line([(cx+side_pos, cy-int(22*s)), (cx+side_pos, cy-int(28*s))], fill=color, width=int(2*s))
            draw.line([(cx+side_pos, cy+int(22*s)), (cx+side_pos, cy+int(28*s))], fill=color, width=int(2*s))
            draw.line([(cx-int(22*s), cy+side_pos), (cx-int(28*s), cy+side_pos)], fill=color, width=int(2*s))
            draw.line([(cx+int(22*s), cy+side_pos), (cx+int(28*s), cy+side_pos)], fill=color, width=int(2*s))

    elif icon_type == "piggybank":
        # Coin stack
        for i in range(4):
            oy = -i * int(8*s)
            draw.ellipse([cx-int(20*s), cy+oy-int(6*s), cx+int(20*s), cy+oy+int(6*s)],
                         outline=color, width=int(2*s))
        draw.line([(cx-int(20*s), cy), (cx-int(20*s), cy-int(24*s))], fill=color, width=int(2*s))
        draw.line([(cx+int(20*s), cy), (cx+int(20*s), cy-int(24*s))], fill=color, width=int(2*s))

    elif icon_type == "dumbbell":
        # Dumbbell
        draw.line([(cx-int(30*s), cy), (cx+int(30*s), cy)], fill=color, width=int(4*s))
        for side in [-1, 1]:
            wx = cx + side * int(30*s)
            draw.rounded_rectangle([wx-int(8*s), cy-int(14*s), wx+int(8*s), cy+int(14*s)],
                                   radius=int(2*s), outline=color, width=int(3*s))

    elif icon_type == "resume":
        # Resume with checkmarks
        draw.rounded_rectangle([cx-int(22*s), cy-int(30*s), cx+int(22*s), cy+int(30*s)],
                               radius=int(3*s), outline=color, width=int(3*s))
        for i in range(4):
            ly = cy - int(18*s) + i * int(12*s)
            draw.line([(cx-int(10*s), ly), (cx+int(14*s), ly)], fill=color, width=int(2*s))
            # Checkmark
            cx2 = cx - int(14*s)
            draw.line([(cx2-int(3*s), ly), (cx2, ly+int(3*s))], fill=LIME, width=int(2*s))
            draw.line([(cx2, ly+int(3*s)), (cx2+int(5*s), ly-int(3*s))], fill=LIME, width=int(2*s))

    elif icon_type == "sparkle":
        # Sparkle / glow-up star
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            length = int(30*s) if angle % 90 == 0 else int(18*s)
            draw.line([(cx, cy),
                       (cx + int(length * math.cos(rad)), cy + int(length * math.sin(rad)))],
                      fill=color, width=int(3*s) if angle % 90 == 0 else int(2*s))
        draw.ellipse([cx-int(6*s), cy-int(6*s), cx+int(6*s), cy+int(6*s)], fill=color)


def draw_90s_edgy_cover(title, subtitle, category, bg_colors, accent, icon_type, filename):
    """Generate a single edgy 90s cover with geometric graphics, no characters."""
    bg1, bg2 = bg_colors
    img = Image.new("RGBA", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    # Base gradient
    draw_gradient_bg(draw, bg1, bg2)

    # Halftone pattern in background
    random.seed(hash(title))
    draw_halftone(draw, (0, 0, W, H), accent, density=16, max_r=4)

    # Memphis geometric shapes
    draw_memphis_shapes(draw, hash(title) + 7, accent,
                        HOT_PINK if accent != HOT_PINK else TEAL)

    # Diagonal stripe band (top)
    draw_stripe_band(draw, 0, 60, accent, angle_offset=20)

    # Grunge texture dots
    draw_grunge_dots(draw, hash(title))

    # === MAIN FRAME ===
    m = 28
    # Thick edgy border — double frame
    draw.rounded_rectangle([m, m, W-m, H-m], radius=0, outline=accent, width=5)
    draw.rounded_rectangle([m+8, m+8, W-m-8, H-m-8], radius=0, outline=(*accent, 120), width=2)

    # Corner starbursts
    corner_r = 18
    for cx, cy in [(m+20, m+20), (W-m-20, m+20), (m+20, H-m-20), (W-m-20, H-m-20)]:
        draw_starburst(draw, cx, cy, corner_r, accent)

    # === TOP BANNER ===
    banner_h = 48
    banner_y = m + 12
    banner_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(banner_bg)
    bd.rectangle([m+12, banner_y, W-m-12, banner_y + banner_h], fill=(*BLACK, 180))
    img = Image.alpha_composite(img, banner_bg)
    draw = ImageDraw.Draw(img)

    cat_font = ImageFont.truetype(FONT_BOLD, 18)
    draw.text((m + 30, banner_y + 12), category.upper(), fill=accent, font=cat_font)

    brand_font = ImageFont.truetype(FONT_BOLD, 14)
    brand_text = "GIRL GONE AI"
    bb = brand_font.getbbox(brand_text)
    draw.text((W - m - 30 - (bb[2] - bb[0]), banner_y + 16), brand_text, fill=WHITE, font=brand_font)

    # === ICON AREA (left side) ===
    icon_cx = 180
    icon_cy = 340

    # Icon backdrop — large circle glow
    for r in range(90, 30, -5):
        alpha = int(20 + (90 - r) * 0.8)
        glow_c = lerp_color(bg1, accent, (90 - r) / 60)
        draw.ellipse([icon_cx-r, icon_cy-r, icon_cx+r, icon_cy+r], fill=(*glow_c, alpha))
    # Ring
    draw.ellipse([icon_cx-50, icon_cy-50, icon_cx+50, icon_cy+50], outline=accent, width=3)
    draw.ellipse([icon_cx-55, icon_cy-55, icon_cx+55, icon_cy+55], outline=(*accent, 60), width=2)

    # Draw themed abstract icon
    draw_themed_icon(draw, icon_cx, icon_cy, icon_type, WHITE, size=80)

    # === TITLE (right side) ===
    title_x = 340
    title_y = 115
    title_font = ImageFont.truetype(FONT_BOLD, 56)
    title_lines = title.split("\n")
    line_h = 66

    # Title background panel
    panel_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel_bg)
    total_h = line_h * len(title_lines) + 150
    pd.rectangle([title_x - 20, title_y - 15, W - m - 15, title_y + total_h],
                 fill=(10, 5, 25, 160))
    img = Image.alpha_composite(img, panel_bg)
    draw = ImageDraw.Draw(img)

    # Accent bar left of title
    draw.rectangle([title_x - 20, title_y - 15, title_x - 12, title_y + line_h * len(title_lines) + 5],
                   fill=accent)

    for li, line in enumerate(title_lines):
        ly = title_y + li * line_h
        # Bold black stroke
        for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            draw.text((title_x + dx, ly + dy), line, fill=BLACK, font=title_font)
        draw.text((title_x, ly), line, fill=WHITE, font=title_font)

    # Subtitle
    sub_y = title_y + len(title_lines) * line_h + 8
    sub_font = ImageFont.truetype(FONT_REG, 21)
    draw.text((title_x, sub_y), subtitle, fill=NEON_YELLOW, font=sub_font)

    # Feature bullets
    bullet_font = ImageFont.truetype(FONT_REG, 16)
    features = get_features(title)
    bullet_y = sub_y + 34
    for feat in features[:3]:
        # Geometric bullet (small diamond)
        bx = title_x + 6
        draw.polygon([(bx, bullet_y+7), (bx+5, bullet_y+12), (bx, bullet_y+17), (bx-5, bullet_y+12)],
                     fill=accent)
        draw.text((title_x + 18, bullet_y), feat, fill=(210, 220, 235), font=bullet_font)
        bullet_y += 26

    # === BOTTOM BAR ===
    bottom_y = H - m - 52
    bar_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bbd = ImageDraw.Draw(bar_bg)
    bbd.rectangle([m+12, bottom_y, W-m-12, bottom_y + 38], fill=(10, 5, 20, 200))
    img = Image.alpha_composite(img, bar_bg)
    draw = ImageDraw.Draw(img)

    # "90s EDITION" left
    ed_font = ImageFont.truetype(FONT_BOLD, 14)
    draw.text((m + 30, bottom_y + 10), "90s EDITION", fill=NEON_YELLOW, font=ed_font)

    # Separator dots
    for i in range(5):
        dx = m + 140 + i * 10
        draw.ellipse([dx, bottom_y + 15, dx + 6, bottom_y + 21], fill=(*accent, 100))

    # Power badge right
    badge_text = get_power_label(title)
    badge_font = ImageFont.truetype(FONT_BOLD, 15)
    bb_bbox = badge_font.getbbox(badge_text)
    bw = bb_bbox[2] - bb_bbox[0]
    badge_x = W - m - 30 - bw
    draw.rectangle([badge_x - 10, bottom_y + 4, badge_x + bw + 10, bottom_y + 33],
                   fill=accent)
    draw.text((badge_x, bottom_y + 8), badge_text, fill=WHITE, font=badge_font)

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
        "Morning Glow\nPlanner": ["AM routine builder", "Skincare checklist", "Glow-up tracking"],
    }
    for key, feats in features_map.items():
        if key.replace("\n", " ").lower() in title.replace("\n", " ").lower():
            return feats
    return ["Premium digital template", "Instant download", "Fully customizable"]


def get_power_label(title):
    labels = {
        "Podcast": "CREATOR VIBES",
        "Side Hustle": "MONEY MOVES",
        "Meal Prep": "TOTALLY RAD",
        "Midjourney": "AI MAGIC",
        "Student": "ALL THAT",
        "Teacher": "PHAT PLANS",
        "Wedding": "DA BOMB",
        "Invoice": "BIZ BABE",
        "Product Launch": "BLAST OFF",
        "Client": "FLY GIRL",
        "Content": "WORD UP",
        "Social Media": "AS IF!",
        "AI Productivity": "CYBER COOL",
        "Budget": "CHA-CHING",
        "Fitness": "GIRL POWER",
        "Resume": "YOU GO GIRL",
        "Morning Glow": "GLOW UP",
    }
    for key, label in labels.items():
        if key.lower() in title.replace("\n", " ").lower():
            return label
    return "90s PREMIUM"


# ── COVER DEFINITIONS ──

covers = [
    {
        "title": "Podcast\nLaunch Kit",
        "subtitle": "Your complete 30-day podcast launch system",
        "category": "Creator Tools",
        "bg": ((80, 20, 120), (25, 10, 50)),
        "accent": ELECTRIC_PURPLE,
        "icon": "mic",
        "file": "podcast-launch-kit.png"
    },
    {
        "title": "Side Hustle\nIncome Tracker",
        "subtitle": "Track every dollar from side gig to empire",
        "category": "Finance",
        "bg": ((20, 80, 60), (8, 35, 25)),
        "accent": LIME,
        "icon": "dollar",
        "file": "side-hustle.png"
    },
    {
        "title": "Meal Prep\nPlanner",
        "subtitle": "Eat smart, save time, crush your goals",
        "category": "Lifestyle",
        "bg": ((120, 30, 60), (50, 12, 25)),
        "accent": CORAL,
        "icon": "fork_knife",
        "file": "meal-prep.png"
    },
    {
        "title": "Midjourney\nPrompt Pack",
        "subtitle": "500+ prompts to create stunning AI art",
        "category": "AI Tools",
        "bg": ((55, 12, 100), (20, 5, 45)),
        "accent": LAVENDER,
        "icon": "palette",
        "file": "midjourney-prompts.png"
    },
    {
        "title": "Student Study\nPlanner",
        "subtitle": "Ace every class with the ultimate study system",
        "category": "Education",
        "bg": ((20, 50, 120), (8, 20, 55)),
        "accent": BABY_BLUE,
        "icon": "book",
        "file": "student-study.png"
    },
    {
        "title": "Teacher\nPlanner",
        "subtitle": "Plan, grade, and communicate like a pro",
        "category": "Education",
        "bg": ((20, 80, 70), (8, 35, 30)),
        "accent": TEAL,
        "icon": "book",
        "file": "teacher-planner.png"
    },
    {
        "title": "Wedding\nPlanner",
        "subtitle": "Plan your dream day without the stress",
        "category": "Life Events",
        "bg": ((120, 20, 80), (50, 8, 35)),
        "accent": HOT_PINK,
        "icon": "heart",
        "file": "wedding-planning.png"
    },
    {
        "title": "Invoice\nGenerator",
        "subtitle": "Professional invoices in seconds",
        "category": "Business",
        "bg": ((30, 30, 65), (12, 12, 28)),
        "accent": TEAL,
        "icon": "invoice",
        "file": "invoice-generator.png"
    },
    {
        "title": "Product Launch\nPlaybook",
        "subtitle": "Launch with confidence, scale with data",
        "category": "Business",
        "bg": ((100, 20, 30), (45, 8, 12)),
        "accent": BRIGHT_ORANGE,
        "icon": "rocket",
        "file": "product-launch.png"
    },
    {
        "title": "Client Proposal\nTemplate",
        "subtitle": "Win clients with polished proposals",
        "category": "Business",
        "bg": ((30, 40, 85), (12, 18, 38)),
        "accent": LAVENDER,
        "icon": "briefcase",
        "file": "client-proposal.png"
    },
    {
        "title": "Content\nCalendar",
        "subtitle": "30 days of content, planned and ready to post",
        "category": "Social Media",
        "bg": ((100, 20, 80), (45, 8, 35)),
        "accent": HOT_PINK,
        "icon": "calendar",
        "file": "content-calendar.png"
    },
    {
        "title": "Social Media\nBundle",
        "subtitle": "200+ templates for every platform",
        "category": "Marketing",
        "bg": ((80, 20, 100), (35, 8, 45)),
        "accent": CORAL,
        "icon": "phone",
        "file": "social-media-bundle.png"
    },
    {
        "title": "AI Productivity\nStarter Kit",
        "subtitle": "Work smarter with AI-powered workflows",
        "category": "AI Tools",
        "bg": ((15, 15, 55), (35, 12, 65)),
        "accent": MINT,
        "icon": "cpu",
        "file": "ai-productivity-kit.png"
    },
    {
        "title": "Budget\nPlanner",
        "subtitle": "Take control of your money, one week at a time",
        "category": "Finance",
        "bg": ((20, 60, 40), (8, 28, 18)),
        "accent": NEON_YELLOW,
        "icon": "piggybank",
        "file": "budget-planner.png"
    },
    {
        "title": "Fitness\nTracker",
        "subtitle": "Crush your fitness goals with daily tracking",
        "category": "Health & Wellness",
        "bg": ((100, 20, 40), (45, 8, 18)),
        "accent": BRIGHT_ORANGE,
        "icon": "dumbbell",
        "file": "fitness-tracker.png"
    },
    {
        "title": "Resume\nBuilder",
        "subtitle": "Land your dream job with a standout resume",
        "category": "Career",
        "bg": ((30, 30, 75), (12, 12, 32)),
        "accent": BABY_BLUE,
        "icon": "resume",
        "file": "resume-builder.png"
    },
]


if __name__ == "__main__":
    print(f"Generating {len(covers)} edgy 90s-vibe covers (no cartoons)...")
    for c in covers:
        draw_90s_edgy_cover(
            title=c["title"],
            subtitle=c["subtitle"],
            category=c["category"],
            bg_colors=c["bg"],
            accent=c["accent"],
            icon_type=c["icon"],
            filename=c["file"]
        )
    print(f"\nDone! {len(covers)} covers generated in {OUT_DIR}/")
