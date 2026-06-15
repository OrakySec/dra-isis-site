import os
from PIL import Image, ImageDraw

src_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_card.jpg'

try:
    with Image.open(src_path) as img:
        # img is 1618 x 540
        # Background color: (35, 36, 45)
        bg_color = (35, 36, 45)
        
        # Create a copy to edit
        new_img = img.copy()
        draw = ImageDraw.Draw(new_img)
        
        # 1. Move "PÓS IMEDIATO" to the right.
        # It's currently at the bottom of the left half. Let's guess its box is (100, 460) to (700, 540)
        # We will crop it, erase it, and paste it shifted right.
        # Actually, let's just shift a safe rectangle: (200, 470, 750, 540)
        # Let's shift it right by 150 pixels.
        pos_box = (150, 460, 750, 540)
        pos_text = img.crop(pos_box)
        draw.rectangle(pos_box, fill=bg_color)
        new_img.paste(pos_text, (pos_box[0] + 150, pos_box[1]))
        
        # 2. Move "ESTRUTURAÇÃO + ESTÍMULO DE COLÁGENO" down.
        # It's at the top of the right half. Let's guess its box is (809, 0) to (1400, 150)
        # Let's shift it down by 50 pixels.
        est_box = (809, 0, 1400, 120)
        est_text = img.crop(est_box)
        draw.rectangle(est_box, fill=bg_color)
        new_img.paste(est_text, (est_box[0], est_box[1] + 50))
        
        new_img.save(dest_path, quality=95)
        print("Success! Texts shifted towards center.")
except Exception as e:
    print("Error:", e)

# Update index.html to use this card-specific image
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(r'<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image"[^>]*>', '<img src="assets/images/bumbum_up_gold_card.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">', html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use card image")
