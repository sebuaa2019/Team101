
# coding: utf-8

# In[4]:


class BasePart:
    
    def __init__(self,id,config):
        self.id=id
        self.config=config
        
class Visul_Analyser(BasePart):
    
    def __init__(self,id,config,photosize,modelpath,task_analysis):
        self.id=id
        self.config=config
        self.task_analysis
        self.task_analysis=task_analysis
        self.task_analysis.img_analysis.photosize=photosize
        self.task_analysis.img_analysis.modelpath=modelpath
        
    def send_img_message(list task):
        classification=self.task_analysis.task_identity(task)
        return classification
        
    
class Task_Analysis(BasePart):
    
    def __init__(id,img_analysis):
        self.id=id
        self.img_analysis=img_analysis
        
    def task_identity(task):
        if(task.type=='classification'):
            return self.class_execution(task)
     #  else if(): 
            
    def class_execution(task):
        return self.img_analysis.class_analyse(task)

        
class Img_Analysis(BasePart):
    
    def __init__(id):
        self.id=id
        self.phtotsize=0
        self.modelpath='path'
        
    def class_analyse(task):
        img = (np.expand_dims(task.img,0))
        prediction = self.modelpath.predict(img)
        return prediction
    

    
    
       
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

#download
fashion_mnist = keras.datasets.plant
(train_images, train_labels), (test_images, test_labels) = plant.load_data()
class_names = ['plant','weeds','others']

#explore
print(train_images.shape)
print(len(train_labels))
print(train_labels)
print(test_images.shape)
print(len(test_labels));


#visionable
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)

#pretreatment
train_images = train_images / 255.0
test_images = test_images / 255.0

#测试集前25张图像
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.xlabel(class_names[train_labels[i]])
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    
#model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(360,320)),
    keras.layers.Dense(128, activation=tf.nn.relu),#tf.nn.relu是激活函数
    keras.layers.Dense(10, activation=tf.nn.softmax)#同上
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#train
model.fit(train_images, train_labels, epochs=20)

#test
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test loss:',test_loss)
print('Test accuracy:', test_acc)    
        

