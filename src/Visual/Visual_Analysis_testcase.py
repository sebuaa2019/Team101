
# coding: utf-8

# In[33]:


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
        else:
            return 'ERROR'
            
    def class_execution(self,task):
        return self.img_analysis.class_analyse(task)

        
class Img_Analysis(BasePart):
    
    def __init__(self,id,photosize,modelpath):
        self.id=id
        self.photosize=photosize
        self.modelpath=modelpath
        
    def class_analyse(self,task):
        if(task.test==1):
            return 'grass'
        else:
            img = (np.expand_dims(task.img,0))
            prediction = self.modelpath.predict(img)
            return prediction

#testcase
class Task():
    
     def __init__(self,type,test):
        self.type=type
        self.test=test

#BasePart
bp=BasePart(7,{'server':'hjk','client':'ljz'})
print('BasePart的id为:',bp.id)
print('BasePart的config为:',bp.config,'\n')

#Visul_Analyser,Task_Analysis,Img_Analysis
va=Visul_Analyser(7,{'server':'hjk','client':'ljz'},(320,360),'D:\\Software_Engineering\\model.py')
print('Visul_Analyser的id为:',va.id)
print('Visul_Analyser的config为:',va.config)
print('Task_Analysis的id为:',va.task_analysis.id)
print('Img_Analysis的id为:',va.task_analysis.img_analysis.id)
print('Img_Analysis的photosize为:',va.task_analysis.img_analysis.photosize)
print('Img_Analysis的modelpath为:',va.task_analysis.img_analysis.modelpath,'\n')
                  
#Task test
task=Task('classification',1)
print('The type of plant is:',va.send_img_message(task),'\n')
                  
task=Task('location',1)
print('The type of plant is:',va.send_img_message(task))

                  
                  
                  

