#we are making a script that will allow for easy access to print loads of address
#locations to .txt files through a for loop.


file = open('C:/Users/PRO/Desktop/Custom-obj-detection-colab/train.txt','w+')


for x in range(1,107):
    file.write('/content/Custom-obj-detection-colab/img/expo_marker'+str(x)+'.jpg'+'\n') 
    print('/content/Custom-obj-detection-colab/img/expo_marker'+str(x)+'.jpg'+'\n')
file.close() #to change file access modes 
  


