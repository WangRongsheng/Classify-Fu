## 赛事介绍

[图像分类成长赛——AI集福，“福”字图片识别](https://www.marsbigdata.com/competition/details?id=17284239856640)

### 1. train：  
- pip install -r requirments.txt  
- 修改 `train_model.py` 里的训练参数  
- python train_model.py  

一个常识:好的预训练是成功的一半,最好还是用预训练好的模型进行初始化.  


### 2. predict：
- 修改 `inference_model.py` 里的预测参数  
- python inference_model.py   


### 3. score：  
模型选用resnext101_32x4d, 先用mixup训练30epoch后,在用正常的数据微调模型后,预测得分`0.889967637540453`



