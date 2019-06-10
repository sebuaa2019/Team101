import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import model
import os

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
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info =  'The type of the input：'+plant_type
    print(toLog(time, level , "Visual", info))
    
    for img in os.listdir(r"./img"): 
        
        time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        level = 2
        info =  'start analyse'
        print(toLog(time, level , "Visual", info))
    
        task=Task('classification',0,img,0)
        end=va.send_img_message(task)
        if(end==plant_type):
            right_times=right_times+1
            time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
            level = 2
            info =  'The type of the image is crops'
            print(toLog(time, level , "Visual", info))
        else:
            time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
            level = 2
            info =  'The type of the timage is grass'
            print(toLog(time, level , "Visual", info))
            
    accuracy=right_times/100
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info =  accuracy
    print(toLog(time, level , "Visual", info))
    

for i in range(26):
    test()
    
