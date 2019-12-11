import shutil 
import os

location = 'C:/Users/nigel/Desktop/ufc fighter/resize'
destination = 'C:/Users/nigel/Desktop/XmlToTxt/xml'

for x in os.listdir(location):
    if x.endswith('.xml'):
        shutil.copy(location+'/'+str(x),destination)
        
