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
