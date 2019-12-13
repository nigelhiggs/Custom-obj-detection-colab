import shutil 
import os

location = 'C:/Users/PRO/Desktop/Custom-obj-detection-colab/img'
destination = 'C:/Users/PRO/Desktop/Recycle Bin'

for x in os.listdir(location):
    print(x)
    if x.endswith('.xml'):
        shutil.move(location+'/'+str(x),destination)
        print(location+'/'+str(x))        
