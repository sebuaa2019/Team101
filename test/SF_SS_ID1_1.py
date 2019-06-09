#!/usr/bin/env python
# coding: utf-8

# In[15]:


class BasePart:
    
    def __init__(self,id,config):
        self.id=id
        self.config=config
        
class Visul_Analyser(BasePart):
    
    def __init__(self,id,config,photosize,modelpath):
        self.id=id
        self.config=config
        self.task_analysis=Task_Analysis(id,photosize,modelpath)
        
    def send_img_message(self,task):
        classification=self.task_analysis.task_identity(task)
        return classification
        
    
class Task_Analysis(BasePart):
    
    def __init__(self,id,photosize,modelpath):
        self.id=id
        self.img_analysis=Img_Analysis(id,photosize,modelpath)
        
    def task_identity(self,task):
        if(task.type=='classification'):
            return self.class_execution(task)
        
        else if(task.type=='growth'):
            if(self.class_execution(task)!='plant'):
                print('ERROR')
            else:
                return self.growth_execution(task)
        
        else:
            return 'ERROR'
            
    def class_execution(self,task):
        return self.img_analysis.class_analyse(task)
    
    def growth_execution(self,task):
        return self.img_analysis.growth_analyse(task)

        
class Img_Analysis(BasePart):
    
    def __init__(self,id,photosize,modelpath):
        self.id=id
        self.photosize=photosize
        self.modelpath=modelpath
        
    def class_analyse(self,task):
        if(task.test==1):
            return task.img
        else:
            img = (np.expand_dims(task.img,0))
            prediction = self.modelpath.predict(img)
            return prediction
        
    def growth_analyse(self,task):
        if(self.class_execution(task)!='plant'):
            print('ERROR')
        else:
            return task.growth

#testcase
class Task():
    
     def __init__(self,type,test,img,growth):
        self.type=type
        self.test=test
        self.img=img
        self.growth=growth

import time as tm

def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def test():
    bp=BasePart(7,{'server':'hjk','client':'ljz'})
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'BasePart的id为:'+ bp.id 
    print(toLog(time, level , "Visual", info))
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'BasePart的config为:'+ bp.config
    print(toLog(time, level , "Visual", info))
    
#Visul_Analyser,Task_Analysis,Img_Analysis
    va=Visul_Analyser(7,{'server':'hjk','client':'ljz'},(320,360),'D:\\Software_Engineering\\model.py')
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'Visul_Analyser的id为:'+va.id
    print(toLog(time, level , "Visual", info))
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'Visul_Analyser的config为:'+va.config
    print(toLog(time, level , "Visual", info))
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'Task_Analysis的id为:'+va.task_analysis.id
    print(toLog(time, level , "Visual", info))
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'Img_Analysis的id为:'+va.task_analysis.img_analysis.id
    print(toLog(time, level , "Visual", info))
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'Img_Analysis的photosize为:'+va.task_analysis.img_analysis.photosize
    print(toLog(time, level , "Visual", info))
    
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'Img_Analysis的modelpath为:'+va.task_analysis.img_analysis.modelpath
    print(toLog(time, level , "Visual", info))
    

test
    
        


# In[ ]:




