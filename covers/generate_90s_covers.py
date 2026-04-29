#!/usr/bin/env python3
"""Generate 90s-vibe product covers with cartoon characters for Girl Gone AI."""

import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
OUT_DIR = "/home/boogarweed/girl-gone-ai/covers"

# 90s color palette
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
DARK_BG = (25, 15, 45)

# Skin tones for variety
SKIN_LIGHT = (255, 220, 185)
SKIN_MED = (222, 180, 140)
SKIN_TAN = (198, 155, 115)


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_90s_bg(draw, img, bg1, bg2, accent):
    """Draw a 90s Memphis-style background."""
    # Base gradient
    for y in range(H):
        t = y / H
        c = lerp_color(bg1, bg2, t)
        draw.line([(0, y), (W, y)], fill=c)

    random.seed(42)

    # Memphis triangles
    for _ in range(12):
        x = random.randint(-20, W + 20)
        y = random.randint(-20, H + 20)
        size = random.randint(20, 60)
        angle = random.random() * math.pi * 2
        pts = []
        for i in range(3):
            a = angle + i * (2 * math.pi / 3)
            pts.append((x + size * math.cos(a), y + size * math.sin(a)))
        c = random.choice([HOT_PINK, TEAL, NEON_YELLOW, LIME, ELECTRIC_PURPLE, BRIGHT_ORANGE])
        draw.polygon(pts, fill=(*c, 50), outline=(*c, 90))

    # Confetti dots
    for _ in range(40):
        x = random.randint(0, W)
        y = random.randint(0, H)
        r = random.randint(3, 8)
        c = random.choice([HOT_PINK, TEAL, NEON_YELLOW, LIME, CORAL, LAVENDER])
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(*c, 70))

    # Zigzag lines
    for _ in range(6):
        start_x = random.randint(0, W)
        start_y = random.randint(0, H)
        c = random.choice([HOT_PINK, TEAL, NEON_YELLOW, accent])
        pts = [(start_x, start_y)]
        for seg in range(8):
            pts.append((pts[-1][0] + random.randint(15, 35),
                        pts[-1][1] + (20 if seg % 2 == 0 else -20)))
        for i in range(len(pts) - 1):
            draw.line([pts[i], pts[i + 1]], fill=(*c, 60), width=2)

    # Squiggly S-curves
    for _ in range(4):
        base_x = random.randint(0, W)
        base_y = random.randint(0, H)
        c = random.choice([HOT_PINK, TEAL, LIME, BRIGHT_ORANGE])
        prev = None
        for t in range(40):
            x = base_x + t * 3
            y = base_y + math.sin(t * 0.4) * 20
            if prev:
                draw.line([prev, (x, y)], fill=(*c, 50), width=2)
            prev = (x, y)

    # Stars (90s star bursts)
    for _ in range(8):
        cx = random.randint(40, W - 40)
        cy = random.randint(40, H - 40)
        size = random.randint(8, 20)
        c = random.choice([NEON_YELLOW, WHITE, HOT_PINK])
        draw_star_burst(draw, cx, cy, size, (*c, 80))


def draw_star_burst(draw, cx, cy, r, color):
    """Draw a 4-pointed star burst (90s style)."""
    pts = []
    for i in range(8):
        angle = i * math.pi / 4 - math.pi / 8
        rad = r if i % 2 == 0 else r * 0.35
        pts.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    rgb = color[:3]
    draw.polygon(pts, fill=rgb)


def draw_90s_card_frame(draw, accent1, accent2):
    """Draw a retro 90s card border with bold geometric elements."""
    m = 30
    # Thick outer border
    draw.rounded_rectangle([m, m, W - m, H - m], radius=18, outline=BLACK, width=6)
    draw.rounded_rectangle([m + 4, m + 4, W - m - 4, H - m - 4], radius=15, outline=accent1, width=3)

    # Corner circles (90s decorative)
    corner_r = 16
    corners = [(m + 10, m + 10), (W - m - 10, m + 10),
               (m + 10, H - m - 10), (W - m - 10, H - m - 10)]
    for cx, cy in corners:
        draw.ellipse([cx - corner_r, cy - corner_r, cx + corner_r, cy + corner_r],
                     fill=accent2, outline=BLACK, width=2)
        # Inner dot
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=accent1)


def draw_character_base(draw, cx, cy, scale, skin, hair_color, outfit_color, hair_style="long"):
    """Draw base cartoon character (cute chibi girl) facing forward."""
    s = scale

    # === BODY ===
    body_top = cy + int(28 * s)
    body_w = int(35 * s)
    body_h = int(50 * s)
    # Outfit / dress shape
    draw.rounded_rectangle(
        [cx - body_w, body_top, cx + body_w, body_top + body_h],
        radius=int(12 * s), fill=outfit_color, outline=BLACK, width=3
    )
    # Skirt flare
    draw.polygon([
        (cx - body_w - int(10 * s), body_top + body_h),
        (cx + body_w + int(10 * s), body_top + body_h),
        (cx + body_w + int(5 * s), body_top + int(25 * s)),
        (cx - body_w - int(5 * s), body_top + int(25 * s))
    ], fill=outfit_color, outline=BLACK, width=2)

    # === ARMS ===
    arm_y = body_top + int(12 * s)
    # Left arm
    draw.line([(cx - body_w, arm_y), (cx - body_w - int(25 * s), arm_y + int(20 * s))],
              fill=skin, width=int(10 * s))
    draw.ellipse([cx - body_w - int(25 * s) - int(7 * s), arm_y + int(20 * s) - int(7 * s),
                  cx - body_w - int(25 * s) + int(7 * s), arm_y + int(20 * s) + int(7 * s)],
                 fill=skin, outline=BLACK, width=2)
    # Right arm
    draw.line([(cx + body_w, arm_y), (cx + body_w + int(25 * s), arm_y + int(20 * s))],
              fill=skin, width=int(10 * s))
    draw.ellipse([cx + body_w + int(25 * s) - int(7 * s), arm_y + int(20 * s) - int(7 * s),
                  cx + body_w + int(25 * s) + int(7 * s), arm_y + int(20 * s) + int(7 * s)],
                 fill=skin, outline=BLACK, width=2)

    # === LEGS ===
    leg_y = body_top + body_h - int(5 * s)
    for lx in [cx - int(15 * s), cx + int(15 * s)]:
        draw.line([(lx, leg_y), (lx, leg_y + int(30 * s))], fill=skin, width=int(10 * s))
        # Shoes
        draw.ellipse([lx - int(8 * s), leg_y + int(25 * s),
                      lx + int(12 * s), leg_y + int(38 * s)],
                     fill=outfit_color, outline=BLACK, width=2)

    # === HEAD ===
    head_r = int(35 * s)
    head_cy = cy
    # Neck
    draw.rectangle([cx - int(8 * s), head_cy + head_r - int(5 * s),
                     cx + int(8 * s), body_top + int(5 * s)],
                    fill=skin)

    # Hair behind head
    if hair_style == "long":
        # Long flowing hair behind
        draw.ellipse([cx - head_r - int(12 * s), head_cy - head_r - int(8 * s),
                      cx + head_r + int(12 * s), head_cy + head_r + int(40 * s)],
                     fill=hair_color, outline=BLACK, width=2)
    elif hair_style == "short":
        draw.ellipse([cx - head_r - int(5 * s), head_cy - head_r - int(5 * s),
                      cx + head_r + int(5 * s), head_cy + head_r + int(5 * s)],
                     fill=hair_color, outline=BLACK, width=2)
    elif hair_style == "updo":
        # Bun on top
        draw.ellipse([cx - head_r - int(5 * s), head_cy - head_r - int(5 * s),
                      cx + head_r + int(5 * s), head_cy + head_r + int(5 * s)],
                     fill=hair_color, outline=BLACK, width=2)
        bun_r = int(18 * s)
        draw.ellipse([cx - bun_r, head_cy - head_r - bun_r - int(5*s),
                      cx + bun_r, head_cy - head_r + int(5*s)],
                     fill=hair_color, outline=BLACK, width=2)
    elif hair_style == "ponytail":
        draw.ellipse([cx - head_r - int(5 * s), head_cy - head_r - int(5 * s),
                      cx + head_r + int(5 * s), head_cy + head_r + int(5 * s)],
                     fill=hair_color, outline=BLACK, width=2)
        # Ponytail flowing right
        pts = [
            (cx + head_r, head_cy - int(10 * s)),
            (cx + head_r + int(30 * s), head_cy + int(10 * s)),
            (cx + head_r + int(25 * s), head_cy + int(40 * s)),
            (cx + head_r + int(5 * s), head_cy + int(30 * s)),
        ]
        draw.polygon(pts, fill=hair_color, outline=BLACK, width=2)
    elif hair_style == "curly":
        # Big curly hair
        for dx, dy in [(-15, -10), (15, -10), (-20, 5), (20, 5), (-10, -20), (10, -20), (0, -22)]:
            cr = int(20 * s)
            draw.ellipse([cx + int(dx * s) - cr, head_cy + int(dy * s) - cr,
                          cx + int(dx * s) + cr, head_cy + int(dy * s) + cr],
                         fill=hair_color, outline=BLACK, width=1)

    # Face circle
    draw.ellipse([cx - head_r, head_cy - head_r, cx + head_r, head_cy + head_r],
                 fill=skin, outline=BLACK, width=3)

    # Hair bangs/fringe on top
    if hair_style in ("long", "ponytail"):
        # Side-swept bangs
        draw.arc([cx - head_r - int(3*s), head_cy - head_r - int(5*s),
                  cx + int(10*s), head_cy - int(5*s)],
                 start=200, end=360, fill=hair_color, width=int(15*s))
    elif hair_style == "short":
        draw.arc([cx - head_r, head_cy - head_r - int(3*s),
                  cx + head_r, head_cy],
                 start=180, end=360, fill=hair_color, width=int(12*s))
    elif hair_style in ("updo", "curly"):
        draw.arc([cx - head_r - int(2*s), head_cy - head_r - int(5*s),
                  cx + head_r + int(2*s), head_cy - int(2*s)],
                 start=180, end=360, fill=hair_color, width=int(14*s))

    # === FACE ===
    eye_y = head_cy - int(5 * s)
    eye_sep = int(14 * s)
    eye_r = int(6 * s)

    # Eyes (big cute anime-style)
    for ex in [cx - eye_sep, cx + eye_sep]:
        # White
        draw.ellipse([ex - eye_r, eye_y - eye_r, ex + eye_r, eye_y + eye_r],
                     fill=WHITE, outline=BLACK, width=2)
        # Pupil
        pr = int(3.5 * s)
        draw.ellipse([ex - pr, eye_y - pr, ex + pr, eye_y + pr], fill=BLACK)
        # Shine
        sr = int(1.5 * s)
        draw.ellipse([ex - pr + int(2*s), eye_y - pr, ex - pr + int(2*s) + sr, eye_y - pr + sr],
                     fill=WHITE)

    # Blush circles
    blush_y = head_cy + int(5 * s)
    for bx in [cx - int(20 * s), cx + int(20 * s)]:
        draw.ellipse([bx - int(6*s), blush_y - int(3*s), bx + int(6*s), blush_y + int(3*s)],
                     fill=(255, 150, 150, 120))

    # Smile
    smile_y = head_cy + int(10 * s)
    draw.arc([cx - int(8*s), smile_y - int(5*s), cx + int(8*s), smile_y + int(5*s)],
             start=10, end=170, fill=BLACK, width=2)

    return {
        "head_cy": head_cy, "head_r": head_r, "body_top": body_top,
        "left_hand": (cx - body_w - int(25 * s), arm_y + int(20 * s)),
        "right_hand": (cx + body_w + int(25 * s), arm_y + int(20 * s)),
        "cx": cx, "s": s
    }


def draw_prop_lipstick(draw, x, y, s):
    """Lipstick tube prop."""
    tw = int(8 * s)
    th = int(30 * s)
    draw.rounded_rectangle([x - tw, y - th, x + tw, y], radius=3, fill=HOT_PINK, outline=BLACK, width=2)
    draw.rounded_rectangle([x - tw + 2, y - th - int(12*s), x + tw - 2, y - th + 2],
                           radius=2, fill=(220, 30, 80), outline=BLACK, width=2)


def draw_prop_headphones(draw, cx, cy, r, s):
    """Headphones on head."""
    hr = r + int(8 * s)
    draw.arc([cx - hr, cy - hr - int(5*s), cx + hr, cy + int(5*s)],
             start=200, end=340, fill=(50, 50, 50), width=int(6*s))
    # Ear cups
    for side in [-1, 1]:
        ex = cx + side * (hr - int(2*s))
        ey = cy
        draw.rounded_rectangle([ex - int(8*s), ey - int(12*s), ex + int(8*s), ey + int(12*s)],
                               radius=5, fill=TEAL, outline=BLACK, width=2)


def draw_prop_mic(draw, x, y, s):
    """Microphone prop."""
    # Handle
    draw.rectangle([x - int(3*s), y, x + int(3*s), y + int(25*s)],
                   fill=(100, 100, 100), outline=BLACK, width=2)
    # Head
    draw.ellipse([x - int(8*s), y - int(12*s), x + int(8*s), y + int(5*s)],
                 fill=(80, 80, 80), outline=BLACK, width=2)
    # Grill lines
    for ly in range(int(y - 8*s), int(y + 2*s), int(3*s)):
        draw.line([(x - int(6*s), ly), (x + int(6*s), ly)], fill=(120, 120, 120), width=1)


def draw_prop_laptop(draw, x, y, s):
    """Laptop prop."""
    lw, lh = int(30 * s), int(20 * s)
    # Screen
    draw.rounded_rectangle([x - lw, y - lh, x + lw, y], radius=3, fill=(50, 50, 80), outline=BLACK, width=2)
    # Screen glow
    draw.rounded_rectangle([x - lw + 3, y - lh + 3, x + lw - 3, y - 3], radius=2, fill=BABY_BLUE)
    # Base
    draw.polygon([(x - lw - 5, y), (x + lw + 5, y), (x + lw + 10, y + int(6*s)), (x - lw - 10, y + int(6*s))],
                 fill=(180, 180, 190), outline=BLACK, width=2)


def draw_prop_book(draw, x, y, s, color=TEAL):
    """Book prop."""
    bw, bh = int(18*s), int(24*s)
    draw.rounded_rectangle([x - bw, y - bh, x + bw, y], radius=3, fill=color, outline=BLACK, width=2)
    # Spine line
    draw.line([(x - bw + int(4*s), y - bh + 2), (x - bw + int(4*s), y - 2)], fill=BLACK, width=2)
    # Lines on cover
    for ly in range(int(y - bh + 8*s), int(y - 5*s), int(5*s)):
        draw.line([(x - bw + int(8*s), ly), (x + bw - int(5*s), ly)], fill=(*BLACK, 80), width=1)


def draw_prop_paintbrush(draw, x, y, s):
    """Paintbrush prop."""
    # Handle
    draw.line([(x, y), (x + int(8*s), y + int(35*s))], fill=(180, 130, 70), width=int(5*s))
    # Bristles
    draw.polygon([
        (x - int(6*s), y - int(4*s)),
        (x + int(6*s), y - int(4*s)),
        (x + int(3*s), y + int(8*s)),
        (x - int(3*s), y + int(8*s))
    ], fill=ELECTRIC_PURPLE, outline=BLACK, width=2)


def draw_prop_cooking_spoon(draw, x, y, s):
    """Cooking spoon prop."""
    draw.line([(x, y), (x, y + int(35*s))], fill=(180, 130, 70), width=int(4*s))
    draw.ellipse([x - int(10*s), y - int(10*s), x + int(10*s), y + int(5*s)],
                 fill=(180, 130, 70), outline=BLACK, width=2)


def draw_prop_bouquet(draw, x, y, s):
    """Flower bouquet prop."""
    # Stems
    for dx in [-5, 0, 5]:
        draw.line([(x + int(dx*s), y + int(15*s)), (x + int(dx*s), y + int(30*s))],
                  fill=(80, 160, 80), width=int(2*s))
    # Flowers
    colors = [HOT_PINK, CORAL, LAVENDER, NEON_YELLOW, HOT_PINK]
    positions = [(-8, -5), (8, -5), (0, -10), (-5, 2), (5, 2)]
    for (dx, dy), c in zip(positions, colors):
        fr = int(7 * s)
        fx, fy = x + int(dx * s), y + int(dy * s)
        draw.ellipse([fx - fr, fy - fr, fx + fr, fy + fr], fill=c, outline=BLACK, width=1)
        # Center
        draw.ellipse([fx - int(2*s), fy - int(2*s), fx + int(2*s), fy + int(2*s)], fill=NEON_YELLOW)


def draw_prop_money(draw, x, y, s):
    """Dollar bills prop."""
    for i, (dx, dy, rot) in enumerate([(0, 0, 5), (-8, 5, -10), (6, -3, 15)]):
        bw, bh = int(22*s), int(12*s)
        bx, by = x + int(dx*s), y + int(dy*s)
        draw.rounded_rectangle([bx - bw, by - bh, bx + bw, by + bh],
                               radius=2, fill=(100, 200, 100), outline=(50, 130, 50), width=2)
        font = ImageFont.truetype(FONT_BOLD, max(10, int(12*s)))
        draw.text((bx - int(4*s), by - int(5*s)), "$", fill=(50, 130, 50), font=font)


def draw_prop_piggy_bank(draw, x, y, s):
    """Piggy bank prop."""
    # Body
    bw, bh = int(25*s), int(18*s)
    draw.ellipse([x - bw, y - bh, x + bw, y + bh], fill=HOT_PINK, outline=BLACK, width=2)
    # Snout
    draw.ellipse([x + bw - int(8*s), y - int(5*s), x + bw + int(8*s), y + int(5*s)],
                 fill=(255, 150, 170), outline=BLACK, width=2)
    # Nostril dots
    draw.ellipse([x + bw, y - int(2*s), x + bw + int(3*s), y + int(1*s)], fill=BLACK)
    draw.ellipse([x + bw + int(4*s), y - int(2*s), x + bw + int(7*s), y + int(1*s)], fill=BLACK)
    # Eye
    draw.ellipse([x + int(5*s), y - int(10*s), x + int(10*s), y - int(5*s)], fill=BLACK)
    # Coin slot
    draw.line([(x - int(8*s), y - bh + int(2*s)), (x + int(5*s), y - bh + int(2*s))],
              fill=BLACK, width=int(2*s))
    # Legs
    for lx in [x - int(12*s), x - int(5*s), x + int(5*s), x + int(12*s)]:
        draw.rectangle([lx - int(3*s), y + bh - int(2*s), lx + int(3*s), y + bh + int(8*s)],
                       fill=HOT_PINK, outline=BLACK, width=1)


def draw_prop_dumbbell(draw, x, y, s):
    """Dumbbell prop."""
    # Bar
    draw.rounded_rectangle([x - int(20*s), y - int(3*s), x + int(20*s), y + int(3*s)],
                           radius=2, fill=(160, 160, 170), outline=BLACK, width=2)
    # Weights
    for side in [-1, 1]:
        wx = x + side * int(20*s)
        draw.rounded_rectangle([wx - int(6*s), y - int(10*s), wx + int(6*s), y + int(10*s)],
                               radius=3, fill=ELECTRIC_PURPLE, outline=BLACK, width=2)


def draw_prop_rocket(draw, x, y, s):
    """Rocket prop."""
    # Body
    draw.polygon([
        (x, y - int(25*s)),
        (x - int(10*s), y + int(10*s)),
        (x + int(10*s), y + int(10*s))
    ], fill=WHITE, outline=BLACK, width=2)
    # Window
    draw.ellipse([x - int(4*s), y - int(8*s), x + int(4*s), y], fill=BABY_BLUE, outline=BLACK, width=1)
    # Fins
    for side in [-1, 1]:
        fx = x + side * int(10*s)
        draw.polygon([
            (fx, y + int(5*s)),
            (fx + side * int(8*s), y + int(15*s)),
            (fx, y + int(15*s))
        ], fill=HOT_PINK, outline=BLACK, width=1)
    # Flame
    draw.polygon([
        (x - int(6*s), y + int(10*s)),
        (x, y + int(22*s)),
        (x + int(6*s), y + int(10*s))
    ], fill=BRIGHT_ORANGE)
    draw.polygon([
        (x - int(3*s), y + int(10*s)),
        (x, y + int(18*s)),
        (x + int(3*s), y + int(10*s))
    ], fill=NEON_YELLOW)


def draw_prop_briefcase(draw, x, y, s):
    """Briefcase prop."""
    bw, bh = int(22*s), int(16*s)
    draw.rounded_rectangle([x - bw, y - bh, x + bw, y + bh],
                           radius=4, fill=(140, 90, 50), outline=BLACK, width=2)
    # Handle
    draw.arc([x - int(8*s), y - bh - int(8*s), x + int(8*s), y - bh + int(4*s)],
             start=180, end=360, fill=BLACK, width=int(3*s))
    # Clasp
    draw.rounded_rectangle([x - int(5*s), y - int(3*s), x + int(5*s), y + int(3*s)],
                           radius=2, fill=NEON_YELLOW, outline=BLACK, width=1)


def draw_prop_phone(draw, x, y, s):
    """Smartphone prop (selfie pose)."""
    pw, ph = int(10*s), int(18*s)
    draw.rounded_rectangle([x - pw, y - ph, x + pw, y + ph],
                           radius=int(3*s), fill=(40, 40, 50), outline=BLACK, width=2)
    # Screen
    draw.rounded_rectangle([x - pw + 2, y - ph + int(3*s), x + pw - 2, y + ph - int(3*s)],
                           radius=int(2*s), fill=BABY_BLUE)
    # Camera dot
    draw.ellipse([x - int(2*s), y - ph + int(1*s), x + int(2*s), y - ph + int(3*s)], fill=(60, 60, 70))


def draw_prop_calendar(draw, x, y, s):
    """Calendar prop."""
    cw, ch = int(22*s), int(20*s)
    draw.rounded_rectangle([x - cw, y - ch, x + cw, y + ch],
                           radius=3, fill=WHITE, outline=BLACK, width=2)
    # Header
    draw.rounded_rectangle([x - cw, y - ch, x + cw, y - ch + int(8*s)],
                           radius=3, fill=CORAL, outline=BLACK, width=2)
    # Grid lines
    for gy in range(3):
        ly = y - ch + int(12*s) + gy * int(9*s)
        draw.line([(x - cw + 3, ly), (x + cw - 3, ly)], fill=(200, 200, 200), width=1)
    for gx in range(4):
        lx = x - cw + int(5*s) + gx * int(10*s)
        draw.line([(lx, y - ch + int(8*s)), (lx, y + ch - 3)], fill=(200, 200, 200), width=1)


def draw_prop_resume(draw, x, y, s):
    """Resume/document prop."""
    pw, ph = int(18*s), int(24*s)
    draw.rounded_rectangle([x - pw, y - ph, x + pw, y + ph],
                           radius=2, fill=WHITE, outline=BLACK, width=2)
    # Photo placeholder
    draw.rounded_rectangle([x - pw + int(3*s), y - ph + int(3*s),
                            x - pw + int(10*s), y - ph + int(10*s)],
                           radius=1, fill=BABY_BLUE, outline=(180, 180, 180), width=1)
    # Text lines
    for i in range(6):
        lw = int((12 + random.randint(0, 8)) * s)
        ly = y - ph + int(14*s) + i * int(5*s)
        draw.line([(x - pw + int(3*s), ly), (x - pw + int(3*s) + lw, ly)],
                  fill=(180, 180, 180), width=int(2*s))


def draw_prop_glasses(draw, cx, eye_y, s):
    """Round glasses on face."""
    gr = int(10 * s)
    sep = int(14 * s)
    for ex in [cx - sep, cx + sep]:
        draw.ellipse([ex - gr, eye_y - gr, ex + gr, eye_y + gr],
                     outline=(60, 60, 80), width=int(2*s))
    # Bridge
    draw.arc([cx - sep + gr, eye_y - int(4*s), cx + sep - gr, eye_y + int(4*s)],
             start=180, end=360, fill=(60, 60, 80), width=int(2*s))


def draw_prop_chef_hat(draw, cx, top_y, s):
    """Chef hat prop."""
    hw = int(25 * s)
    hh = int(25 * s)
    # Puffy top
    for dx in [-15, 0, 15]:
        r = int(16 * s)
        draw.ellipse([cx + int(dx*s) - r, top_y - hh - r, cx + int(dx*s) + r, top_y - hh + r],
                     fill=WHITE, outline=BLACK, width=2)
    # Band
    draw.rounded_rectangle([cx - hw, top_y - int(5*s), cx + hw, top_y + int(5*s)],
                           radius=3, fill=WHITE, outline=BLACK, width=2)


def generate_90s_cover(title, subtitle, category, bg_colors, accent, char_type, filename):
    """Generate a single 90s-vibe cover with cartoon character."""
    bg1, bg2 = bg_colors
    img = Image.new("RGBA", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    # 90s Memphis background
    draw_90s_bg(draw, img, bg1, bg2, accent)

    # Card frame
    draw_90s_card_frame(draw, accent, HOT_PINK if accent != HOT_PINK else TEAL)

    # === TOP BANNER ===
    banner_h = 52
    banner_y = 42
    # Semi-transparent banner bg
    banner_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(banner_bg)
    bd.rounded_rectangle([50, banner_y, W - 50, banner_y + banner_h],
                         radius=10, fill=(*accent, 220))
    img = Image.alpha_composite(img, banner_bg)
    draw = ImageDraw.Draw(img)

    cat_font = ImageFont.truetype(FONT_BOLD, 18)
    draw.text((70, banner_y + 14), category.upper(), fill=WHITE, font=cat_font)

    # "GIRL GONE AI" right-aligned in banner
    brand_font = ImageFont.truetype(FONT_BOLD, 14)
    brand_text = "GIRL GONE AI"
    bb = brand_font.getbbox(brand_text)
    draw.text((W - 70 - (bb[2] - bb[0]), banner_y + 18), brand_text, fill=WHITE, font=brand_font)

    # === CHARACTER (left side) ===
    char_cx = 220
    char_cy = 310
    char_scale = 2.2

    skin = random.choice([SKIN_LIGHT, SKIN_MED, SKIN_TAN])
    hair_colors = [(60, 30, 15), (30, 20, 10), (180, 130, 60), (200, 50, 50), (100, 60, 140), HOT_PINK]
    random.seed(hash(title))
    hair_color = random.choice(hair_colors)
    hair_styles = ["long", "short", "updo", "ponytail", "curly"]
    hair_style = random.choice(hair_styles)

    # Draw character with themed props
    info = draw_character_base(draw, char_cx, char_cy, char_scale, skin, hair_color, accent, hair_style)

    # Draw themed props based on character type
    rh = info["right_hand"]
    lh = info["left_hand"]
    s = info["s"]
    hcy = info["head_cy"]
    hr = info["head_r"]

    if char_type == "podcast":
        draw_prop_headphones(draw, char_cx, hcy - int(5*s), hr, s * 0.8)
        draw_prop_mic(draw, rh[0] + int(5*s), rh[1] - int(20*s), s)
    elif char_type == "money":
        draw_prop_laptop(draw, lh[0] - int(5*s), lh[1] - int(5*s), s * 0.8)
        draw_prop_money(draw, rh[0] + int(10*s), rh[1] - int(10*s), s * 0.8)
    elif char_type == "cooking":
        draw_prop_chef_hat(draw, char_cx, hcy - hr, s)
        draw_prop_cooking_spoon(draw, rh[0] + int(5*s), rh[1] - int(15*s), s)
    elif char_type == "artist":
        draw_prop_paintbrush(draw, rh[0], rh[1] - int(15*s), s)
    elif char_type == "student":
        draw_prop_glasses(draw, char_cx, hcy - int(5*s), s)
        draw_prop_book(draw, lh[0] - int(5*s), lh[1], s, TEAL)
    elif char_type == "teacher":
        draw_prop_glasses(draw, char_cx, hcy - int(5*s), s)
        draw_prop_book(draw, lh[0] - int(5*s), lh[1], s, CORAL)
    elif char_type == "wedding":
        draw_prop_bouquet(draw, rh[0], rh[1] - int(5*s), s)
    elif char_type == "business":
        draw_prop_briefcase(draw, lh[0], lh[1] + int(5*s), s * 0.8)
    elif char_type == "rocket":
        draw_prop_rocket(draw, rh[0] + int(10*s), rh[1] - int(20*s), s)
    elif char_type == "proposal":
        draw_prop_resume(draw, lh[0] - int(5*s), lh[1], s * 0.8)
    elif char_type == "calendar":
        draw_prop_calendar(draw, rh[0] + int(10*s), rh[1] - int(5*s), s * 0.8)
    elif char_type == "selfie":
        draw_prop_phone(draw, rh[0] + int(5*s), rh[1] - int(10*s), s)
    elif char_type == "ai":
        draw_prop_laptop(draw, lh[0] - int(10*s), lh[1] - int(5*s), s * 0.8)
    elif char_type == "piggybank":
        draw_prop_piggy_bank(draw, rh[0] + int(15*s), rh[1], s)
    elif char_type == "fitness":
        draw_prop_dumbbell(draw, rh[0] + int(5*s), rh[1] - int(5*s), s * 0.8)
    elif char_type == "resume":
        draw_prop_resume(draw, rh[0] + int(5*s), rh[1] - int(5*s), s)
    elif char_type == "lipstick":
        draw_prop_lipstick(draw, rh[0] + int(3*s), rh[1] - int(5*s), s)

    # === TITLE (right side) ===
    title_x = 420
    title_y = 130
    title_font = ImageFont.truetype(FONT_BOLD, 52)
    title_lines = title.split("\n")
    line_h = 62

    # Title background panel (semi-transparent)
    panel_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel_bg)
    total_h = line_h * len(title_lines) + 140
    pd.rounded_rectangle([title_x - 20, title_y - 20, W - 55, title_y + total_h],
                         radius=14, fill=(20, 10, 35, 160))
    img = Image.alpha_composite(img, panel_bg)
    draw = ImageDraw.Draw(img)

    for li, line in enumerate(title_lines):
        ly = title_y + li * line_h
        # Bold black outline effect
        for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            draw.text((title_x + dx, ly + dy), line, fill=BLACK, font=title_font)
        draw.text((title_x, ly), line, fill=WHITE, font=title_font)

    # Subtitle
    sub_y = title_y + len(title_lines) * line_h + 10
    sub_font = ImageFont.truetype(FONT_REG, 22)
    draw.text((title_x, sub_y), subtitle, fill=NEON_YELLOW, font=sub_font)

    # Feature bullets
    bullet_font = ImageFont.truetype(FONT_REG, 17)
    features = get_features_90s(title)
    bullet_y = sub_y + 35
    for feat in features[:3]:
        # 90s star bullet
        draw_star_burst(draw, title_x + 8, bullet_y + 8, 8, accent)
        draw.text((title_x + 22, bullet_y), feat, fill=(220, 230, 240), font=bullet_font)
        bullet_y += 28

    # === BOTTOM BAR ===
    bottom_y = H - 80
    # Bottom bar bg
    bb_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bbd = ImageDraw.Draw(bb_bg)
    bbd.rounded_rectangle([50, bottom_y, W - 50, bottom_y + 40],
                          radius=10, fill=(15, 10, 30, 200))
    img = Image.alpha_composite(img, bb_bg)
    draw = ImageDraw.Draw(img)

    # 90s-style power badge
    badge_text = get_power_label_90s(title)
    badge_font = ImageFont.truetype(FONT_BOLD, 16)
    bb_bbox = badge_font.getbbox(badge_text)
    bw = bb_bbox[2] - bb_bbox[0]
    badge_x = W - 80 - bw
    draw.rounded_rectangle([badge_x - 12, bottom_y + 5, badge_x + bw + 12, bottom_y + 35],
                           radius=8, fill=accent)
    draw.text((badge_x, bottom_y + 8), badge_text, fill=WHITE, font=badge_font)

    # "90s EDITION" label on left
    ed_font = ImageFont.truetype(FONT_BOLD, 14)
    draw.text((70, bottom_y + 12), "90s EDITION", fill=NEON_YELLOW, font=ed_font)

    # === SAVE ===
    final = img.convert("RGB")
    final.save(f"{OUT_DIR}/{filename}", quality=95)
    print(f"  Saved {filename}")


def get_features_90s(title):
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


def get_power_label_90s(title):
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
        "bg": ((80, 20, 120), (30, 10, 60)),
        "accent": ELECTRIC_PURPLE,
        "char": "podcast",
        "file": "podcast-launch-kit.png"
    },
    {
        "title": "Side Hustle\nIncome Tracker",
        "subtitle": "Track every dollar from side gig to empire",
        "category": "Finance",
        "bg": ((20, 80, 60), (10, 40, 30)),
        "accent": LIME,
        "char": "money",
        "file": "side-hustle.png"
    },
    {
        "title": "Meal Prep\nPlanner",
        "subtitle": "Eat smart, save time, crush your goals",
        "category": "Lifestyle",
        "bg": ((120, 30, 60), (60, 15, 30)),
        "accent": CORAL,
        "char": "cooking",
        "file": "meal-prep.png"
    },
    {
        "title": "Midjourney\nPrompt Pack",
        "subtitle": "500+ prompts to create stunning AI art",
        "category": "AI Tools",
        "bg": ((50, 10, 100), (20, 5, 50)),
        "accent": LAVENDER,
        "char": "artist",
        "file": "midjourney-prompts.png"
    },
    {
        "title": "Student Study\nPlanner",
        "subtitle": "Ace every class with the ultimate study system",
        "category": "Education",
        "bg": ((20, 50, 120), (10, 25, 60)),
        "accent": BABY_BLUE,
        "char": "student",
        "file": "student-study.png"
    },
    {
        "title": "Teacher\nPlanner",
        "subtitle": "Plan, grade, and communicate like a pro",
        "category": "Education",
        "bg": ((20, 80, 70), (10, 40, 35)),
        "accent": TEAL,
        "char": "teacher",
        "file": "teacher-planner.png"
    },
    {
        "title": "Wedding\nPlanner",
        "subtitle": "Plan your dream day without the stress",
        "category": "Life Events",
        "bg": ((120, 20, 80), (60, 10, 40)),
        "accent": HOT_PINK,
        "char": "wedding",
        "file": "wedding-planning.png"
    },
    {
        "title": "Invoice\nGenerator",
        "subtitle": "Professional invoices in seconds",
        "category": "Business",
        "bg": ((30, 30, 60), (15, 15, 30)),
        "accent": TEAL,
        "char": "business",
        "file": "invoice-generator.png"
    },
    {
        "title": "Product Launch\nPlaybook",
        "subtitle": "Launch with confidence, scale with data",
        "category": "Business",
        "bg": ((100, 20, 30), (50, 10, 15)),
        "accent": BRIGHT_ORANGE,
        "char": "rocket",
        "file": "product-launch.png"
    },
    {
        "title": "Client Proposal\nTemplate",
        "subtitle": "Win clients with polished proposals",
        "category": "Business",
        "bg": ((30, 40, 80), (15, 20, 40)),
        "accent": LAVENDER,
        "char": "proposal",
        "file": "client-proposal.png"
    },
    {
        "title": "Content\nCalendar",
        "subtitle": "30 days of content, planned and ready to post",
        "category": "Social Media",
        "bg": ((100, 20, 80), (50, 10, 40)),
        "accent": HOT_PINK,
        "char": "calendar",
        "file": "content-calendar.png"
    },
    {
        "title": "Social Media\nBundle",
        "subtitle": "200+ templates for every platform",
        "category": "Marketing",
        "bg": ((80, 20, 100), (40, 10, 50)),
        "accent": CORAL,
        "char": "selfie",
        "file": "social-media-bundle.png"
    },
    {
        "title": "AI Productivity\nStarter Kit",
        "subtitle": "Work smarter with AI-powered workflows",
        "category": "AI Tools",
        "bg": ((15, 15, 50), (40, 15, 70)),
        "accent": MINT,
        "char": "ai",
        "file": "ai-productivity-kit.png"
    },
    {
        "title": "Budget\nPlanner",
        "subtitle": "Take control of your money, one week at a time",
        "category": "Finance",
        "bg": ((20, 60, 40), (10, 30, 20)),
        "accent": NEON_YELLOW,
        "char": "piggybank",
        "file": "budget-planner.png"
    },
    {
        "title": "Fitness\nTracker",
        "subtitle": "Crush your fitness goals with daily tracking",
        "category": "Health & Wellness",
        "bg": ((100, 20, 40), (50, 10, 20)),
        "accent": BRIGHT_ORANGE,
        "char": "fitness",
        "file": "fitness-tracker.png"
    },
    {
        "title": "Resume\nBuilder",
        "subtitle": "Land your dream job with a standout resume",
        "category": "Career",
        "bg": ((30, 30, 70), (15, 15, 35)),
        "accent": BABY_BLUE,
        "char": "resume",
        "file": "resume-builder.png"
    },
]


if __name__ == "__main__":
    print(f"Generating {len(covers)} 90s-vibe covers with cartoon characters...")
    for c in covers:
        generate_90s_cover(
            title=c["title"],
            subtitle=c["subtitle"],
            category=c["category"],
            bg_colors=c["bg"],
            accent=c["accent"],
            char_type=c["char"],
            filename=c["file"]
        )
    print(f"\nDone! {len(covers)} covers generated in {OUT_DIR}/")
