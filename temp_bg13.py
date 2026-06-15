import os
from PIL import Image

orig_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_uniforme.jpg'

try:
    with Image.open(orig_path) as img:
        w, h = img.size
        
        # We need to crop out ALL texts to make it 100% clean and uniform.
        # Top image (Antes): Buttock is on the left.
        # "PÓS IMEDIATO" is at the bottom (y=470-540).
        # "CORREÇÃO" is on the right (x>550).
        # Safe crop for pure left buttock: x=0 to 550, y=0 to 460
        left_buttock = img.crop((0, 0, 550, 460))
        
        # Bottom image (Depois): Buttock is on the right.
        # "ESTRUTURAÇÃO" is on the left (x<400) and top (y=540-600).
        # Safe crop for pure right buttock: x=400 to 809, y=560 to 1020
        # To match height of 460: y=560 to 1020 is exactly 460px tall!
        right_buttock = img.crop((400, 560, w, 1020))
        
        # Stitch them side-by-side
        # Canvas width = 550 + (809 - 400) = 550 + 409 = 959
        # Canvas height = 460
        canvas = Image.new('RGB', (959, 460), (35, 36, 45))
        canvas.paste(left_buttock, (0, 0))
        canvas.paste(right_buttock, (550, 0))
        
        canvas.save(dest_path, quality=100)
        print("Success! Created bumbum_uniforme.jpg")
except Exception as e:
    print("Error:", e)

# Update HTML to use bumbum_uniforme.jpg
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Match any img tag for bumbum gold card image
target_pattern = r'<img src="assets/images/bumbum_up_gold_[^"]+"[^>]*class="service-card__image"[^>]*>'
replacement = '<img src="assets/images/bumbum_uniforme.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image">'

html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use bumbum_uniforme.jpg")
