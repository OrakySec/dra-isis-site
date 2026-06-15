import os
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        # original is 809x1024
        # "PÓS IMEDIATO" is in the middle. Let's crop from y=0 to y=470 for top, and y=550 to y=1024 for bottom
        # Let's also crop some left/right borders to make it less wide.
        
        top_img = img.crop((0, 0, width, 480))
        bottom_img = img.crop((0, 540, width, 1024))
        
        # New sizes
        t_width, t_height = top_img.size
        b_width, b_height = bottom_img.size
        
        new_width = t_width + b_width
        new_height = max(t_height, b_height)
        
        new_img = Image.new('RGB', (new_width, new_height), (35, 36, 45)) # approx background color
        new_img.paste(top_img, (0, 0))
        new_img.paste(bottom_img, (t_width, 0))
        
        new_img.save(dest_path, quality=95)
        print("Success! Image split and rejoined. New size:", new_img.size)
except Exception as e:
    print("Error processing image:", e)

# Let's also update index.html to have object-fit: contain for this image so it doesn't get chopped.
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">'
replacement = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-fit: contain; background: #23242c; padding: 10px;">'
html = html.replace(target, replacement)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
