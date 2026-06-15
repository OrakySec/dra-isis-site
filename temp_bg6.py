import os
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        # Original: 809x1024
        
        # We want to keep "PÓS IMEDIATO" entirely on the top image.
        # "PÓS IMEDIATO" seems to end around y=530 or so.
        # Let's crop top image to 540 height to include it safely.
        top_img = img.crop((0, 0, width, 540))
        
        # Bottom image starts right after the text.
        bottom_img = img.crop((0, 540, width, 1024))
        
        # Now stitch them side-by-side. 
        # The top image is 540 tall. The bottom image is 484 tall.
        # Let's pad the bottom image with the background color so they align well.
        # Wait, if we pad the bottom image, we can just center it vertically or align to bottom.
        # Let's create a canvas 540 tall.
        new_width = width * 2
        new_height = 540
        
        new_img = Image.new('RGB', (new_width, new_height), (35, 36, 45))
        new_img.paste(top_img, (0, 0))
        # Center the bottom image vertically
        y_offset = (540 - 484) // 2
        new_img.paste(bottom_img, (width, y_offset))
        
        new_img.save(dest_path, quality=95)
        print("Success! Image recreated side-by-side keeping text intact. New size:", new_img.size)
except Exception as e:
    print("Error:", e)

# Update index.html to use this wide image again
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Make sure the card uses bumbum_up_gold_antes_depois.jpg and DOES NOT have object-fit: contain
html = re.sub(r'<img src="assets/images/bumbum_up_gold_card.jpg"[^>]*>', '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">', html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html card to use wide image again")
