import os
from PIL import Image
import re

orig_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
antes_dest = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_antes.jpg'
depois_dest = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_depois.jpg'

try:
    with Image.open(orig_path) as img:
        w, h = img.size
        # OVERLAPPING SPLIT: guarantees no text near the center is physically sliced!
        # Top image gets 0 to 560
        top_img = img.crop((0, 0, w, 560))
        # Bottom image gets 460 to 1024
        bottom_img = img.crop((0, 460, w, 1024))
        
        top_img.save(antes_dest, quality=100)
        bottom_img.save(depois_dest, quality=100)
        print("Success! Created overlapping pristine splits.")
except Exception as e:
    print("Error:", e)

# Fix HTML to Flexbox with Optimized object-position
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any single image card with the optimized flexbox
target_pattern = r'<img src="assets/images/bumbum_up_gold_antes_depois\.jpg"[^>]*>'
replacement = '''<div class="bumbum-flex-container" style="display: flex; height: 200px; width: 100%;">
            <img src="assets/images/bumbum_antes.jpg" alt="Antes" style="width: 50%; height: 100%; object-fit: cover; object-position: 85% bottom;">
            <img src="assets/images/bumbum_depois.jpg" alt="Depois" style="width: 50%; height: 100%; object-fit: cover; object-position: left 5%;">
          </div>'''

html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML with Optimized Flexbox")
