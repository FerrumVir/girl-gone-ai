#!/usr/bin/env python3
"""Generate 5 Girl Gone AI logos as 1200x1200 PNGs for Google Ads."""

from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1200
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
OUT_DIR = os.path.join(os.path.dirname(__file__), "logos")
os.makedirs(OUT_DIR, exist_ok=True)


def gradient_fill(draw, shape, color1, color2, direction="vertical"):
    """Fill image with a vertical or diagonal gradient."""
    img = draw._image
    w, h = img.size
    for y in range(h):
        ratio = y / h
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))


def draw_bolt(draw, cx, cy, scale=1.0, color=(255, 59, 139), outline=None):
    """Draw a lightning bolt polygon centered at (cx, cy)."""
    # Bolt shape points (relative to center, normalized to ~300px tall at scale=1)
    points = [
        (25, -150),   # top
        (-45, -15),   # left notch top
        (-5, -15),    # inner notch top
        (-25, 150),   # bottom
        (45, 15),     # right notch bottom
        (5, 15),      # inner notch bottom
    ]
    scaled = [(cx + p[0] * scale, cy + p[1] * scale) for p in points]
    draw.polygon(scaled, fill=color, outline=outline)
    return scaled


def draw_bolt_gradient(img, cx, cy, scale=1.0, color_top=(255, 59, 139), color_bot=(59, 130, 246)):
    """Draw a lightning bolt with vertical gradient fill."""
    # Create bolt mask
    mask = Image.new("L", img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    points = [
        (25, -150), (-45, -15), (-5, -15),
        (-25, 150), (45, 15), (5, 15),
    ]
    scaled = [(cx + p[0] * scale, cy + p[1] * scale) for p in points]
    mask_draw.polygon(scaled, fill=255)

    # Create gradient image
    grad = Image.new("RGBA", img.size)
    grad_draw = ImageDraw.Draw(grad)
    min_y = min(p[1] for p in scaled)
    max_y = max(p[1] for p in scaled)
    for y in range(img.size[1]):
        if min_y <= y <= max_y:
            ratio = (y - min_y) / (max_y - min_y) if max_y > min_y else 0
            r = int(color_top[0] + (color_bot[0] - color_top[0]) * ratio)
            g = int(color_top[1] + (color_bot[1] - color_top[1]) * ratio)
            b = int(color_top[2] + (color_bot[2] - color_top[2]) * ratio)
            grad_draw.line([(0, y), (img.size[0], y)], fill=(r, g, b, 255))

    # Apply mask
    grad.putalpha(mask)
    img.paste(grad, (0, 0), grad)
    return scaled


def draw_text_centered(draw, text, y, font, fill):
    """Draw text centered horizontally."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (SIZE - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)


def draw_glow(img, cx, cy, radius, color, alpha=80):
    """Draw a soft radial glow."""
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for r in range(radius, 0, -2):
        a = int(alpha * (r / radius) ** 0.5 * (1 - r / radius))
        glow_draw.ellipse(
            [cx - r, cy - r, cx + r, cy + r],
            fill=(color[0], color[1], color[2], max(0, a))
        )
    img.paste(Image.alpha_composite(Image.new("RGBA", img.size, (0, 0, 0, 0)), glow), (0, 0), glow)


def logo1_current_website_retro():
    """Logo 1: Hot pink bolt on dark purple-to-black gradient."""
    img = Image.new("RGBA", (SIZE, SIZE))
    draw = ImageDraw.Draw(img)

    # Purple to black gradient background
    for y in range(SIZE):
        ratio = y / SIZE
        r = int(45 * (1 - ratio))
        g = int(27 * (1 - ratio))
        b = int(105 * (1 - ratio))
        draw.line([(0, y), (SIZE, y)], fill=(r, g, b, 255))

    # Glow behind bolt
    draw_glow(img, SIZE // 2, SIZE // 2 - 60, 350, (255, 59, 139), alpha=60)
    draw = ImageDraw.Draw(img)

    # Lightning bolt
    draw_bolt(draw, SIZE // 2, SIZE // 2 - 60, scale=2.2, color=(255, 59, 139))

    # Subtle bolt outline
    points = [
        (25, -150), (-45, -15), (-5, -15),
        (-25, 150), (45, 15), (5, 15),
    ]
    scaled = [(SIZE // 2 + p[0] * 2.2, SIZE // 2 - 60 + p[1] * 2.2) for p in points]
    draw.polygon(scaled, outline=(255, 255, 255, 60))

    # Text
    font_main = ImageFont.truetype(FONT_BOLD, 72)
    font_tag = ImageFont.truetype(FONT_REG, 24)
    draw_text_centered(draw, "Girl Gone AI", SIZE // 2 + 290, font_main, (255, 255, 255))
    draw_text_centered(draw, "Smart Girl Energy Meets Artificial Intelligence",
                       SIZE // 2 + 370, font_tag, (59, 130, 246))

    img.save(os.path.join(OUT_DIR, "logo1-current-website-retro.png"))
    print("Logo 1 saved")


def logo2_nerdy_classy_gradient():
    """Logo 2: Gradient bolt on clean white background."""
    img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Gradient bolt (pink to blue)
    draw_bolt_gradient(img, SIZE // 2, SIZE // 2 - 80, scale=2.2,
                       color_top=(255, 59, 139), color_bot=(59, 130, 246))

    # Drop shadow for bolt (subtle)
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    points = [
        (25, -150), (-45, -15), (-5, -15),
        (-25, 150), (45, 15), (5, 15),
    ]
    scaled = [(SIZE // 2 + 6 + p[0] * 2.2, SIZE // 2 - 74 + p[1] * 2.2) for p in points]
    sdraw.polygon(scaled, fill=(0, 0, 0, 30))
    img_with_shadow = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 255))
    img_with_shadow.paste(shadow, (0, 0), shadow)
    # Re-draw gradient bolt on top
    draw_bolt_gradient(img_with_shadow, SIZE // 2, SIZE // 2 - 80, scale=2.2,
                       color_top=(255, 59, 139), color_bot=(59, 130, 246))
    img = img_with_shadow

    draw = ImageDraw.Draw(img)
    font_main = ImageFont.truetype(FONT_BOLD, 72)
    draw_text_centered(draw, "Girl Gone AI", SIZE // 2 + 280, font_main, (168, 85, 247))

    img.save(os.path.join(OUT_DIR, "logo2-nerdy-classy-gradient.png"))
    print("Logo 2 saved")


def logo3_neon_sassy_badge():
    """Logo 3: Circular neon badge on deep navy."""
    img = Image.new("RGBA", (SIZE, SIZE), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)

    cx, cy = SIZE // 2, SIZE // 2
    badge_r = 450

    # Glow behind badge
    draw_glow(img, cx, cy, 500, (59, 130, 246), alpha=40)
    draw = ImageDraw.Draw(img)

    # Badge ring (electric blue glow)
    for i in range(6):
        r = badge_r + 3 - i
        alpha = 255 - i * 40
        draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                     outline=(59, 130, 246, max(alpha, 60)), width=2)

    # Inner fill (slightly lighter navy)
    draw.ellipse([cx - badge_r + 10, cy - badge_r + 10,
                  cx + badge_r - 10, cy + badge_r - 10],
                 fill=(20, 30, 55, 255))

    # Neon bolt with glow
    draw_glow(img, cx, cy + 20, 250, (255, 59, 139), alpha=70)
    draw = ImageDraw.Draw(img)
    draw_bolt(draw, cx, cy + 20, scale=1.8, color=(255, 59, 139))

    # "GIRL GONE AI" arc text (simplified as straight text above bolt)
    font_arc = ImageFont.truetype(FONT_BOLD, 64)
    text = "GIRL GONE AI"
    # Draw as arc approximation
    total_angle = 120  # degrees of arc
    start_angle = -90 - total_angle // 2
    r_text = badge_r - 80
    for i, ch in enumerate(text):
        angle_deg = start_angle + (total_angle / (len(text) - 1)) * i
        angle_rad = math.radians(angle_deg)
        tx = cx + r_text * math.cos(angle_rad)
        ty = cy + r_text * math.sin(angle_rad)
        # Rotate each character
        char_img = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((5, 5), ch, font=font_arc, fill=(255, 255, 255))
        rotated = char_img.rotate(-angle_deg - 90, expand=True, resample=Image.BICUBIC)
        paste_x = int(tx - rotated.width // 2)
        paste_y = int(ty - rotated.height // 2)
        img.paste(rotated, (paste_x, paste_y), rotated)

    # Sparkle accents
    draw = ImageDraw.Draw(img)
    sparkle_color = (168, 85, 247, 200)
    for sx, sy, sr in [(cx - 180, cy + 40, 6), (cx + 180, cy + 40, 6),
                        (cx - 120, cy - 100, 4), (cx + 120, cy - 100, 4)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=sparkle_color)
        # Cross sparkle
        draw.line([(sx - sr * 2, sy), (sx + sr * 2, sy)], fill=sparkle_color, width=2)
        draw.line([(sx, sy - sr * 2), (sx, sy + sr * 2)], fill=sparkle_color, width=2)

    img.save(os.path.join(OUT_DIR, "logo3-neon-sassy-badge.png"))
    print("Logo 3 saved")


def logo4_pastel_soft_glow():
    """Logo 4: Pastel pink bolt on soft lavender."""
    img = Image.new("RGBA", (SIZE, SIZE), (243, 232, 255, 255))
    draw = ImageDraw.Draw(img)

    cx, cy = SIZE // 2, SIZE // 2 - 60

    # Soft glow behind bolt
    draw_glow(img, cx, cy, 350, (255, 179, 217), alpha=50)
    draw = ImageDraw.Draw(img)

    # Pastel pink bolt
    draw_bolt(draw, cx, cy, scale=2.2, color=(255, 179, 217))

    # Soft inner highlight
    points = [
        (25, -150), (-45, -15), (-5, -15),
    ]
    highlight = [(cx + p[0] * 2.2, cy + p[1] * 2.2) for p in points]
    draw.polygon(highlight, fill=(255, 210, 235, 120))

    # Sparkle dots (pale gold)
    sparkle = (255, 223, 160, 180)
    for sx, sy, sr in [(cx - 160, cy - 180, 5), (cx + 170, cy - 120, 4),
                        (cx - 130, cy + 200, 3), (cx + 150, cy + 180, 5),
                        (cx + 80, cy - 250, 3), (cx - 200, cy + 50, 4)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=sparkle)

    # Text
    font_main = ImageFont.truetype(FONT_BOLD, 68)
    draw_text_centered(draw, "Girl Gone AI", SIZE // 2 + 290, font_main, (124, 58, 237))

    img.save(os.path.join(OUT_DIR, "logo4-pastel-soft-glow.png"))
    print("Logo 4 saved")


def logo5_bold_block_stack():
    """Logo 5: GGA monogram on black."""
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    cx, cy = SIZE // 2, SIZE // 2

    # Large GGA letters
    font_gga = ImageFont.truetype(FONT_BOLD, 320)
    text = "GGA"
    bbox = draw.textbbox((0, 0), text, font=font_gga)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) // 2
    ty = (SIZE - th) // 2 - 80
    draw.text((tx, ty), text, font=font_gga, fill=(255, 59, 139))

    # Small lightning bolt in the A crossbar area
    # Approximate A position: rightmost third of the text
    a_cx = tx + tw - 80
    a_cy = ty + th // 2 + 30
    # Tiny bolt
    bolt_points = [
        (a_cx + 8, a_cy - 30),
        (a_cx - 8, a_cy),
        (a_cx + 2, a_cy),
        (a_cx - 8, a_cy + 30),
        (a_cx + 8, a_cy),
        (a_cx - 2, a_cy),
    ]
    draw.polygon(bolt_points, fill=(59, 130, 246))

    # "Girl Gone AI" text below
    font_sub = ImageFont.truetype(FONT_REG, 40)
    # Wide tracking
    sub_text = "G I R L   G O N E   A I"
    draw_text_centered(draw, sub_text, ty + th + 40, font_sub, (59, 130, 246))

    img.save(os.path.join(OUT_DIR, "logo5-bold-block-stack.png"))
    print("Logo 5 saved")


if __name__ == "__main__":
    logo1_current_website_retro()
    logo2_nerdy_classy_gradient()
    logo3_neon_sassy_badge()
    logo4_pastel_soft_glow()
    logo5_bold_block_stack()
    print(f"\nAll 5 logos saved to {OUT_DIR}/")
    for f in sorted(os.listdir(OUT_DIR)):
        if f.endswith(".png"):
            path = os.path.join(OUT_DIR, f)
            size = os.path.getsize(path)
            print(f"  {f} ({size // 1024}KB)")
