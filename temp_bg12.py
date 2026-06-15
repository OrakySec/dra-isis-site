import re

index_path = r'd:\Projetos\Dr. Isis Site\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the flexbox layout with the clean card image
target_pattern = r'<div class="bumbum-flex-container"[^>]*>.*?</div>'
replacement = '<img src="assets/images/bumbum_up_gold_card.jpg" alt="Bumbum Up Gold Antes e Depois" class="service-card__image">'

html = re.sub(target_pattern, replacement, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to use clean textless bumbum_up_gold_card.jpg")
