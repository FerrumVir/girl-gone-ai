#!/usr/bin/env python3
"""Generate banners (1200x300) and thumbnails (600x600) from /covers2 graphics."""

import os
from PIL import Image

REPO = "/home/boogarweed/girl-gone-ai"
SRC = os.path.join(REPO, "covers2")
HEADERS_DIR = os.path.join(REPO, "headers")
THUMBS_DIR = os.path.join(REPO, "assets", "thumbnails")

os.makedirs(HEADERS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

BANNER_W, BANNER_H = 1200, 300
THUMB_SIZE = 600

for fname in sorted(os.listdir(SRC)):
    if not fname.endswith(".png"):
        continue
    src_path = os.path.join(SRC, fname)
    img = Image.open(src_path)
    w, h = img.size

    # Banner: center-crop to 1200x300 aspect, then resize
    target_ratio = BANNER_W / BANNER_H  # 4:1
    src_ratio = w / h
    if src_ratio > target_ratio:
        # Source is wider — crop width
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        crop_box = (left, 0, left + new_w, h)
    else:
        # Source is taller — crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        crop_box = (0, top, w, top + new_h)
    banner = img.crop(crop_box).resize((BANNER_W, BANNER_H), Image.LANCZOS)
    banner.save(os.path.join(HEADERS_DIR, fname), optimize=True)
    print(f"Banner: {fname}")

    # Thumbnail: center-crop to square, then resize to 600x600
    sq = min(w, h)
    left = (w - sq) // 2
    top = (h - sq) // 2
    thumb = img.crop((left, top, left + sq, top + sq)).resize(
        (THUMB_SIZE, THUMB_SIZE), Image.LANCZOS
    )
    thumb.save(os.path.join(THUMBS_DIR, fname), optimize=True)
    print(f"Thumb:  {fname}")

print(f"\nDone. {len([f for f in os.listdir(HEADERS_DIR) if f.endswith('.png')])} banners in /headers/")
print(f"       {len([f for f in os.listdir(THUMBS_DIR) if f.endswith('.png')])} thumbnails in /assets/thumbnails/")
