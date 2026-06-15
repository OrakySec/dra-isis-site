import os
from PIL import Image

dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(dest_path) as img:
        width, height = img.size
        # currently 1318x484
        
        # Target aspect ratio 3:2 (1.5)
        target_height = int(width / 1.5) # 1318 / 1.5 = ~878
        
        # Create a new image with the target dimensions, filled with the background color
        new_img = Image.new('RGB', (width, target_height), (35, 36, 45))
        
        # Calculate Y position to center the image vertically
        y_pos = (target_height - height) // 2
        
        # Paste the existing image into the center
        new_img.paste(img, (0, y_pos))
        
        new_img.save(dest_path, quality=95)
        print("Success! Image padded to 3:2 aspect ratio. New size:", new_img.size)
except Exception as e:
    print("Error:", e)
