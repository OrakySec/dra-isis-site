import os
from PIL import Image

orig_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_perfect.jpg'

try:
    with Image.open(orig_path) as img:
        w, h = img.size # 809 x 1024
        
        # Perfect Symmetrical Crop (Exactly half width = 404px each)
        # Left Image (Antes):
        # We want the left half. Crop y=0 to 460 to perfectly avoid "PÓS IMEDIATO" at the bottom.
        left_buttock = img.crop((0, 0, 404, 460))
        
        # Right Image (Depois):
        # We want the right half. Crop y=560 to 1020 to align the buttock vertically and avoid any stray arrow lines at the top.
        right_buttock = img.crop((809 - 404, 560, 809, 1020))
        
        # Canvas: 808 x 460
        canvas = Image.new('RGB', (808, 460), (35, 36, 45))
        canvas.paste(left_buttock, (0, 0))
        canvas.paste(right_buttock, (404, 0))
        
        canvas.save(dest_path, quality=100)
        print("Success! Created bumbum_perfect.jpg")
except Exception as e:
    print("Error:", e)

# Update HTML to use bumbum_perfect.jpg
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Match any img tag for bumbum gold card image
target_pattern = r'<img src="assets/images/bumbum_[^"]+"[^>]*class="service-card__image"[^>]*>'
replacement = '<img src="assets/images/bumbum_perfect.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image">'

html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use bumbum_perfect.jpg")
