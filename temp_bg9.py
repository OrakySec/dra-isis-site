import re

index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# The current HTML has the flexbox:
# <div style="display: flex; height: 200px; width: 100%;"> ... </div>

target_pattern = r'<div style="display: flex; height: 200px; width: 100%;">.*?</div>'
replacement = '<img src="assets/images/bumbum_up_gold_antes_depois.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image" style="height: 140px; object-position: center;">'

html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use single wide image with height: 140px")
