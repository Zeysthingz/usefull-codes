import pandas as pd
import numpy as np
import os
from tqdm import tqdm
import shutil

imagePath = r"D:\Eren\Teknofest-zgems\customDataset\zgems\Images" #İmgelerin dosya yolu olarak değiştirilecek
csvPath = r"D:\Eren\Teknofest-zgems\customDataset\zgems" #csv'lerin dosya yolu olarak değiştirilecek
outputPath = r"D:\Eren\Teknofest-zgems\customDataset\zgems" #train-test dosyaları nereye oluşmasını istersen o dosya yolu girilmeli

cdcwyaguhıjokplğşüi
,set4vbjsadknlmkşlşi
,
os.mkdir(os.path.join(outputPath,"train"))
os.mkdir(os.path.join(outputPath,"test"))

###Train
df = pd.read_csv(os.path.join(csvPath,"train.csv"))

dst = os.path.join(outputPath,"train")
for f in tqdm(df["filename"]):
    imgName = f.split(".")[0]+".jpg"
    shutil.copy2(os.path.join(imagePath,imgName), dst)
    break
    
    
###Test
df = pd.read_csv(os.path.join(csvPath,"test.csv"))

dst = os.path.join(outputPath,"test")
for f in tqdm(df["filename"]):
    imgName = f.split(".")[0]+".jpg"
    shutil.copy2(os.path.join(imagePath,imgName), dst)
    break
    


