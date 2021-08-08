import cv2 as cv
import os 
import glob
from pathlib import Path
data_path="stanford_person/"
#data_path2="data2/"
data = os.listdir(data_path)
from PIL import Image

for i in data:
  
   if i.endswith('.jpg'):
        i=i.rsplit( ".jpg")[0]
        path="stanford_person/"+ i+".jpg"
        img=cv.imread("stanford_person/"+ i+".jpg")
        #cv.imshow('Image',img)
        #cv.waitKey(0)
        #break
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        cv.imwrite(f'{data_path}/{i}.jpg',img_rgb)


for i in range(5,10):
        print(i*2)
        print(lol)
print("hello")