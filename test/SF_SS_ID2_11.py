from arm_interface import *
import arm_control.joint_trajectory_controller as jointHandler
import time as tm
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/src')

def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def unitTestClawClose():
    clawOpen()
    clawClose()
    if jointHander.clawstate == 0: 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
        
if __name__ == "__main__":
    unitTestClawClose()
    print("Unit Test Claw Succeed")
