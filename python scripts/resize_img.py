import os
from PIL import Image
import imageio
import numpy as np

#this count will help with imageio.write to folder renaming 
count = 1
#looping through folder
for path in os.listdir('C:/Users/nigel/Desktop/ufc fighter'):

    #opens each individual photo
    img = Image.open('C:/Users/nigel/Desktop/ufc fighter/'+path)
    img = img.resize((416,416),Image.NEAREST)
    img = np.array(img)
    imageio.imwrite('C:/Users/nigel/Desktop/ufc fighter/resize/'+'fighter'+str(count)+'.jpg',img)
    count+=1
    print(path)
