import os
from PIL import Image

# Re-create the pristine wide image first from the original to ensure no previous patches
orig_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    # 1. Create pristine side-by-side
    with Image.open(orig_path) as orig:
        w, h = orig.size
        top_img = orig.crop((0, 0, w, 540))
        bottom_img = orig.crop((0, 540, w, 1024))
        
        img = Image.new('RGB', (w * 2, 540), (35, 36, 45))
        img.paste(top_img, (0, 0))
        img.paste(bottom_img, (w, (540 - 484) // 2))

    # 2. Seamlessly move "PÓS IMEDIATO"
    pos_box = (100, 460, 750, 540)
    pos_text = img.crop(pos_box)
    
    # Erase original with a patch from just above it
    pos_patch = img.crop((100, 380, 750, 460))
    img.paste(pos_patch, (100, 460))
    
    # Create mask for white text
    pos_mask = pos_text.convert("L").point(lambda p: 255 if p > 150 else 0, mode="1")
    
    # Paste shifted right
    img.paste(pos_text, (100 + 150, 460), pos_mask)
    
    # 3. Seamlessly move "ESTRUTURAÇÃO"
    est_box = (809, 0, 1400, 120)
    est_text = img.crop(est_box)
    
    # Erase original with a patch from just below it
    est_patch = img.crop((809, 120, 1400, 240))
    img.paste(est_patch, (809, 0))
    
    # Create mask for white text
    est_mask = est_text.convert("L").point(lambda p: 255 if p > 140 else 0, mode="1")
    
    # Paste shifted down and right
    img.paste(est_text, (809 + 80, 0 + 60), est_mask)

    img.save(dest_path, quality=95)
    print("Success! Image edited flawlessly.")
except Exception as e:
    print("Error:", e)

# Fix HTML back to standard
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Remove flexbox layout, restore single image with default CSS
target_pattern = r'<div class="bumbum-flex-container">.*?</div>|<div style="display: flex; height: 200px; width: 100%;">.*?</div>'
replacement = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">'
html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

# Also remove any inline height from the single image if it exists
html = re.sub(r'<img src="assets/images/bumbum_up_gold_antes_depois.jpg"[^>]*>', replacement, html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored index.html to standard 200px card")
