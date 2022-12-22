import pymel.core as pm
import maya.cmds as cmds

from . import jsonLB as jLB

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

param_dicts=[
        {"attr":"rotateZ","value":0,"time":0},
        {"attr":"rotateZ","value":-60,"time":6},
        {"attr":"rotateZ","value":-60,"time":12},
        {"attr":"rotateZ","value":0,"time":24},
    ]


class MatrixKey():
    def __init__(self):
        self.

class KeyObject():
    def __init__(self):
        self._object=""
        self._attr=""
        self._time=""
        self._value=0
        self._inTangentType="linear"
        self._outTangentType="linear"

    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setAttr(self,variable):
        self._attr=variable
        return self._attr
    def getAttr(self):
        return self._attr

    def setTime(self,variable):
        self._time=variable
        return self._time
    def getTime(self):
        return self._time

    def setValue(self,variable):
        self._value=variable
        return self._value
    def getValue(self):
        return self._value

    def setInTangentType(self,variable):
        self._inTangentType=variable
        return self._inTangentType
    def getInTangentType(self):
        return self._inTangentType

    def setOutTangentType(self,variable):
        self._outTangentType=variable
        return self._outTangentType
    def getOutTangentType(self):
        return self._outTangentType

    def setKeyFrame(self):
        cmds.setKeyframe(self._object,at=self._attr,v=self._value,t=[self._time],itt=self._inTangentType,ott=self._outTangentType)

class EditKey():
    def __init__(self):
        self._object=""
        self._param_dicts=[]


def setObjectKey(obj,params):
    keyObj=KeyObject()
    keyObj.setObject(obj)
    for param_dict in param_dicts:
        keyObj.setAttr(param_dict["attr"])
        keyObj.setValue(param_dict["value"])
        keyObj.setTime(param_dict["time"])
        keyObj.setKeyFrame()

def readKey(anim_dict):
    keyObj=KeyObject()
    for objParam_list in anim_dict.items():
        keyObj.setObject(objParam_list[0])
        for param_dict in objParam_list[1]:
            keyObj.setAttr(param_dict["attr"])
            keyObj.setValue(param_dict["value"])
            keyObj.setTime(param_dict["time"])
            keyObj.setKeyFrame()
            #print(anim[0],param)


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

