#!/usr/bin/env python3
"""Generate 90s floral girlie covers for Girl Gone AI.

90s vibe with floral patterns, pastel palette, feminine style.
"""

import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
OUT_DIR = "/home/boogarweed/girl-gone-ai/covers3"

# Girlie pastel + 90s palette
ROSE = (255, 105, 140)
BLUSH = (255, 182, 193)
HOT_PINK = (255, 20, 147)
MAUVE = (204, 153, 204)
LAVENDER = (200, 170, 255)
LILAC = (220, 190, 255)
PEACH = (255, 200, 160)
CORAL = (255, 150, 130)
MINT = (170, 240, 210)
BABY_BLUE = (170, 210, 255)
CREAM = (255, 245, 230)
SOFT_YELLOW = (255, 240, 170)
SAGE = (180, 210, 170)
DUSTY_ROSE = (200, 130, 140)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_PLUM = (40, 15, 35)
DEEP_ROSE = (80, 20, 50)


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_gradient_bg(draw, c1, c2):
    for y in range(H):
        t = y / H
        draw.line([(0, y), (W, y)], fill=lerp_color(c1, c2, t))


def draw_flower(draw, cx, cy, petal_r, num_petals, petal_color, center_color, alpha=80):
    """Draw a simple flower with round petals."""
    for i in range(num_petals):
        angle = (2 * math.pi * i / num_petals) + random.random() * 0.2
        px = cx + int(petal_r * 0.7 * math.cos(angle))
        py = cy + int(petal_r * 0.7 * math.sin(angle))
        r = petal_r
        draw.ellipse([px - r, py - r, px + r, py + r],
                     fill=(*petal_color, alpha))
    # Center
    cr = int(petal_r * 0.4)
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr],
                 fill=(*center_color, min(alpha + 40, 255)))


def draw_daisy(draw, cx, cy, size, petal_color, center_color, alpha=90):
    """Draw a 90s-style daisy with elongated petals."""
    num_petals = 8
    for i in range(num_petals):
        angle = (2 * math.pi * i / num_petals)
        for t in range(0, size, 2):
            px = cx + int(t * math.cos(angle))
            py = cy + int(t * math.sin(angle))
            r = max(1, int((size - t) * 0.25))
            draw.ellipse([px - r, py - r, px + r, py + r],
                         fill=(*petal_color, alpha))
    cr = int(size * 0.2)
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr],
                 fill=(*center_color, min(alpha + 50, 255)))


def draw_rose_spiral(draw, cx, cy, size, color, alpha=70):
    """Draw a stylized spiral rose."""
    prev = None
    for t in range(0, 200, 3):
        r = size * 0.05 * t / 10
        angle = t * 0.15
        px = cx + int(r * math.cos(angle))
        py = cy + int(r * math.sin(angle))
        if prev and r < size:
            draw.line([prev, (px, py)], fill=(*color, alpha), width=max(1, int(3 - r / size * 2)))
        prev = (px, py)
    draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(*color, alpha + 30))


def draw_vine(draw, start_x, start_y, length, direction, color, alpha=50):
    """Draw a curving vine with small leaves."""
    prev = (start_x, start_y)
    for t in range(0, length, 4):
        x = start_x + t * direction
        y = start_y + int(math.sin(t * 0.08) * 30)
        draw.line([prev, (x, y)], fill=(*color, alpha), width=2)
        if t % 20 == 0:
            leaf_angle = math.sin(t * 0.08) * 0.5 + math.pi / 4
            lx = x + int(8 * math.cos(leaf_angle))
            ly = y + int(8 * math.sin(leaf_angle))
            draw.ellipse([min(x, lx) - 2, min(y, ly) - 2, max(x, lx) + 2, max(y, ly) + 2],
                         fill=(*color, alpha + 20))
        prev = (x, y)


def draw_floral_border(draw, accent, seed):
    """Scatter flowers along edges for a border effect."""
    random.seed(seed)
    flower_colors = [ROSE, BLUSH, MAUVE, LAVENDER, PEACH, CORAL, LILAC]

    # Top and bottom borders
    for _ in range(12):
        x = random.randint(0, W)
        y = random.choice([random.randint(0, 80), random.randint(H - 80, H)])
        petal_r = random.randint(8, 22)
        num_petals = random.choice([5, 6, 7, 8])
        pc = random.choice(flower_colors)
        cc = SOFT_YELLOW if random.random() > 0.3 else WHITE
        alpha = random.randint(50, 90)
        draw_flower(draw, x, y, petal_r, num_petals, pc, cc, alpha)

    # Side borders
    for _ in range(8):
        x = random.choice([random.randint(0, 60), random.randint(W - 60, W)])
        y = random.randint(80, H - 80)
        petal_r = random.randint(8, 18)
        num_petals = random.choice([5, 6, 7])
        pc = random.choice(flower_colors)
        cc = SOFT_YELLOW
        alpha = random.randint(40, 80)
        draw_flower(draw, x, y, petal_r, num_petals, pc, cc, alpha)


def draw_scattered_flowers(draw, seed, accent):
    """Scatter flowers across the background for the floral pattern."""
    random.seed(seed + 42)
    flower_colors = [ROSE, BLUSH, MAUVE, LAVENDER, PEACH, CORAL, LILAC, MINT]

    # Background flowers (subtle)
    for _ in range(20):
        x = random.randint(-20, W + 20)
        y = random.randint(-20, H + 20)
        size = random.randint(6, 16)
        pc = random.choice(flower_colors)
        alpha = random.randint(25, 55)
        flower_type = random.choice(["simple", "daisy", "rose"])
        if flower_type == "simple":
            draw_flower(draw, x, y, size, random.choice([5, 6, 7]), pc, SOFT_YELLOW, alpha)
        elif flower_type == "daisy":
            draw_daisy(draw, x, y, size, pc, SOFT_YELLOW, alpha)
        else:
            draw_rose_spiral(draw, x, y, size, pc, alpha)

    # Accent flowers (brighter, fewer)
    for _ in range(6):
        x = random.randint(50, W - 50)
        y = random.randint(50, H - 50)
        size = random.randint(12, 28)
        pc = lerp_color(accent, random.choice(flower_colors), 0.5)
        draw_flower(draw, x, y, size, random.choice([5, 6, 7, 8]), pc, WHITE, random.randint(40, 70))


def draw_sparkle_dots(draw, seed, count=60):
    """Scatter glitter/sparkle dots in pastel colors."""
    random.seed(seed + 777)
    sparkle_colors = [WHITE, BLUSH, LAVENDER, SOFT_YELLOW, MINT, PEACH]
    for _ in range(count):
        x = random.randint(0, W)
        y = random.randint(0, H)
        r = random.randint(1, 3)
        c = random.choice(sparkle_colors)
        a = random.randint(30, 90)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(*c, a))


def draw_butterfly(draw, cx, cy, size, color, alpha=60):
    """Draw a tiny butterfly silhouette."""
    s = size
    # Left wing
    draw.ellipse([cx - s, cy - int(s * 0.6), cx, cy + int(s * 0.3)],
                 fill=(*color, alpha))
    # Right wing
    draw.ellipse([cx, cy - int(s * 0.6), cx + s, cy + int(s * 0.3)],
                 fill=(*color, alpha))
    # Body
    draw.line([(cx, cy - int(s * 0.4)), (cx, cy + int(s * 0.4))],
              fill=(*color, alpha + 30), width=1)


def draw_90s_girlie_elements(draw, seed, accent):
    """90s touches: stars, hearts, butterflies."""
    random.seed(seed + 333)

    # Mini hearts
    for _ in range(5):
        x = random.randint(40, W - 40)
        y = random.randint(40, H - 40)
        s = random.randint(4, 10)
        c = random.choice([ROSE, HOT_PINK, BLUSH, CORAL])
        a = random.randint(40, 80)
        # Simple heart shape
        draw.ellipse([x - s, y - s, x, y], fill=(*c, a))
        draw.ellipse([x, y - s, x + s, y], fill=(*c, a))
        draw.polygon([(x - s, y - int(s * 0.3)), (x + s, y - int(s * 0.3)),
                       (x, y + s)], fill=(*c, a))

    # Butterflies
    for _ in range(4):
        x = random.randint(30, W - 30)
        y = random.randint(30, H - 30)
        s = random.randint(6, 14)
        c = random.choice([LAVENDER, MAUVE, BABY_BLUE, BLUSH, MINT])
        draw_butterfly(draw, x, y, s, c, random.randint(40, 70))

    # Small stars (90s doodle style)
    for _ in range(8):
        x = random.randint(20, W - 20)
        y = random.randint(20, H - 20)
        r = random.randint(3, 8)
        c = random.choice([SOFT_YELLOW, WHITE, PEACH])
        a = random.randint(40, 80)
        pts = []
        for i in range(10):
            angle = i * math.pi / 5 - math.pi / 2
            rad = r if i % 2 == 0 else r * 0.4
            pts.append((x + int(rad * math.cos(angle)), y + int(rad * math.sin(angle))))
        draw.polygon(pts, fill=(*c, a))


def draw_themed_icon(draw, cx, cy, icon_type, color, size=80):
    """Draw a bold abstract icon for each product theme."""
    s = size / 80

    if icon_type == "mic":
        draw.rounded_rectangle([cx - int(12 * s), cy - int(30 * s), cx + int(12 * s), cy + int(5 * s)],
                               radius=int(12 * s), outline=color, width=int(4 * s))
        draw.line([(cx, cy + int(5 * s)), (cx, cy + int(25 * s))], fill=color, width=int(4 * s))
        draw.arc([cx - int(20 * s), cy - int(5 * s), cx + int(20 * s), cy + int(15 * s)],
                 start=0, end=180, fill=color, width=int(3 * s))
        draw.line([(cx - int(15 * s), cy + int(25 * s)), (cx + int(15 * s), cy + int(25 * s))],
                  fill=color, width=int(3 * s))

    elif icon_type == "dollar":
        draw.ellipse([cx - int(35 * s), cy - int(35 * s), cx + int(35 * s), cy + int(35 * s)],
                     outline=color, width=int(4 * s))
        font = ImageFont.truetype(FONT_BOLD, int(50 * s))
        bb = font.getbbox("$")
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        draw.text((cx - tw // 2, cy - th // 2 - int(5 * s)), "$", fill=color, font=font)

    elif icon_type == "fork_knife":
        draw.line([(cx - int(20 * s), cy - int(30 * s)), (cx + int(20 * s), cy + int(30 * s))],
                  fill=color, width=int(4 * s))
        draw.line([(cx + int(20 * s), cy - int(30 * s)), (cx - int(20 * s), cy + int(30 * s))],
                  fill=color, width=int(4 * s))
        draw.ellipse([cx - int(6 * s), cy - int(6 * s), cx + int(6 * s), cy + int(6 * s)], fill=color)

    elif icon_type == "palette":
        draw.arc([cx - int(30 * s), cy - int(30 * s), cx + int(30 * s), cy + int(30 * s)],
                 start=30, end=330, fill=color, width=int(5 * s))
        for i, angle in enumerate([60, 140, 220, 300]):
            r = int(8 * s)
            dx = int(18 * s) * math.cos(math.radians(angle))
            dy = int(18 * s) * math.sin(math.radians(angle))
            c2 = [ROSE, SOFT_YELLOW, LAVENDER, MINT][i]
            draw.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=c2)

    elif icon_type == "book":
        draw.arc([cx - int(30 * s), cy - int(10 * s), cx, cy + int(20 * s)],
                 start=180, end=360, fill=color, width=int(3 * s))
        draw.arc([cx, cy - int(10 * s), cx + int(30 * s), cy + int(20 * s)],
                 start=180, end=360, fill=color, width=int(3 * s))
        draw.line([(cx, cy - int(25 * s)), (cx, cy + int(20 * s))], fill=color, width=int(3 * s))
        draw.line([(cx - int(30 * s), cy - int(10 * s)), (cx - int(30 * s), cy + int(20 * s))],
                  fill=color, width=int(3 * s))
        draw.line([(cx + int(30 * s), cy - int(10 * s)), (cx + int(30 * s), cy + int(20 * s))],
                  fill=color, width=int(3 * s))

    elif icon_type == "heart":
        pts = []
        for t_val in range(0, 360, 3):
            rad = math.radians(t_val)
            x = 16 * (math.sin(rad) ** 3)
            y = -(13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
            pts.append((cx + int(x * 2 * s), cy + int(y * 2 * s) - int(5 * s)))
        for i in range(len(pts) - 1):
            draw.line([pts[i], pts[i + 1]], fill=color, width=int(4 * s))

    elif icon_type == "invoice":
        draw.rounded_rectangle([cx - int(22 * s), cy - int(30 * s), cx + int(22 * s), cy + int(30 * s)],
                               radius=int(3 * s), outline=color, width=int(3 * s))
        for i in range(4):
            ly = cy - int(18 * s) + i * int(12 * s)
            lw = int(30 * s) if i < 3 else int(18 * s)
            draw.line([(cx - int(14 * s), ly), (cx - int(14 * s) + lw, ly)], fill=color, width=int(2 * s))

    elif icon_type == "rocket":
        draw.polygon([
            (cx, cy - int(35 * s)),
            (cx - int(14 * s), cy + int(10 * s)),
            (cx + int(14 * s), cy + int(10 * s))
        ], outline=color, width=int(3 * s))
        draw.ellipse([cx - int(5 * s), cy - int(10 * s), cx + int(5 * s), cy], outline=color, width=int(2 * s))

    elif icon_type == "briefcase":
        draw.rounded_rectangle([cx - int(28 * s), cy - int(18 * s), cx + int(28 * s), cy + int(18 * s)],
                               radius=int(4 * s), outline=color, width=int(3 * s))
        draw.arc([cx - int(10 * s), cy - int(28 * s), cx + int(10 * s), cy - int(14 * s)],
                 start=180, end=360, fill=color, width=int(3 * s))

    elif icon_type == "calendar":
        draw.rounded_rectangle([cx - int(26 * s), cy - int(26 * s), cx + int(26 * s), cy + int(26 * s)],
                               radius=int(3 * s), outline=color, width=int(3 * s))
        draw.line([(cx - int(26 * s), cy - int(14 * s)), (cx + int(26 * s), cy - int(14 * s))],
                  fill=color, width=int(2 * s))
        for row in range(3):
            for col in range(4):
                bx = cx - int(20 * s) + col * int(13 * s)
                by = cy - int(8 * s) + row * int(11 * s)
                draw.rounded_rectangle([bx, by, bx + int(8 * s), by + int(7 * s)],
                                       radius=1, outline=(*color, 150), width=1)

    elif icon_type == "phone":
        draw.rounded_rectangle([cx - int(15 * s), cy - int(28 * s), cx + int(15 * s), cy + int(28 * s)],
                               radius=int(5 * s), outline=color, width=int(3 * s))
        draw.rounded_rectangle([cx - int(12 * s), cy - int(22 * s), cx + int(12 * s), cy + int(18 * s)],
                               radius=int(2 * s), outline=(*color, 80), width=int(1 * s))

    elif icon_type == "cpu":
        draw.rounded_rectangle([cx - int(22 * s), cy - int(22 * s), cx + int(22 * s), cy + int(22 * s)],
                               radius=int(3 * s), outline=color, width=int(3 * s))
        draw.rounded_rectangle([cx - int(14 * s), cy - int(14 * s), cx + int(14 * s), cy + int(14 * s)],
                               radius=int(2 * s), outline=color, width=int(2 * s))
        for side_pos in [-int(16 * s), -int(8 * s), 0, int(8 * s), int(16 * s)]:
            draw.line([(cx + side_pos, cy - int(22 * s)), (cx + side_pos, cy - int(28 * s))],
                      fill=color, width=int(2 * s))
            draw.line([(cx + side_pos, cy + int(22 * s)), (cx + side_pos, cy + int(28 * s))],
                      fill=color, width=int(2 * s))

    elif icon_type == "piggybank":
        for i in range(4):
            oy = -i * int(8 * s)
            draw.ellipse([cx - int(20 * s), cy + oy - int(6 * s), cx + int(20 * s), cy + oy + int(6 * s)],
                         outline=color, width=int(2 * s))
        draw.line([(cx - int(20 * s), cy), (cx - int(20 * s), cy - int(24 * s))], fill=color, width=int(2 * s))
        draw.line([(cx + int(20 * s), cy), (cx + int(20 * s), cy - int(24 * s))], fill=color, width=int(2 * s))

    elif icon_type == "dumbbell":
        draw.line([(cx - int(30 * s), cy), (cx + int(30 * s), cy)], fill=color, width=int(4 * s))
        for side in [-1, 1]:
            wx = cx + side * int(30 * s)
            draw.rounded_rectangle([wx - int(8 * s), cy - int(14 * s), wx + int(8 * s), cy + int(14 * s)],
                                   radius=int(2 * s), outline=color, width=int(3 * s))

    elif icon_type == "resume":
        draw.rounded_rectangle([cx - int(22 * s), cy - int(30 * s), cx + int(22 * s), cy + int(30 * s)],
                               radius=int(3 * s), outline=color, width=int(3 * s))
        for i in range(4):
            ly = cy - int(18 * s) + i * int(12 * s)
            draw.line([(cx - int(10 * s), ly), (cx + int(14 * s), ly)], fill=color, width=int(2 * s))
            cx2 = cx - int(14 * s)
            draw.line([(cx2 - int(3 * s), ly), (cx2, ly + int(3 * s))], fill=MINT, width=int(2 * s))
            draw.line([(cx2, ly + int(3 * s)), (cx2 + int(5 * s), ly - int(3 * s))], fill=MINT, width=int(2 * s))

    elif icon_type == "sparkle":
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            length = int(30 * s) if angle % 90 == 0 else int(18 * s)
            draw.line([(cx, cy),
                       (cx + int(length * math.cos(rad)), cy + int(length * math.sin(rad)))],
                      fill=color, width=int(3 * s) if angle % 90 == 0 else int(2 * s))
        draw.ellipse([cx - int(6 * s), cy - int(6 * s), cx + int(6 * s), cy + int(6 * s)], fill=color)


def draw_floral_90s_cover(title, subtitle, category, bg_colors, accent, icon_type, filename):
    """Generate a single 90s floral girlie cover."""
    bg1, bg2 = bg_colors
    img = Image.new("RGBA", (W, H), DARK_PLUM)
    draw = ImageDraw.Draw(img)

    # Base gradient
    draw_gradient_bg(draw, bg1, bg2)

    # Floral patterns
    seed = hash(title)
    draw_scattered_flowers(draw, seed, accent)
    draw_floral_border(draw, accent, seed + 100)

    # Vines along top and bottom
    draw_vine(draw, 0, 35, W // 2, 1, SAGE, 35)
    draw_vine(draw, W, H - 35, W // 2, -1, SAGE, 35)

    # 90s girlie elements (hearts, butterflies, stars)
    draw_90s_girlie_elements(draw, seed, accent)

    # Sparkle dots
    draw_sparkle_dots(draw, seed, 50)

    # === DECORATIVE FRAME ===
    m = 24
    # Soft rounded double frame
    draw.rounded_rectangle([m, m, W - m, H - m], radius=16, outline=(*accent, 180), width=3)
    draw.rounded_rectangle([m + 7, m + 7, W - m - 7, H - m - 7], radius=12, outline=(*accent, 80), width=1)

    # Corner flowers instead of starbursts
    for cx, cy in [(m + 24, m + 24), (W - m - 24, m + 24), (m + 24, H - m - 24), (W - m - 24, H - m - 24)]:
        draw_flower(draw, cx, cy, 12, 6, accent, SOFT_YELLOW, 120)

    # === TOP BANNER ===
    banner_h = 44
    banner_y = m + 10
    banner_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(banner_bg)
    bd.rounded_rectangle([m + 10, banner_y, W - m - 10, banner_y + banner_h],
                         radius=8, fill=(*DARK_PLUM, 160))
    img = Image.alpha_composite(img, banner_bg)
    draw = ImageDraw.Draw(img)

    cat_font = ImageFont.truetype(FONT_BOLD, 16)
    draw.text((m + 28, banner_y + 12), category.upper(), fill=accent, font=cat_font)

    brand_font = ImageFont.truetype(FONT_BOLD, 13)
    brand_text = "GIRL GONE AI"
    bb = brand_font.getbbox(brand_text)
    draw.text((W - m - 28 - (bb[2] - bb[0]), banner_y + 14), brand_text, fill=BLUSH, font=brand_font)

    # Small flower accents on banner
    draw_flower(draw, m + 14, banner_y + banner_h // 2, 5, 5, BLUSH, SOFT_YELLOW, 100)
    draw_flower(draw, W - m - 14, banner_y + banner_h // 2, 5, 5, BLUSH, SOFT_YELLOW, 100)

    # === ICON AREA (left side) ===
    icon_cx = 180
    icon_cy = 340

    # Floral wreath around the icon
    for i in range(12):
        angle = 2 * math.pi * i / 12
        fx = icon_cx + int(65 * math.cos(angle))
        fy = icon_cy + int(65 * math.sin(angle))
        fc = [ROSE, BLUSH, MAUVE, LAVENDER, PEACH, CORAL][i % 6]
        draw_flower(draw, fx, fy, 8, 5, fc, SOFT_YELLOW, 80)

    # Soft glow behind icon
    for r in range(80, 25, -4):
        alpha = int(15 + (80 - r) * 0.6)
        glow_c = lerp_color(bg1, accent, (80 - r) / 55)
        draw.ellipse([icon_cx - r, icon_cy - r, icon_cx + r, icon_cy + r], fill=(*glow_c, alpha))

    # Soft ring
    draw.ellipse([icon_cx - 48, icon_cy - 48, icon_cx + 48, icon_cy + 48],
                 outline=(*accent, 140), width=2)

    draw_themed_icon(draw, icon_cx, icon_cy, icon_type, WHITE, size=80)

    # === TITLE (right side) ===
    title_x = 340
    title_y = 115
    title_font = ImageFont.truetype(FONT_BOLD, 54)
    title_lines = title.split("\n")
    line_h = 64

    # Semi-transparent panel with rounded corners
    panel_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel_bg)
    total_h = line_h * len(title_lines) + 145
    pd.rounded_rectangle([title_x - 20, title_y - 15, W - m - 12, title_y + total_h],
                         radius=12, fill=(30, 15, 30, 140))
    img = Image.alpha_composite(img, panel_bg)
    draw = ImageDraw.Draw(img)

    # Floral accent bar left of title (gradient bar with flowers)
    bar_top = title_y - 10
    bar_bottom = title_y + line_h * len(title_lines) + 5
    for y_pos in range(bar_top, bar_bottom, 2):
        t = (y_pos - bar_top) / max(1, bar_bottom - bar_top)
        bc = lerp_color(accent, BLUSH, t)
        draw.line([(title_x - 18, y_pos), (title_x - 12, y_pos)], fill=(*bc, 200))
    # Tiny flowers on the accent bar
    for y_pos in range(bar_top + 15, bar_bottom - 10, 40):
        draw_flower(draw, title_x - 15, y_pos, 5, 5, BLUSH, SOFT_YELLOW, 130)

    for li, line in enumerate(title_lines):
        ly = title_y + li * line_h
        # Soft shadow
        for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            draw.text((title_x + dx, ly + dy), line, fill=DARK_PLUM, font=title_font)
        draw.text((title_x, ly), line, fill=WHITE, font=title_font)

    # Subtitle in accent color
    sub_y = title_y + len(title_lines) * line_h + 8
    sub_font = ImageFont.truetype(FONT_REG, 20)
    draw.text((title_x, sub_y), subtitle, fill=PEACH, font=sub_font)

    # Feature bullets with flower bullets
    bullet_font = ImageFont.truetype(FONT_REG, 15)
    features = get_features(title)
    bullet_y = sub_y + 32
    for feat in features[:3]:
        draw_flower(draw, title_x + 6, bullet_y + 8, 4, 5, accent, SOFT_YELLOW, 150)
        draw.text((title_x + 16, bullet_y), feat, fill=CREAM, font=bullet_font)
        bullet_y += 24

    # === BOTTOM BAR ===
    bottom_y = H - m - 48
    bar_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bbd = ImageDraw.Draw(bar_bg)
    bbd.rounded_rectangle([m + 10, bottom_y, W - m - 10, bottom_y + 36],
                          radius=8, fill=(30, 12, 28, 190))
    img = Image.alpha_composite(img, bar_bg)
    draw = ImageDraw.Draw(img)

    ed_font = ImageFont.truetype(FONT_BOLD, 13)
    draw.text((m + 28, bottom_y + 9), "90s FLORAL EDITION", fill=BLUSH, font=ed_font)

    # Flower separator dots
    for i in range(5):
        dx = m + 170 + i * 14
        draw_flower(draw, dx, bottom_y + 18, 3, 5, ROSE, SOFT_YELLOW, 100)

    badge_text = get_power_label(title)
    badge_font = ImageFont.truetype(FONT_BOLD, 14)
    bb_bbox = badge_font.getbbox(badge_text)
    bw = bb_bbox[2] - bb_bbox[0]
    badge_x = W - m - 28 - bw
    draw.rounded_rectangle([badge_x - 10, bottom_y + 3, badge_x + bw + 10, bottom_y + 31],
                           radius=6, fill=accent)
    draw.text((badge_x, bottom_y + 7), badge_text, fill=WHITE, font=badge_font)

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


def get_power_label(title):
    labels = {
        "Podcast": "QUEEN BEE",
        "Side Hustle": "BOSS BABE",
        "Meal Prep": "NOURISHED",
        "Midjourney": "DREAMY",
        "Student": "SLAY IT",
        "Teacher": "BLOOM",
        "Wedding": "FOREVER",
        "Invoice": "GIRLBOSS",
        "Product Launch": "GLOW UP",
        "Client": "DARLING",
        "Content": "ICONIC",
        "Social Media": "IT GIRL",
        "AI Productivity": "FUTURE BABE",
        "Budget": "RICH GIRL",
        "Fitness": "FIERCE",
        "Resume": "MAIN CHARACTER",
    }
    for key, label in labels.items():
        if key.lower() in title.replace("\n", " ").lower():
            return label
    return "FLORAL QUEEN"


# Cover definitions with girlie pastel backgrounds
covers = [
    {
        "title": "Podcast\nLaunch Kit",
        "subtitle": "Your complete 30-day podcast launch system",
        "category": "Creator Tools",
        "bg": ((90, 40, 100), (55, 20, 65)),
        "accent": MAUVE,
        "icon": "mic",
        "file": "podcast-launch-kit.png"
    },
    {
        "title": "Side Hustle\nIncome Tracker",
        "subtitle": "Track every dollar from side gig to empire",
        "category": "Finance",
        "bg": ((50, 80, 70), (30, 50, 45)),
        "accent": MINT,
        "icon": "dollar",
        "file": "side-hustle.png"
    },
    {
        "title": "Meal Prep\nPlanner",
        "subtitle": "Eat smart, save time, crush your goals",
        "category": "Lifestyle",
        "bg": ((110, 50, 70), (70, 30, 45)),
        "accent": CORAL,
        "icon": "fork_knife",
        "file": "meal-prep.png"
    },
    {
        "title": "Midjourney\nPrompt Pack",
        "subtitle": "500+ prompts to create stunning AI art",
        "category": "AI Tools",
        "bg": ((70, 40, 110), (45, 25, 70)),
        "accent": LILAC,
        "icon": "palette",
        "file": "midjourney-prompts.png"
    },
    {
        "title": "Student Study\nPlanner",
        "subtitle": "Ace every class with the ultimate study system",
        "category": "Education",
        "bg": ((50, 65, 110), (30, 40, 70)),
        "accent": BABY_BLUE,
        "icon": "book",
        "file": "student-study.png"
    },
    {
        "title": "Teacher\nPlanner",
        "subtitle": "Plan, grade, and communicate like a pro",
        "category": "Education",
        "bg": ((50, 85, 75), (30, 55, 50)),
        "accent": SAGE,
        "icon": "book",
        "file": "teacher-planner.png"
    },
    {
        "title": "Wedding\nPlanner",
        "subtitle": "Plan your dream day without the stress",
        "category": "Life Events",
        "bg": ((120, 50, 80), (75, 30, 55)),
        "accent": ROSE,
        "icon": "heart",
        "file": "wedding-planning.png"
    },
    {
        "title": "Invoice\nGenerator",
        "subtitle": "Professional invoices in seconds",
        "category": "Business",
        "bg": ((55, 50, 80), (35, 30, 55)),
        "accent": LAVENDER,
        "icon": "invoice",
        "file": "invoice-generator.png"
    },
    {
        "title": "Product Launch\nPlaybook",
        "subtitle": "Launch with confidence, scale with data",
        "category": "Business",
        "bg": ((110, 55, 60), (70, 35, 40)),
        "accent": PEACH,
        "icon": "rocket",
        "file": "product-launch.png"
    },
    {
        "title": "Client Proposal\nTemplate",
        "subtitle": "Win clients with polished proposals",
        "category": "Business",
        "bg": ((65, 55, 95), (40, 35, 60)),
        "accent": LILAC,
        "icon": "briefcase",
        "file": "client-proposal.png"
    },
    {
        "title": "Content\nCalendar",
        "subtitle": "30 days of content, planned and ready to post",
        "category": "Social Media",
        "bg": ((110, 45, 85), (70, 28, 55)),
        "accent": HOT_PINK,
        "icon": "calendar",
        "file": "content-calendar.png"
    },
    {
        "title": "Social Media\nBundle",
        "subtitle": "200+ templates for every platform",
        "category": "Marketing",
        "bg": ((95, 45, 90), (60, 28, 58)),
        "accent": BLUSH,
        "icon": "phone",
        "file": "social-media-bundle.png"
    },
    {
        "title": "AI Productivity\nStarter Kit",
        "subtitle": "Work smarter with AI-powered workflows",
        "category": "AI Tools",
        "bg": ((40, 50, 80), (25, 30, 55)),
        "accent": MINT,
        "icon": "cpu",
        "file": "ai-productivity-kit.png"
    },
    {
        "title": "Budget\nPlanner",
        "subtitle": "Take control of your money, one week at a time",
        "category": "Finance",
        "bg": ((55, 75, 60), (35, 50, 40)),
        "accent": SOFT_YELLOW,
        "icon": "piggybank",
        "file": "budget-planner.png"
    },
    {
        "title": "Fitness\nTracker",
        "subtitle": "Crush your fitness goals with daily tracking",
        "category": "Health & Wellness",
        "bg": ((100, 50, 60), (65, 30, 40)),
        "accent": CORAL,
        "icon": "dumbbell",
        "file": "fitness-tracker.png"
    },
    {
        "title": "Resume\nBuilder",
        "subtitle": "Land your dream job with a standout resume",
        "category": "Career",
        "bg": ((55, 55, 90), (35, 35, 58)),
        "accent": BABY_BLUE,
        "icon": "resume",
        "file": "resume-builder.png"
    },
]


if __name__ == "__main__":
    print(f"Generating {len(covers)} floral 90s girlie covers...")
    for c in covers:
        draw_floral_90s_cover(
            title=c["title"],
            subtitle=c["subtitle"],
            category=c["category"],
            bg_colors=c["bg"],
            accent=c["accent"],
            icon_type=c["icon"],
            filename=c["file"]
        )
    print(f"\nDone! {len(covers)} covers generated in {OUT_DIR}/")
