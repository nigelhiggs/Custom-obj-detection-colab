import PIL
from PIL import Image

basewidth = 600
hsize = 800

img = Image.open('C:/Users/nigel/Desktop/ground_181.jpg')

wpercent = (basewidth / float(img.size[0]))
#hsize = int((float(img.size[0]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
print(wpercent,hsize,img)
img.save('C:/Users/nigel/Desktop/exa6.jpg')
