import pymel.core as pm
import maya.cmds as cmds

def multiCountKey(interval = 10, keyNum = 4, grpKey = 1, sels = ''):
    cmds.select(sels)
    num = keyNum * grpKey
    nowKey = cmds.currentTime( query=True )
    for loopNum in range(num):
        cmds.currentTime( nowKey )
        cmds.setKeyframe()
        nowKey += interval

def countKey(interval = 10, keyNum = 4, grpKey = 1, sels = ''):
    for sel in sels:
        pm.select(sel)
        num = keyNum * grpKey
        nowKey = pm.currentTime( query=True )
        for loopNum in range(num):
            pm.currentTime( nowKey )
            pm.setKeyframe()
            nowKey += interval

def simpleKey_create_func(obj,attr,value,time):
    cmds.setKeyframe(obj,at=attr,v=value,t=[time])


def main():
    sels = pm.selected()
    multiCountKey(interval = 5, keyNum = 4, grpKey = 1, sels = sels)
    #countKey(interval = 5, keyNum = 4, grpKey = 1, sels = sels)

def sample():
    anim_dict={
    "sleeveChain_L0_fk0_ctl":[
        {"attr":"rotateZ","value":0,"time":0},
        {"attr":"rotateZ","value":-60,"time":6},
        {"attr":"rotateZ","value":-60,"time":12},
        {"attr":"rotateZ","value":0,"time":24},
        ],
    "sleeveChain_L0_fk1_ctl":[
        {"attr":"rotateZ","value":0,"time":0},
        {"attr":"rotateZ","value":-60,"time":6},
        {"attr":"rotateZ","value":-60,"time":12},
        {"attr":"rotateZ","value":0,"time":24},
        ]
    }
    for anim in anim_dict.items():
        for param in anim[1]:
            print(anim[0],param)

def moveCheck_create_func(objs,params,count=0):
    objs=objs or [
        "nurbsCircle1"
        "nurbsCircle2"
    ]
    params=params or [
        {"attr":"rotateZ","value":0,"time":0},
        {"attr":"rotateZ","value":-60,"time":6},
        {"attr":"rotateZ","value":-60,"time":12},
        {"attr":"rotateZ","value":0,"time":24},
    ]

    for obj in objs:
        for param in params:
            attr=param["attr"]
            value=param["value"]
            time=param["time"]+count
            #print(obj,attr,value,time)
            simpleKey_create_func(obj,attr,value,time)
        count=count+params[-1]["time"]