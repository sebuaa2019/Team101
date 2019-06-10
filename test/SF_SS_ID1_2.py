import model
import Visual_Analyser
import time as tm

#testcase
class Task():
    
     def __init__(self,type,test,img,growth):
        self.type=type
        self.test=test
        self.img=img
        self.growth=growth

def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def test():
    ran=random.randint(0,100)
    if(ran>40):
        task=Task('classification',1,'grass',0)
        time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        level = 2
        info = 'The type of plant is:'+ va.send_img_message(task)
        print(toLog(time, level , "Visual", info))
    elif(ran>10):
        task=Task('classification',1,'plant',0)
        time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        level = 2
        info = 'The type of plant is:'+va.send_img_message(task)
        print(toLog(time, level , "Visual", info))
    elif(ran>3)
        task=Task('classification',1,'other',0)
        time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        level = 2
        info = 'The type of plant is:'+va.send_img_message(task)
        print(toLog(time, level , "Visual", info))
    else:
        task=Task('work',1,'other',0)
        time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        level = 1
        info = 'WRONG DEMAND'
        print(toLog(time, level , "Visual", info))

for i in range(200):
    test()
