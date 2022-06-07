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

    def sameSetKey_create_func(self,objs,params,start=0):
        for obj in objs:
            for param in params:
                attr=param["attr"]
                value=param["value"]
                time=param["time"]+start
                self.run(obj,attr,value,time)

    def repeatSetKey_create_func(self,objs,params,start=0):
        count=0
        for obj in objs:
            for param in params:
                attr=param["attr"]
                value=param["value"]
                time=param["time"]+count+start
                self.run(obj,attr,value,time)
            count=count+(params[-1]["time"]-params[0]["time"])



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