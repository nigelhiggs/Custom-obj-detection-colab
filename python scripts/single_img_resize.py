import os
from PIL import Image
import imageio
import numpy as np
import PIL

#added libraries and file path.
image = Image.open("C:/Users/PRO/Desktop/IMG_0932.jpg")
if hasattr(image, '_getexif'):
    orientation = 0x0112
    exif = image._getexif()
    if exif is not None:
        orientation = exif[orientation]
        rotations = {
            3: Image.ROTATE_180,
            6: Image.ROTATE_270,
            8: Image.ROTATE_90
        }
        image = image.transpose(rotations[orientation])
        #my edits 
        image = image.resize((416,416),PIL.Image.ANTIALIAS)
        
image.save('C:/Users/PRO/Desktop/test.jpeg')
