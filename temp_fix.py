import os
import shutil

# 1. Rename the image to the correct name
old_img = r'd:\Projetos\Dr. Isis Site\assets\images\tratamentos_corporais_antes_depois.jpg'
new_img = r'd:\Projetos\Dr. Isis Site\assets\images\harmonizacao_corporal_antes_depois.jpg'
if os.path.exists(old_img):
    shutil.move(old_img, new_img)

# 2. Fix index.html
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Revert Tratamentos Corporais card image to lipo
html = html.replace('<img src="assets/images/tratamentos_corporais_antes_depois.jpg" alt="Tratamentos Corporais - Antes e Depois" class="service-card__image" style="object-position: center;">', '<img src="assets/images/lipo-antes-depois.png" alt="Tratamentos Corporais Antes e Depois" class="service-card__image">')

# Change Harmonização Corporal card image
target_hc = '<img src="assets/images/peitoral-antes-depois.png" alt="Harmonização Peitoral Antes e Depois" class="service-card__image">'
replacement_hc = '<img src="assets/images/harmonizacao_corporal_antes_depois.jpg" alt="Harmonização Corporal Antes e Depois" class="service-card__image" style="object-position: center;">'
html = html.replace(target_hc, replacement_hc)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed index.html")

# 3. Fix tratamentos-corporais/index.html
tc_path = r'd:\Projetos\Dr. Isis Site\tratamentos-corporais\index.html'
with open(tc_path, 'r', encoding='utf-8') as f:
    tc_html = f.read()

# Update the before/after section in tratamentos corporais to use the old lipo image
tc_html = tc_html.replace('tratamentos_corporais_antes_depois.jpg', 'lipo-antes-depois.png')
with open(tc_path, 'w', encoding='utf-8') as f:
    f.write(tc_html)

# 4. Update harmonizacao-corporal/index.html
hc_path = r'd:\Projetos\Dr. Isis Site\harmonizacao-corporal\index.html'
with open(hc_path, 'r', encoding='utf-8') as f:
    hc_html = f.read()

# Replace texts
hc_html = hc_html.replace('Harmonização Peitoral', 'Harmonização Corporal')
hc_html = hc_html.replace('harmonização peitoral', 'harmonização corporal')
hc_html = hc_html.replace('Para Homens', 'Contorno Perfeito')

antes_depois_html = """
  <!-- ===== ANTES E DEPOIS ===== -->
  <section class="before-after" id="resultados" style="background: var(--cream); padding: 80px 0;">
    <div class="container--wide">
      <div class="section-header animate-on-scroll">
        <span class="label">Resultados Reais</span>
        <h2 class="section-title">
          Protocolos<br><em>Na Prática</em>
        </h2>
        <div class="divider"></div>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-strong); position: relative;">
        <img src="../assets/images/harmonizacao_corporal_antes_depois.jpg" alt="Antes e Depois Harmonização Corporal" style="width: 100%; display: block;">
      </div>
    </div>
  </section>
"""

# Insert right before FOR WHO section
if '<!-- ===== ANTES E DEPOIS ===== -->' not in hc_html:
    hc_html = hc_html.replace('<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->')

with open(hc_path, 'w', encoding='utf-8') as f:
    f.write(hc_html)
print("Updated harmonizacao-corporal page")
