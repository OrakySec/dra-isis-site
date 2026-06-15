import os
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        # Original: 809x1024
        
        # Top image: text is on the right. We can crop the left.
        # Let's crop x from 150 to 809, and y from 0 to 480.
        top_img = img.crop((150, 0, 809, 480))
        
        # Bottom image: text is on the left. We can crop the right.
        # Let's crop x from 0 to 659, and y from 540 to 1024.
        bottom_img = img.crop((0, 540, 659, 1024))
        
        t_width, t_height = top_img.size
        b_width, b_height = bottom_img.size
        
        new_width = t_width + b_width
        new_height = max(t_height, b_height)
        
        new_img = Image.new('RGB', (new_width, new_height), (35, 36, 45))
        new_img.paste(top_img, (0, 0))
        new_img.paste(bottom_img, (t_width, 0))
        
        new_img.save(dest_path, quality=95)
        print("Success! Image tightly cropped and rejoined. New size:", new_img.size)
except Exception as e:
    print("Error:", e)

# Restore index.html card to use object-fit cover instead of contain
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-fit: contain; background: #23242c; padding: 10px;">'
replacement = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">'
html = html.replace(target, replacement)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html card to revert object-fit contain")
