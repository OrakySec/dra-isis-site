from PIL import Image
import os

img_path = 'd:\\Projetos\\Dr. Isis Site\\assets\\images\\harmonizacao_facial_antes_depois.jpg'
output_path = 'd:\\Projetos\\Dr. Isis Site\\assets\\images\\harmonizacao_facial_antes_depois_cropped.jpg'

try:
    with Image.open(img_path) as img:
        width, height = img.size
        # Crop top 180px (Antes Depois text) and bottom 120px
        left = 0
        top = 180
        right = width
        bottom = height - 120
        
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path, quality=95)
        print("Success! Image cropped. New size:", cropped_img.size)
except Exception as e:
    print("Error:", e)
