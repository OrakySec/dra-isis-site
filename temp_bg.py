import os
import shutil
from PIL import Image
import re

# 1. Process the image
src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        print(f"Original size: {width}x{height}")
        
        # Split top/bottom
        half_height = height // 2
        
        top_img = img.crop((0, 0, width, half_height))
        bottom_img = img.crop((0, half_height, width, height))
        
        # Create new image side-by-side
        new_width = width * 2
        new_height = half_height
        
        new_img = Image.new('RGB', (new_width, new_height))
        new_img.paste(top_img, (0, 0))
        new_img.paste(bottom_img, (width, 0))
        
        new_img.save(dest_path, quality=95)
        print("Success! Image split and rejoined side-by-side. New size:", new_img.size)
except Exception as e:
    print("Error processing image:", e)

# 2. Update index.html Bumbum Gold card
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<img src="assets/images/bumbum-antes-depois.png" alt="Bumbum Up Gold Antes e Depois" class="service-card__image">'
replacement = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="object-position: center;">'
html = html.replace(target, replacement)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html card")

# 3. Update bumbum-gold/index.html (Wait, the page is in bumbum-up-gold/)
bg_path = r'd:\Projetos\Dr. Isis Site\bumbum-up-gold\index.html'
with open(bg_path, 'r', encoding='utf-8') as f:
    bg_html = f.read()

antes_depois_html = """
  <!-- ===== ANTES E DEPOIS ===== -->
  <section class="before-after" id="resultados" style="background: var(--cream); padding: 80px 0;">
    <div class="container--wide">
      <div class="section-header animate-on-scroll">
        <span class="label">Resultados Reais</span>
        <h2 class="section-title">
          Protocolo<br><em>Na Prática</em>
        </h2>
        <div class="divider"></div>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-strong); position: relative;">
        <img src="../assets/images/bumbum_up_gold_antes_depois.jpg" alt="Antes e Depois Bumbum Up Gold" style="width: 100%; display: block;">
      </div>
    </div>
  </section>
"""

# check if section exists
if '<!-- ===== ANTES E DEPOIS ===== -->' in bg_html:
    # replace the entire section
    bg_html = re.sub(r'<!-- ===== ANTES E DEPOIS ===== -->.*?<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->', bg_html, flags=re.DOTALL)
else:
    bg_html = bg_html.replace('<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->')

with open(bg_path, 'w', encoding='utf-8') as f:
    f.write(bg_html)
print("Updated bumbum-up-gold page")
