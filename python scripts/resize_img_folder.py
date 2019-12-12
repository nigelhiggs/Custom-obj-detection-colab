import os
from PIL import Image
import imageio
import numpy as np
from PIL import ImageOps
import PIL

#this count will help with imageio.write to folder renaming 
count = 1
#looping through folder, os.listdir() place file path to folder inside.
for path in os.listdir('C:/Users/PRO/Desktop/Custom-obj-detection-colab/img'):
    img = Image.open('C:/Users/PRO/Desktop/Custom-obj-detection-colab/img/'+path)
    if hasattr(img, '_getexif'):
        orientation = 0x0112
        exif = img._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            img = img.transpose(rotations[orientation])
            img = img.resize((416,416),PIL.Image.ANTIALIAS)    
    
        img.save("C:/Users/PRO/Desktop/Custom-obj-detection-colab/img/"+path)

