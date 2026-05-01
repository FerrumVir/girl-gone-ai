#!/usr/bin/env python3
"""Generate social media banners/graphics for all platforms for Girl Gone AI."""

from PIL import Image, ImageDraw, ImageFont
import math
import os
import random

# Brand colors
BG_DARK = (26, 26, 46)
HOT_PINK = (255, 59, 139)
PURPLE = (168, 85, 247)
CYAN = (0, 200, 220)
YELLOW = (255, 230, 0)
WHITE = (255, 255, 255)

BASE = os.path.dirname(os.path.abspath(__file__))

# Platform specs: (width, height, description)
PLATFORMS = {
    "facebook": [
        (820, 312, "cover"),
        (1200, 630, "post"),
    ],
    "instagram": [
        (1080, 1080, "post"),
        (1080, 1920, "story"),
    ],
    "tiktok": [
        (1080, 1920, "cover"),
    ],
    "twitter": [
        (1500, 500, "header"),
        (1200, 675, "post"),
    ],
    "youtube": [
        (2560, 1440, "banner"),
        (1280, 720, "thumbnail"),
    ],
    "pinterest": [
        (1000, 1500, "pin"),
    ],
    "linkedin": [
        (1128, 191, "cover"),
        (1200, 627, "post"),
    ],
}


def load_font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def load_font_regular(size):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def make_gradient_bg(draw, w, h):
    for y in range(h):
        r = int(26 + (80 - 26) * (y / h) * 0.3)
        g = int(26 + (10 - 26) * (y / h) * 0.3)
        b = int(46 + (60 - 46) * (y / h) * 0.3)
        draw.line([(0, y), (w, y)], fill=(r, g, b))


def draw_wave(draw, x0, y0, length, amplitude, color, width=3):
    points = []
    for i in range(length):
        x = x0 + i
        y = y0 + int(amplitude * math.sin(i * 0.05))
        points.append((x, y))
    if len(points) > 1:
        draw.line(points, fill=color, width=width)


def draw_cross(draw, cx, cy, size, color, width=2):
    draw.line([(cx - size, cy), (cx + size, cy)], fill=color, width=width)
    draw.line([(cx, cy - size), (cx, cy + size)], fill=color, width=width)


def draw_diamond(draw, cx, cy, size, color):
    draw.polygon([
        (cx, cy - size), (cx + size, cy),
        (cx, cy + size), (cx - size, cy)
    ], outline=color, width=2)


def generate_banner(w, h, platform, variant):
    random.seed(42)
    img = Image.new("RGB", (w, h), BG_DARK)
    draw = ImageDraw.Draw(img)
    make_gradient_bg(draw, w, h)
    draw = ImageDraw.Draw(img)

    # Border
    border = max(2, min(6, w // 300))
    draw.rectangle([0, 0, w - 1, h - 1], outline=HOT_PINK, width=border)

    # Scale factor relative to the FB banner (1640x624)
    scale = min(w / 1640, h / 624)
    scale = max(scale, 0.15)

    # Scattered dots
    for _ in range(max(10, int(30 * scale))):
        x = random.randint(50, w - 50)
        y = random.randint(50, h - 50)
        s = random.randint(2, max(3, int(4 * scale)))
        draw.ellipse([x - s, y - s, x + s, y + s], fill=WHITE)

    # Crosses and diamonds
    for _ in range(max(2, int(4 * scale))):
        cx = random.randint(int(w * 0.05), int(w * 0.95))
        cy = random.randint(int(h * 0.05), int(h * 0.95))
        draw_cross(draw, cx, cy, int(15 * scale), CYAN, max(2, int(3 * scale)))

    for _ in range(max(1, int(3 * scale))):
        cx = random.randint(int(w * 0.05), int(w * 0.95))
        cy = random.randint(int(h * 0.05), int(h * 0.95))
        draw_diamond(draw, cx, cy, int(12 * scale), CYAN)

    # Waves
    wave_len = min(250, w // 3)
    draw_wave(draw, int(w * 0.04), int(h * 0.3), wave_len, int(20 * scale), YELLOW, max(2, int(3 * scale)))
    draw_wave(draw, int(w * 0.7), int(h * 0.85), wave_len, int(15 * scale), CYAN, max(2, int(3 * scale)))

    # Semi-transparent text panel
    panel_margin_x = int(w * 0.15)
    panel_margin_y = int(h * 0.15)
    # For very wide/short banners (LinkedIn cover), adjust
    if w / h > 4:
        panel_margin_x = int(w * 0.25)
        panel_margin_y = int(h * 0.1)

    panel = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle(
        [panel_margin_x, panel_margin_y, w - panel_margin_x, h - panel_margin_y],
        radius=max(5, int(20 * scale)), fill=(40, 10, 50, 160)
    )
    img = Image.alpha_composite(img.convert("RGBA"), panel).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Text sizing
    available_h = h - 2 * panel_margin_y
    available_w = w - 2 * panel_margin_x

    # Brand text
    brand_size = max(16, min(int(available_h * 0.35), int(available_w * 0.08)))
    font_brand = load_font(brand_size)
    brand_text = "GIRL GONE AI"
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    tw = bbox[2] - bbox[0]
    tx = (w - tw) // 2

    # Vertical centering
    total_text_h = brand_size + int(brand_size * 0.5) + int(brand_size * 0.4) + int(brand_size * 0.4)
    ty_start = max(panel_margin_y + 10, (h - total_text_h) // 2 - int(brand_size * 0.2))

    # Shadow + text
    for ox, oy in [(2, 2), (-1, -1)]:
        draw.text((tx + ox, ty_start + oy), brand_text, fill=PURPLE, font=font_brand)
    draw.text((tx, ty_start), brand_text, fill=WHITE, font=font_brand)

    # Tagline
    tagline_size = max(12, int(brand_size * 0.35))
    font_tagline = load_font_regular(tagline_size)
    tagline = "Smart Girl Energy Meets AI"
    bbox2 = draw.textbbox((0, 0), tagline, font=font_tagline)
    tw2 = bbox2[2] - bbox2[0]
    ty2 = ty_start + brand_size + int(brand_size * 0.15)
    draw.text(((w - tw2) // 2, ty2), tagline, fill=HOT_PINK, font=font_tagline)

    # Sub text
    sub_size = max(10, int(brand_size * 0.25))
    font_sub = load_font_regular(sub_size)
    sub_text = "Digital Products | Templates | Planners | AI Tools"
    bbox3 = draw.textbbox((0, 0), sub_text, font=font_sub)
    tw3 = bbox3[2] - bbox3[0]
    ty3 = ty2 + tagline_size + int(brand_size * 0.12)
    if tw3 < available_w:
        draw.text(((w - tw3) // 2, ty3), sub_text, fill=(200, 200, 220), font=font_sub)

    # URL
    url_size = max(10, int(brand_size * 0.25))
    font_url = load_font_regular(url_size)
    url_text = "girlgone.ai"
    bbox4 = draw.textbbox((0, 0), url_text, font=font_url)
    tw4 = bbox4[2] - bbox4[0]
    ty4 = ty3 + sub_size + int(brand_size * 0.12)
    if ty4 + url_size < h - panel_margin_y:
        draw.text(((w - tw4) // 2, ty4), url_text, fill=CYAN, font=font_url)

    # Product thumbnails on sides (skip for very small or narrow banners)
    if w >= 800 and h >= 300 and w / h < 4:
        covers_dir = os.path.join(BASE, "covers2")
        if os.path.isdir(covers_dir):
            cover_files = sorted([f for f in os.listdir(covers_dir) if f.endswith(".png")])
            thumb_size = max(60, int(min(w, h) * 0.15))
            # Left side
            for i, cf in enumerate(cover_files[:3]):
                try:
                    cimg = Image.open(os.path.join(covers_dir, cf))
                    cimg = cimg.resize((thumb_size, int(thumb_size * 0.56)), Image.LANCZOS)
                    bordered = Image.new("RGB", (cimg.width + 4, cimg.height + 4), HOT_PINK)
                    bordered.paste(cimg, (2, 2))
                    angle = random.choice([-8, -5, 5, 8])
                    bordered = bordered.rotate(angle, expand=True, fillcolor=BG_DARK)
                    x = 20 + i * 15
                    y = int(h * 0.2) + i * (cimg.height + 20)
                    if y + bordered.height < h - 10:
                        img.paste(bordered, (x, y))
                except Exception:
                    pass
            # Right side
            for i, cf in enumerate(cover_files[3:6]):
                try:
                    cimg = Image.open(os.path.join(covers_dir, cf))
                    cimg = cimg.resize((thumb_size, int(thumb_size * 0.56)), Image.LANCZOS)
                    bordered = Image.new("RGB", (cimg.width + 4, cimg.height + 4), HOT_PINK)
                    bordered.paste(cimg, (2, 2))
                    angle = random.choice([-8, -5, 5, 8])
                    bordered = bordered.rotate(angle, expand=True, fillcolor=BG_DARK)
                    x = w - bordered.width - 20 - i * 15
                    y = int(h * 0.2) + i * (cimg.height + 20)
                    if y + bordered.height < h - 10:
                        img.paste(bordered, (x, y))
                except Exception:
                    pass
            draw = ImageDraw.Draw(img)

    # Bottom bar
    bar_h = max(8, int(h * 0.06))
    draw.rectangle([0, h - bar_h, w, h], fill=(10, 5, 20))
    draw.rectangle([0, h - bar_h, w, h - bar_h + 2], fill=HOT_PINK)

    retro_size = max(10, int(bar_h * 0.6))
    font_retro = load_font(retro_size)
    if bar_h >= 20:
        draw.rounded_rectangle([10, h - bar_h + 4, 10 + int(retro_size * 7), h - 4],
                               radius=3, fill=HOT_PINK)
        draw.text((16, h - bar_h + 5), "90s EDITION", fill=BG_DARK, font=font_retro)

    return img


def main():
    index_lines = ["# Girl Gone AI - Social Media Graphics\n"]
    index_lines.append("Download the graphics you need for each platform.\n")

    for platform, specs in PLATFORMS.items():
        folder = os.path.join(BASE, f"{platform}banner" if platform == "facebook" else f"{platform}-banners")
        if platform == "facebook":
            folder = os.path.join(BASE, "fbbanner")
        os.makedirs(folder, exist_ok=True)

        index_lines.append(f"\n## {platform.title()}\n")
        index_lines.append(f"Folder: `/{os.path.basename(folder)}/`\n")

        for w, h, variant in specs:
            filename = f"{platform}-{variant}-{w}x{h}.png"
            filepath = os.path.join(folder, filename)
            img = generate_banner(w, h, platform, variant)
            img.save(filepath, "PNG", optimize=True)
            print(f"  {platform}/{variant}: {w}x{h} -> {filepath}")

            web_path = f"/{os.path.basename(folder)}/{filename}"
            index_lines.append(f"- **{variant.title()}** ({w}x{h}): [{filename}]({web_path})\n")

    # Write index HTML for easy browsing
    html = generate_index_html()
    index_path = os.path.join(BASE, "social-banners.html")
    with open(index_path, "w") as f:
        f.write(html)
    print(f"\nIndex page: {index_path}")

    # Print summary
    print("\n=== SUMMARY ===")
    for platform, specs in PLATFORMS.items():
        folder_name = "fbbanner" if platform == "facebook" else f"{platform}-banners"
        print(f"\n{platform.upper()}:")
        for w, h, variant in specs:
            filename = f"{platform}-{variant}-{w}x{h}.png"
            print(f"  {variant}: girlgone.ai/{folder_name}/{filename} ({w}x{h})")


def generate_index_html():
    rows = []
    for platform, specs in PLATFORMS.items():
        folder_name = "fbbanner" if platform == "facebook" else f"{platform}-banners"
        for w, h, variant in specs:
            filename = f"{platform}-{variant}-{w}x{h}.png"
            url = f"/{folder_name}/{filename}"
            rows.append(f"""
        <tr>
          <td>{platform.title()}</td>
          <td>{variant.title()}</td>
          <td>{w}x{h}</td>
          <td><a href="{url}" download>{filename}</a></td>
          <td><img src="{url}" style="max-width:200px;max-height:80px;border:1px solid #FF3B8B;border-radius:4px"></td>
        </tr>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Girl Gone AI - Social Media Graphics</title>
<style>
  body {{ background: #1a1a2e; color: #fff; font-family: system-ui, sans-serif; padding: 2rem; }}
  h1 {{ color: #FF3B8B; }}
  table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
  th {{ background: #FF3B8B; color: #1a1a2e; padding: 0.75rem; text-align: left; }}
  td {{ padding: 0.75rem; border-bottom: 1px solid #333; }}
  a {{ color: #00c8dc; }}
  tr:hover {{ background: rgba(168,85,247,0.1); }}
</style>
</head>
<body>
<h1>Girl Gone AI - Social Media Graphics</h1>
<p>Click any filename to download. Right-click the preview to save.</p>
<table>
  <thead><tr><th>Platform</th><th>Type</th><th>Size</th><th>Download</th><th>Preview</th></tr></thead>
  <tbody>{"".join(rows)}
  </tbody>
</table>
</body>
</html>"""


if __name__ == "__main__":
    main()
