import os

# 1. Update index.html
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Instead of exact exact string, let's look for the image tags around the IDs
# Card 2: Harmonização Corporal has id="card-harmonizacao-peitoral"
# Card 3: Tratamentos Corporais has id="card-lipo-enzimatica"

# Let's just find and replace the image filenames directly for now
html = html.replace('assets/images/tratamentos_corporais_antes_depois.jpg', 'assets/images/lipo-antes-depois.png')

import re
# For harmonizacao corporal card, we want to replace the image.
# The card has id="card-harmonizacao-peitoral" or similar
# Let's replace 'peitoral-antes-depois.png' OR 'peitoral_horizontal_antes_depois.png' OR 'peitoral_horizontal_sem_texto_1780422922300.png'
# whatever is there.
html = re.sub(r'src="assets/images/peitoral[^"]*"', 'src="assets/images/harmonizacao_corporal_antes_depois.jpg" style="object-position: center;"', html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update tratamentos-corporais/index.html
tc_path = r'd:\Projetos\Dr. Isis Site\tratamentos-corporais\index.html'
with open(tc_path, 'r', encoding='utf-8') as f:
    tc_html = f.read()
tc_html = tc_html.replace('tratamentos_corporais_antes_depois.jpg', 'lipo-antes-depois.png')
with open(tc_path, 'w', encoding='utf-8') as f:
    f.write(tc_html)


# 3. Update harmonizacao-corporal/index.html
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
else:
    # If it was already there, update image src just in case
    hc_html = re.sub(r'src="\.\./assets/images/peitoral[^"]*"', 'src="../assets/images/harmonizacao_corporal_antes_depois.jpg"', hc_html)

with open(hc_path, 'w', encoding='utf-8') as f:
    f.write(hc_html)

print("Updates applied")
