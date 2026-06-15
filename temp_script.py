import os
import re

file_path = 'harmonizacao-facial/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace texts to match Harmonização Facial
html = html.replace('UltraMed (HIFU)', 'Harmonização Facial')
html = html.replace('UltraMed com a Dra. Ísis Andrade. Ultrassom micro e macrofocado para lifting facial sem cortes', 'Harmonização Facial com a Dra. Ísis Andrade. Preenchimento, botox e reestruturação facial')
html = html.replace('UltraMed — Dra. Ísis Andrade', 'Harmonização Facial — Dra. Ísis Andrade')
html = html.replace('A tecnologia HIFU de ultrassom focado para um autêntico lifting facial e corporal sem cortes.', 'Resultados naturais e elegantes em preenchimento e toxina botulínica.')
html = html.replace('UltraMed (Lifting sem cortes)', 'Harmonização Facial')
html = html.replace('Tecnologia Avançada (HIFU)', 'Estética Avançada')
html = html.replace('UltraMed\n        <em>Lifting sem cortes.</em>', 'Harmonização\n        <em>Facial.</em>')
html = html.replace('Rejuvenescimento profundo e redução de flacidez através do ultrassom micro e macrofocado, estimulando colágeno desde as fáscias musculares até a superfície.', 'Equilíbrio, proporção e realce da sua beleza natural. Utilizamos os melhores preenchedores e toxina botulínica do mercado para resultados sutis e de alto padrão.')
html = html.replace('no UltraMed (Lifting sem cortes)', 'na Harmonização Facial')
html = html.replace('o UltraMed', 'a Harmonização Facial')
html = html.replace('Por que escolher o UltraMed', 'Por que realizar Harmonização com a Dra. Ísis')
html = html.replace('Firmeza e contorno<br><em>sem bisturi</em>', 'Naturalidade e<br><em>Simetria</em>')

# Create the new section for Before/After
antes_depois_html = """
  <!-- ===== ANTES E DEPOIS ===== -->
  <section class="before-after" id="resultados" style="background: var(--cream); padding: 80px 0;">
    <div class="container--wide">
      <div class="section-header animate-on-scroll">
        <span class="label">Resultados Reais</span>
        <h2 class="section-title">
          Harmonização<br><em>Na Prática</em>
        </h2>
        <div class="divider"></div>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-strong); position: relative;">
        <img src="../assets/images/harmonizacao_facial_antes_depois.jpg" alt="Antes e Depois Harmonização Facial" style="width: 100%; display: block;">
      </div>
    </div>
  </section>
"""

# Insert right before FOR WHO section
html = html.replace('<!-- ===== FOR WHO ===== -->', antes_depois_html + '\n  <!-- ===== FOR WHO ===== -->')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated harmonizacao facial page")
