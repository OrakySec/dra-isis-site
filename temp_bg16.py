import os
from PIL import Image

orig_path = r'C:\Users\MrDel\.gemini\antigravity\brain\ed7a5c69-061c-456c-8058-90a71597b62a\media__1781121851605.jpg'
dest_path = r'd:\Projetos\Dr. Isis Site\assets\images\bumbum_up_gold_antes_depois.jpg'

try:
    with Image.open(orig_path) as img:
        w, h = img.size # 809 x 1024
        
        # Left Image (Antes):
        # Crop y=0 to 460
        left_img = img.crop((0, 0, w, 460))
        
        # Right Image (Depois):
        # Previously y=500 to 960. This caused the bottom edge of the TOP image (y=500-512) 
        # to bleed into the top of the right buttock, creating the dark band and letters!
        # By shifting the crop down to y=525, we safely clear the seam (y=512) and eliminate the artifact.
        right_img = img.crop((0, 525, w, 985))
        
        # Canvas: 1618 x 460
        canvas = Image.new('RGB', (w * 2, 460), (35, 36, 45))
        canvas.paste(left_img, (0, 0))
        canvas.paste(right_img, (w, 0))
        
        canvas.save(dest_path, quality=100)
        print("Success! Artifact eliminated.")
except Exception as e:
    print("Error:", e)
