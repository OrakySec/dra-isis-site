import os
import shutil
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121628627.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\tratamentos_corporais_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        print(f"Original size: {width}x{height}")
        
        # The image has large solid color borders at top and bottom.
        # Let's crop the top 20% and bottom 20% approximately
        # or we can find the first non-solid line.
        
        # Simple crop for now: assume the actual photos are in the middle half
        # let's crop top 22% and bottom 22%
        top = int(height * 0.22)
        bottom = int(height * 0.78)
        
        cropped_img = img.crop((0, top, width, bottom))
        cropped_img.save(dest_path, quality=95)
        print("Success! Image cropped. New size:", cropped_img.size)
except Exception as e:
    print("Error processing image:", e)

# 1. Update index.html Tratamentos Corporais card
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<img src="assets/images/lipo-antes-depois.png" alt="Tratamentos Corporais Antes e Depois" class="service-card__image">'
replacement = '<img src="assets/images/tratamentos_corporais_antes_depois.jpg" alt="Tratamentos Corporais Antes e Depois" class="service-card__image" style="object-position: center;">'
html = html.replace(target, replacement)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html card")

# 2. Update tratamentos-corporais/index.html
tc_path = r'd:\Projetos\Dr. Isis Site\tratamentos-corporais\index.html'
with open(tc_path, 'r', encoding='utf-8') as f:
    tc_html = f.read()

tc_html = tc_html.replace('lipo-antes-depois.png', 'tratamentos_corporais_antes_depois.jpg')

with open(tc_path, 'w', encoding='utf-8') as f:
    f.write(tc_html)
print("Updated tratamentos-corporais page")
