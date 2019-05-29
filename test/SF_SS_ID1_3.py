#!/usr/bin/env python
# coding: utf-8


#testcase
class Task():
    
     def __init__(self,type,test,img,growth):
        self.type=type
        self.test=test
        self.img=img
        self.growth=growth

import Visual_Analyser
import model
import time as tm

def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def test():
    task=Task('growth',1,'plant',0)
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'The type of plant is:'+va.send_img_message(task)
    print(toLog(time, level , "Visual", info))

    task=Task('growth',1,'plant',1)
    time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    level = 2
    info = 'The type of plant is:'+va.send_img_message(task)
    print(toLog(time, level , "Visual", info))
    
test


