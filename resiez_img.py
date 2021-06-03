import cv2
import pandas as pd
import numpy as np
from PIL import Image




def padding_image(image): 
    h, w = image.shape[0], image.shape[1] 
    if h - w > 0: 
        left_size,right_size = (h-w)//2,h-w-(h-w)//2 
        image = cv2.copyMakeBorder(image, 0, 0, left_size, right_size, cv2.BORDER_CONSTANT, 
                                   value=(0, 0, 0)) 
    else: 
        top,bottom = (w-h)//2,w-h-(w-h)//2 
        image = cv2.copyMakeBorder(image, top, bottom, 0, 0, cv2.BORDER_CONSTANT, 
                                   value=(0, 0, 0)) 
    return image
    
df = pd.read_csv('./input0/fu-data/data/0.886.csv')
for i in range(len(df)):
    #cv2.destroyAllWindows()
    img_name = './input0/fu-data/data/test/'+str(df['img_id'][i])
    #img = cv2.imread(path)
    #image = cv2.imdecode(np.fromfile(img_name, dtype=np.uint8), -1) 
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    #image = cv2.imread(img_name)
    #image = Image.open(img_name)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #image = image[:, :, [2,1,0]]
    image = cv2.imread(img_name,1)
    #image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB) 
    #b,g,r = cv2.split(image_bgr)
    #image = cv2.merge([r,g,b])
    cv2.imshow(str(df['img_id'][i]),image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #image = padding_image(image) 
    #cv2.imshow('image',image)
    #cv2.waitKey(0)
    #cv2.imwrite('./newdata/'+str(df['img_id'][i]), image)