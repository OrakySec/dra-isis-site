import os
from PIL import Image

orig_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(orig_path) as img:
        w, h = img.size # 809 x 1024
        
        # We recreate the wide side-by-side layout with empty space in the middle.
        # But we vertically crop to strategically eliminate "PÓS IMEDIATO" which was causing the mobile crop issue,
        # while preserving "CORREÇÃO" and "ESTRUTURAÇÃO" perfectly in the center safe zone.
        
        # Left Image (Antes):
        # Buttock on left, empty space on right.
        # Crop y=0 to 460 to cleanly remove "PÓS IMEDIATO" at the bottom.
        left_img = img.crop((0, 0, w, 460))
        
        # Right Image (Depois):
        # Empty space on left, buttock on right.
        # Crop y=500 to 960 to safely include "ESTRUTURAÇÃO" which is near the top (y=512+).
        right_img = img.crop((0, 500, w, 960))
        
        # Canvas: 1618 x 460
        canvas = Image.new('RGB', (w * 2, 460), (35, 36, 45))
        canvas.paste(left_img, (0, 0))
        canvas.paste(right_img, (w, 0))
        
        canvas.save(dest_path, quality=100)
        print("Success! Created flawlessly balanced bumbum_up_gold_antes_depois.jpg")
except Exception as e:
    print("Error:", e)

# Update HTML to use this image, no CSS hacks needed.
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
target_pattern = r'<img src="assets/images/bumbum_[^"]+"[^>]*class="service-card__image"[^>]*>'
replacement = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">'

html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use the balanced image")
