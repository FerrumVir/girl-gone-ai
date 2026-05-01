#!/usr/bin/env python3
"""Generate a Facebook page cover banner for Girl Gone AI."""

from PIL import Image, ImageDraw, ImageFont
import math
import os
import random

# Facebook cover: 820x312 desktop, we generate 2x for retina
W, H = 1640, 624

# Brand colors from the website
BG_DARK = (26, 26, 46)        # #1a1a2e
HOT_PINK = (255, 59, 139)     # #FF3B8B
PURPLE = (168, 85, 247)       # #A855F7
CYAN = (0, 200, 220)          # teal/cyan accent
YELLOW = (255, 230, 0)        # yellow accent
WHITE = (255, 255, 255)
DARK_PURPLE = (40, 20, 60)
MAGENTA_BG = (80, 10, 50)

BASE = os.path.dirname(os.path.abspath(__file__))

def make_gradient_bg(img):
    """Create dark purple gradient background."""
    draw = ImageDraw.Draw(img)
    for y in range(H):
        r = int(26 + (80 - 26) * (y / H) * 0.3)
        g = int(26 + (10 - 26) * (y / H) * 0.3)
        b = int(46 + (60 - 46) * (y / H) * 0.3)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

def draw_diagonal_stripes(draw, x, y, w, h, color, stripe_w=8, gap=12):
    """Draw diagonal stripe pattern in a region."""
    for i in range(-h, w + h, stripe_w + gap):
        draw.line([(x + i, y), (x + i - h, y + h)], fill=color, width=stripe_w)

def draw_dot_grid(draw, x0, y0, x1, y1, color, spacing=20, radius=2):
    """Draw a grid of dots."""
    for x in range(x0, x1, spacing):
        for y in range(y0, y1, spacing):
            draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)

def draw_diamond(draw, cx, cy, size, color):
    """Draw a diamond shape."""
    draw.polygon([
        (cx, cy - size), (cx + size, cy),
        (cx, cy + size), (cx - size, cy)
    ], outline=color, width=2)

def draw_cross(draw, cx, cy, size, color, width=2):
    """Draw a plus/cross."""
    draw.line([(cx - size, cy), (cx + size, cy)], fill=color, width=width)
    draw.line([(cx, cy - size), (cx, cy + size)], fill=color, width=width)

def draw_wave(draw, x0, y0, length, amplitude, color, width=3):
    """Draw a sine wave."""
    points = []
    for i in range(length):
        x = x0 + i
        y = y0 + int(amplitude * math.sin(i * 0.05))
        points.append((x, y))
    if len(points) > 1:
        draw.line(points, fill=color, width=width)

def draw_sparkle(draw, cx, cy, size, color):
    """Draw a 4-point sparkle."""
    draw.line([(cx, cy - size), (cx, cy + size)], fill=color, width=2)
    draw.line([(cx - size, cy), (cx + size, cy)], fill=color, width=2)
    s2 = int(size * 0.5)
    draw.line([(cx - s2, cy - s2), (cx + s2, cy + s2)], fill=color, width=1)
    draw.line([(cx + s2, cy - s2), (cx - s2, cy + s2)], fill=color, width=1)

def load_font(name, size):
    """Try to load a font, fall back to default."""
    paths = [
        f"/usr/share/fonts/truetype/{name}",
        f"/usr/share/fonts/{name}",
        f"/usr/local/share/fonts/{name}",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    try:
        return ImageFont.truetype(name, size)
    except:
        return ImageFont.load_default()

def main():
    random.seed(42)  # Reproducible
    img = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # 1. Gradient background
    make_gradient_bg(img)
    draw = ImageDraw.Draw(img)

    # 2. Hot pink border (thin)
    border = 6
    draw.rectangle([0, 0, W - 1, H - 1], outline=HOT_PINK, width=border)

    # 3. Diagonal stripes - top left corner
    stripe_region = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sr_draw = ImageDraw.Draw(stripe_region)
    draw_diagonal_stripes(sr_draw, 0, 0, 300, 120, HOT_PINK + (100,), stripe_w=10, gap=14)
    img.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), stripe_region).convert("RGB"),
              mask=stripe_region.split()[3])

    # Diagonal stripes - top right corner
    stripe_region2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sr_draw2 = ImageDraw.Draw(stripe_region2)
    draw_diagonal_stripes(sr_draw2, W - 300, 0, 300, 120, HOT_PINK + (100,), stripe_w=10, gap=14)
    img.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), stripe_region2).convert("RGB"),
              mask=stripe_region2.split()[3])

    draw = ImageDraw.Draw(img)

    # 4. Dot grid pattern in center-left area
    dot_color = (255, 59, 139, 60)
    for x in range(100, 500, 18):
        for y in range(200, 500, 18):
            alpha = random.randint(30, 80)
            draw.ellipse([x - 2, y - 2, x + 2, y + 2],
                         fill=(255, 59, 139))

    # 5. Geometric accents
    # Cyan crosses
    for cx, cy in [(80, 300), (1550, 150), (1500, 480), (200, 550)]:
        draw_cross(draw, cx, cy, 15, CYAN, 3)

    # Cyan diamonds
    for cx, cy in [(120, 450), (1400, 100), (1580, 350)]:
        draw_diamond(draw, cx, cy, 12, CYAN)

    # White sparkles / dots scattered
    for _ in range(30):
        x = random.randint(50, W - 50)
        y = random.randint(50, H - 50)
        s = random.randint(2, 4)
        draw.ellipse([x - s, y - s, x + s, y + s], fill=(255, 255, 255, 150))

    # 6. Yellow wave - top left area
    draw_wave(draw, 60, 180, 250, 20, YELLOW, 3)

    # Cyan wave - bottom right
    draw_wave(draw, 1300, 520, 280, 15, CYAN, 3)

    # Magenta wave - bottom left
    draw_wave(draw, 50, 540, 200, 12, HOT_PINK, 2)

    # 7. Main text area - centered
    # Try to use Poppins or a bold sans-serif
    try:
        font_brand_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
        font_tagline = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        font_retro = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    except:
        font_brand_large = ImageFont.load_default()
        font_tagline = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_retro = ImageFont.load_default()

    # Draw semi-transparent panel behind text
    panel_x0, panel_y0 = 380, 100
    panel_x1, panel_y1 = 1260, 520
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle([panel_x0, panel_y0, panel_x1, panel_y1],
                                  radius=20, fill=(40, 10, 50, 160))
    img = Image.alpha_composite(img.convert("RGBA"), panel).convert("RGB")
    draw = ImageDraw.Draw(img)

    # "GIRL GONE AI" - main brand text
    brand_text = "GIRL GONE AI"
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand_large)
    tw = bbox[2] - bbox[0]
    tx = (W - tw) // 2
    ty = 150

    # Text shadow/glow
    for ox, oy in [(3, 3), (-1, -1), (2, 0), (0, 2)]:
        draw.text((tx + ox, ty + oy), brand_text, fill=(168, 85, 247), font=font_brand_large)
    draw.text((tx, ty), brand_text, fill=WHITE, font=font_brand_large)

    # Tagline
    tagline = "Smart Girl Energy Meets AI"
    bbox2 = draw.textbbox((0, 0), tagline, font=font_tagline)
    tw2 = bbox2[2] - bbox2[0]
    tx2 = (W - tw2) // 2
    ty2 = ty + 140
    draw.text((tx2, ty2), tagline, fill=HOT_PINK, font=font_tagline)

    # Sub text
    sub_text = "Digital Products  |  Templates  |  Planners  |  AI Tools"
    bbox3 = draw.textbbox((0, 0), sub_text, font=font_sub)
    tw3 = bbox3[2] - bbox3[0]
    tx3 = (W - tw3) // 2
    ty3 = ty2 + 70
    draw.text((tx3, ty3), sub_text, fill=(200, 200, 220), font=font_sub)

    # Website URL
    url_text = "girlgone.ai"
    bbox4 = draw.textbbox((0, 0), url_text, font=font_sub)
    tw4 = bbox4[2] - bbox4[0]
    tx4 = (W - tw4) // 2
    ty4 = ty3 + 60
    draw.text((tx4, ty4), url_text, fill=CYAN, font=font_sub)

    # 8. Product thumbnails along left and right edges
    covers_dir = os.path.join(BASE, "covers2")
    cover_files = sorted([f for f in os.listdir(covers_dir) if f.endswith(".png")])
    thumb_size = 140

    # Left side - 3 product thumbnails stacked
    left_covers = cover_files[:3]
    for i, cf in enumerate(left_covers):
        try:
            cimg = Image.open(os.path.join(covers_dir, cf))
            cimg = cimg.resize((thumb_size, int(thumb_size * 0.56)), Image.LANCZOS)
            # Add pink border
            bordered = Image.new("RGB", (cimg.width + 6, cimg.height + 6), HOT_PINK)
            bordered.paste(cimg, (3, 3))
            # Slight rotation
            angle = random.choice([-8, -5, 5, 8])
            bordered = bordered.rotate(angle, expand=True, fillcolor=BG_DARK)
            x = 30 + i * 20
            y = 150 + i * (cimg.height + 30)
            img.paste(bordered, (x, y))
        except Exception:
            pass

    # Right side - 3 product thumbnails
    right_covers = cover_files[3:6]
    for i, cf in enumerate(right_covers):
        try:
            cimg = Image.open(os.path.join(covers_dir, cf))
            cimg = cimg.resize((thumb_size, int(thumb_size * 0.56)), Image.LANCZOS)
            bordered = Image.new("RGB", (cimg.width + 6, cimg.height + 6), HOT_PINK)
            bordered.paste(cimg, (3, 3))
            angle = random.choice([-8, -5, 5, 8])
            bordered = bordered.rotate(angle, expand=True, fillcolor=BG_DARK)
            x = W - bordered.width - 30 - i * 20
            y = 150 + i * (cimg.height + 30)
            img.paste(bordered, (x, y))
        except Exception:
            pass

    draw = ImageDraw.Draw(img)

    # 9. Bottom bar - "90s EDITION" style
    draw.rectangle([0, H - 50, W, H], fill=(10, 5, 20))
    draw.rectangle([0, H - 50, W, H - 48], fill=HOT_PINK)

    # Retro label left
    draw.rounded_rectangle([20, H - 44, 220, H - 8], radius=4, fill=HOT_PINK)
    draw.text((32, H - 42), "90s EDITION", fill=BG_DARK, font=font_retro)

    # Dots
    for i in range(5):
        dx = 240 + i * 18
        dy = H - 26
        draw.ellipse([dx - 5, dy - 5, dx + 5, dy + 5], fill=YELLOW)

    # Retro label right
    draw.rounded_rectangle([W - 200, H - 44, W - 20, H - 8], radius=4, fill=HOT_PINK)
    draw.text((W - 190, H - 42), "WORD UP", fill=BG_DARK, font=font_retro)

    # 10. Lightning bolt icon near the brand (like the logo)
    bolt_cx, bolt_cy = W // 2 - 240, 220
    bolt_points = [
        (bolt_cx + 20, bolt_cy - 40),
        (bolt_cx - 5, bolt_cy + 5),
        (bolt_cx + 8, bolt_cy + 5),
        (bolt_cx - 10, bolt_cy + 50),
        (bolt_cx + 25, bolt_cy - 5),
        (bolt_cx + 12, bolt_cy - 5),
    ]
    draw.polygon(bolt_points, fill=HOT_PINK)

    # Another bolt on right side
    bolt_cx2 = W // 2 + 240
    bolt_points2 = [
        (bolt_cx2 + 20, bolt_cy - 40),
        (bolt_cx2 - 5, bolt_cy + 5),
        (bolt_cx2 + 8, bolt_cy + 5),
        (bolt_cx2 - 10, bolt_cy + 50),
        (bolt_cx2 + 25, bolt_cy - 5),
        (bolt_cx2 + 12, bolt_cy - 5),
    ]
    draw.polygon(bolt_points2, fill=HOT_PINK)

    # 11. Save
    out_path = os.path.join(BASE, "facebook-banner.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Banner saved: {out_path}")
    print(f"Size: {W}x{H} (retina 2x of 820x312)")

    # Also save 1x version
    img_1x = img.resize((820, 312), Image.LANCZOS)
    out_1x = os.path.join(BASE, "facebook-banner-820.png")
    img_1x.save(out_1x, "PNG", optimize=True)
    print(f"1x version saved: {out_1x}")

if __name__ == "__main__":
    main()
