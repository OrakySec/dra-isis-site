import os
from PIL import Image

src_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781120466951.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\tratamentos_corporais_antes_depois.jpg'

try:
    with Image.open(src_path) as img:
        width, height = img.size
        # The image is top/bottom. Split at height/2
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
