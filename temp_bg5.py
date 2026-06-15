import os
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'

card_dest = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_card.jpg'
page_dest = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        
        # 1. Full horizontal for the inner page (preserving text)
        top_full = img.crop((0, 0, width, 480))
        bottom_full = img.crop((0, 540, width, 1024))
        full_img = Image.new('RGB', (width * 2, max(top_full.height, bottom_full.height)), (35, 36, 45))
        full_img.paste(top_full, (0, 0))
        full_img.paste(bottom_full, (width, 0))
        full_img.save(page_dest, quality=95)
        print("Generated full horizontal for inner page:", full_img.size)
        
        # 2. Tightly cropped for the card (removing text in the middle)
        # Top image: text is on the right, crop x from 50 to 550
        top_crop = img.crop((50, 0, 550, 480))
        # Bottom image: text is on the left, crop x from 250 to 750
        bottom_crop = img.crop((250, 540, 750, 1024))
        
        card_img = Image.new('RGB', (1000, max(top_crop.height, bottom_crop.height)), (35, 36, 45))
        card_img.paste(top_crop, (0, 0))
        card_img.paste(bottom_crop, (500, 0))
        card_img.save(card_dest, quality=95)
        print("Generated tightly cropped for card:", card_img.size)

except Exception as e:
    print("Error:", e)

# Update index.html to use the tightly cropped version for the card
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the card image
import re
html = re.sub(r'<img src="assets/images/bumbum_up_gold_antes_depois.jpg"[^>]*>', '<img src="assets/images/bumbum_up_gold_card.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">', html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use card image")
