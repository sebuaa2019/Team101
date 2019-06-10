#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import model

#训练集数据划分正确率评估
data = np.load("../input/Data.npz")
d = dict(zip(("trainX","testX","trainY", "testY"), (data[k] for k in data)))
trainX = d['trainX']
testX = d['testX']
trainY = d['trainY']
testY = d['testY']
#print(d["trainX"])
#print(model.evaluate(trainX, trainY))
print(model.evaluate(testX, testY))

#实际操作正确率评估

import Visual_Analyser#加载视觉分析模块代码

accuracy_all=[]

def test():
    plant_type=input()#手动输入
    right_times=0;
    for i in range(0,5):
        
        img=va.getphoto()#获取图片
        task=Task('classification',0,img,0)
        end=va.send_img_message(task)
        if(end==plant_type):
            right_times=right_times+1
            
    accuracy=right_times/5
    accuracy_all.append(accuracy)

def dsp_accuracy():
    sum=0
    times=0
    for i in accuracy_all:
        sum+=i
        times=times+1
    
    print(sum/i)

