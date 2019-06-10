from arm_interface import *
import arm_control.joint_trajectory_controller as jointHandler
from arm_description import jointMsg
import time as tm
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/src')

def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    return str(time+" "+LEVEL[level]+" "+path+" "+info)

def testUpperArmMove():
    jointMsg jm = jointMsg("test")
    init(jm, jointHandler)
    target = jointHandler.highest()
    upperArmMove(target, jointHandler)
    if jointHandler.pos.equal(target): 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed " + str(jointHandler.pos)
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "upperArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))

    target = jointHandler.lowest()
    upperArmMove(target, jointHandler)
    if jointHandler.pos.equal(target): 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed " + str(jointHandler.pos)
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "upperArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))
    
    target = jointHandler.randomUnreachable()
    try:
       upperArmMove(target, jointHandler)
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "upperArmMove test failed"
    finally:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed " + str(jointHandler.pos)
        
    print(toLog(time, level , "arm_interface", info))


if __name__ == "__main__":
    testUpperArmMove()
