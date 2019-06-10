from arm_interface import *
import arm_control.joint_trajectory_controller as jointHandler
import time as tm
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/src')

def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    return str(time+" "+LEVEL[level]+" "+path+" "+info)

def unitTestClawOpen():
    clawClose()
    clawOpen()
    if jointHandler.clawstate == 1: 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" + str(jointHandler.clawstate)
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "Claw open test failed"
        
    print(toLog(time, level , "claw", info))

if __name__ == "__main__":
    unitTestClawOpen()
