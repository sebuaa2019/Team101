#!/usr/bin/env python
# coding: utf-8

import model
import Visual_Analyser
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
    
        

