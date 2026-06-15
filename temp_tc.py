import os

# 1. Update index.html Tratamentos Corporais card
index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<img src="assets/images/lipo-antes-depois.png" alt="Lipo Enzimática Antes e Depois" class="service-card__image">'
replacement = '<img src="assets/images/tratamentos_corporais_antes_depois.jpg" alt="Tratamentos Corporais - Antes e Depois" class="service-card__image" style="object-position: center;">'
if target in html:
    html = html.replace(target, replacement)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html card")

# 2. Update tratamentos-corporais/index.html
tc_path = r'd:\Projetos\Dr. Isis Site\tratamentos-corporais\index.html'
with open(tc_path, 'r', encoding='utf-8') as f:
    tc_html = f.read()

# Replace texts
tc_html = tc_html.replace('Lipo Enzimática | Dra. Ísis Andrade', 'Tratamentos Corporais | Dra. Ísis Andrade')
tc_html = tc_html.replace('Lipo Enzimática — Dra. Ísis Andrade', 'Tratamentos Corporais — Dra. Ísis Andrade')
tc_html = tc_html.replace('Tratamento minimamente invasivo para redução de gordura localizada. Lipo enzimática em Recife com a Dra. Ísis Andrade.', 'Tratamentos Corporais com a Dra. Ísis Andrade. Protocolos avançados para redução de gordura, celulite e definição corporal.')
tc_html = tc_html.replace('A Lipo Enzimática é o tratamento ideal para eliminar a gordura localizada que não sai com dieta e exercício.', 'Protocolos estéticos corporais avançados para definição, redução de gordura localizada e melhora da flacidez e celulite.')
tc_html = tc_html.replace('Lipo Enzimática', 'Tratamentos Corporais')
tc_html = tc_html.replace('Lipo\n        <em>Enzimática.</em>', 'Tratamentos\n        <em>Corporais.</em>')
tc_html = tc_html.replace('Gordura Localizada', 'Estética Avançada')
tc_html = tc_html.replace('Elimine aquela gordura resistente de forma rápida e segura, redefinindo o contorno corporal ou facial através da aplicação de enzimas.', 'Protocolos minimamente invasivos para eliminar gordura resistente, melhorar o tônus da pele e realçar o seu contorno corporal.')
tc_html = tc_html.replace('na Lipo Enzimática', 'nos Tratamentos Corporais')
tc_html = tc_html.replace('a Lipo Enzimática', 'os Tratamentos Corporais')
tc_html = tc_html.replace('Por que escolher a Lipo Enzimática', 'Por que realizar Tratamentos Corporais com a Dra. Ísis')
tc_html = tc_html.replace('Como funcionam as<br><em>Enzimas</em>', 'Como funcionam os<br><em>Protocolos</em>')

# Create the new section for Before/After
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
        <img src="../assets/images/tratamentos_corporais_antes_depois.jpg" alt="Antes e Depois Tratamentos Corporais" style="width: 100%; display: block;">
      </div>
    </div>
  </section>
"""

# Insert right before FOR WHO section
if '<!-- ===== ANTES E DEPOIS ===== -->' not in tc_html:
    tc_html = tc_html.replace('<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->')

with open(tc_path, 'w', encoding='utf-8') as f:
    f.write(tc_html)
print("Updated tratamentos-corporais page")
