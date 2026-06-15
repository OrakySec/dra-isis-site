import os
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
antes_dest = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_antes.jpg'
depois_dest = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        # cleanly split into top and bottom without shifting anything
        top_img = img.crop((0, 0, width, 540))
        bottom_img = img.crop((0, 540, width, 1024))
        
        top_img.save(antes_dest, quality=95)
        bottom_img.save(depois_dest, quality=95)
        print("Success! Split into antes and depois cleanly.")
except Exception as e:
    print("Error:", e)

# Update index.html to use CSS Flexbox
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re

# find the bumbum image in index.html and replace it with the flex container
target_pattern = r'<img src="assets/images/bumbum_up_gold_antes_depois\.jpg"[^>]*>'
replacement = '''<div style="display: flex; height: 200px; width: 100%;">
            <img src="assets/images/bumbum_antes.jpg" alt="Antes" style="width: 50%; height: 100%; object-fit: cover; object-position: right bottom;">
            <img src="assets/images/bumbum_depois.jpg" alt="Depois" style="width: 50%; height: 100%; object-fit: cover; object-position: left center; border-left: 1px solid rgba(255,255,255,0.1);">
          </div>'''

html = re.sub(target_pattern, replacement, html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use CSS flexbox layout")
