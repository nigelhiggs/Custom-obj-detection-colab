import shutil 
import os

location = 'C:/Users/nigel/Desktop/ufc fighter/resize'
destination = 'C:/Users/nigel/Desktop/Custom-obj-detection-colab/img'

for x in os.listdir(location):
    if x.endswith('.jpg'):
        shutil.copy(location+'/'+str(x),destination)
        
