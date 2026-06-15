import os
from PIL import Image

# 1. Crop the image to make it slightly more horizontal to avoid bad cropping in the UI
img_path = r'd:\Projetos\Dr. Isis Site\assets\images\rejuvenescimento_antes_depois.jpg'
try:
    with Image.open(img_path) as img:
        # Crop 150px from top and 150px from bottom (keeps the faces centered, removes some forehead/neck)
        width, height = img.size
        cropped_img = img.crop((0, 100, width, height - 120))
        cropped_img.save(r'd:\Projetos\Dr. Isis Site\assets\images\rejuvenescimento_antes_depois_cropped.jpg', quality=95)
except Exception as e:
    print("Error cropping:", e)

# 2. Update index.html Rejuvenescimento Facial card
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

target_placeholder = '<div class="service-card__image--placeholder">✨</div>'
# Just replacing the first instance of this under Rejuvenescimento Facial might be tricky if there are multiple. 
# Let's find the card-ultramed
start = html.find('id="card-ultramed"')
if start != -1:
    placeholder_pos = html.find(target_placeholder, start)
    if placeholder_pos != -1:
        replacement = '<img src="assets/images/rejuvenescimento_antes_depois_cropped.jpg" alt="Rejuvenescimento Facial - Antes e Depois" class="service-card__image" style="object-position: center;">'
        html = html[:placeholder_pos] + replacement + html[placeholder_pos + len(target_placeholder):]
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated index.html card")

# 3. Update rejuvenescimento-facial/index.html
rej_path = r'd:\Projetos\Dr. Isis Site\rejuvenescimento-facial\index.html'
with open(rej_path, 'r', encoding='utf-8') as f:
    rej_html = f.read()

# Replace texts to match Rejuvenescimento Facial
rej_html = rej_html.replace('UltraMed (HIFU)', 'Rejuvenescimento Facial')
rej_html = rej_html.replace('UltraMed com a Dra. Ísis Andrade. Ultrassom micro e macrofocado para lifting facial sem cortes', 'Rejuvenescimento Facial com a Dra. Ísis Andrade. Tratamentos para flacidez e renovação da pele')
rej_html = rej_html.replace('UltraMed — Dra. Ísis Andrade', 'Rejuvenescimento Facial — Dra. Ísis Andrade')
rej_html = rej_html.replace('A tecnologia HIFU de ultrassom focado para um autêntico lifting facial e corporal sem cortes.', 'Tecnologia e expertise para uma pele firme, iluminada e jovem.')
rej_html = rej_html.replace('UltraMed (Lifting sem cortes)', 'Rejuvenescimento Facial')
rej_html = rej_html.replace('UltraMed\n        <em>Lifting sem cortes.</em>', 'Rejuvenescimento\n        <em>Facial.</em>')
rej_html = rej_html.replace('no UltraMed (Lifting sem cortes)', 'no Rejuvenescimento Facial')
rej_html = rej_html.replace('o UltraMed', 'o Rejuvenescimento Facial')

# Create the new section for Before/After
antes_depois_html = """
  <!-- ===== ANTES E DEPOIS ===== -->
  <section class="before-after" id="resultados" style="background: var(--cream); padding: 80px 0;">
    <div class="container--wide">
      <div class="section-header animate-on-scroll">
        <span class="label">Resultados Reais</span>
        <h2 class="section-title">
          Rejuvenescimento<br><em>Na Prática</em>
        </h2>
        <div class="divider"></div>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-strong); position: relative;">
        <img src="../assets/images/rejuvenescimento_antes_depois_cropped.jpg" alt="Antes e Depois Rejuvenescimento Facial" style="width: 100%; display: block;">
      </div>
    </div>
  </section>
"""

# Insert right before FOR WHO section
if '<!-- ===== ANTES E DEPOIS ===== -->' not in rej_html:
    rej_html = rej_html.replace('<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->')

with open(rej_path, 'w', encoding='utf-8') as f:
    f.write(rej_html)
print("Updated rejuvenescimento-facial page")
