import os

hc_path = r'd:\Projetos\Dr. Isis Site\harmonizacao-corporal\index.html'
with open(hc_path, 'r', encoding='utf-8') as f:
    hc_html = f.read()

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

import re
# check if section exists
if '<!-- ===== ANTES E DEPOIS ===== -->' in hc_html:
    # replace the entire section
    hc_html = re.sub(r'<!-- ===== ANTES E DEPOIS ===== -->.*?<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->', hc_html, flags=re.DOTALL)
else:
    hc_html = hc_html.replace('<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->')

with open(hc_path, 'w', encoding='utf-8') as f:
    f.write(hc_html)
