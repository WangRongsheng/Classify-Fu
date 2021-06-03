# -*- coding: utf-8 -*-  
import os 

for root, dirs, files in os.walk('./input0/fu-data/data/test/'): 
    print(files) #当前路径下所有非目录子文件
with open('./input0/fu-data/data/test.txt',"a+") as file:
    for i in range(len(files)):
        file.write(str(files[i])+"\n")
