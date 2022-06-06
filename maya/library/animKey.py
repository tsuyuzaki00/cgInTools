import pymel.core as pm
import maya.cmds as cmds

class CAnimKey():
    def run(self,obj,attr,value,time,intt="linear",outt="linear"):
        cmds.setKeyframe(obj,at=attr,v=value,t=[time],itt=intt,ott=outt)
        return obj,attr,value,time,intt,outt

    def exAnim(self):
        pass
    
    def inAnim(self):
        pass

    def repeatChecks_create_func(self,objs,params,count=0):
        for obj in objs:
            for param in params:
                attr=param["attr"]
                value=param["value"]
                time=param["time"]+count
                self.run(obj,attr,value,time)
            count=count+params[-1]["time"]


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

objs=[
    "nurbsCircle1"
    "nurbsCircle2"
],
params=[
{"attr":"rotateZ","value":0,"time":0},
{"attr":"rotateZ","value":-60,"time":6},
{"attr":"rotateZ","value":-60,"time":12},
{"attr":"rotateZ","value":0,"time":24},
]