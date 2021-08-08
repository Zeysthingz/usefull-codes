import numpy as np
import cv2
import os

# print((InputHeight,InputWidth))
cap = cv2.VideoCapture('stanford.mov')
counter = 0

while(cap.isOpened()):
    counter += 1
    if(counter ==1000):
      break
    ret, frame = cap.read()
    img = frame
    out_path = "stanford_person/"+str(counter)+".jpg"
    cv2.imwrite(out_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))    
    #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #out_path = "teknofest_data/"+str(counter)+".jpg"
    #cv2.imwrite(out_path,img)

cap.release()