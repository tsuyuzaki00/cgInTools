import maya.cmds as cmds

from . import objectLB as oLB
from . import jsonLB as jLB

class MatrixKey():
    def __init__(self):
        pass

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

class KeyObjects():
    def __init__(self):
        self._object=""
        self._keyObject_dicts=[]

    def keyObject_create_dicts(self,obj):
        keyAttrs=cmds.listAttr(obj,k=True)
        name=obj.split(":")[-1]
        keys_dict={"keys":[]}
        for keyAttr in keyAttrs:
            times=cmds.keyframe(obj,q=True,at=keyAttr)
            if not times == None:
                for time in times:
                    value=cmds.getAttr(obj+"."+keyAttr,t=time)
                    inType=cmds.keyTangent(obj,q=True,at=keyAttr,itt=True,t=(time,time))
                    outType=cmds.keyTangent(obj,q=True,at=keyAttr,ott=True,t=(time,time))
                    keyObject_dict={"object":name,"attr":keyAttr,"time":time,"value":value,"inTangentType":inType[0],"outTangentType":outType[0]}
                    keys_dict["keys"].append(keyObject_dict)
        return keys_dict
    #Single Function
    def getKeyAttr_query_dicts(self,obj):
        keyObject_dicts=[]
        keyAttrs=cmds.listAttr(obj,k=True)
        for keyAttr in keyAttrs:
            times=cmds.keyframe(obj,q=True,at=keyAttr)
            if not times == None:
                for time in times:
                    keyObject_dict={"object":obj,"attr":keyAttr,"time":time}
                    keyObject_dicts.append(keyObject_dict)
        return keyObject_dicts

    #Multi Function
    def _getObjectKeys_query_dict(self,obj):
        keyObject_dicts=self.getKeyAttr_query_dicts(obj)

        keys_dict={"keys":[]}
        for keyObject_dict in keyObject_dicts:
            keyObject=oLB.KeyObject(keyObject_dict["object"])
            keyObject.setAttr(keyObject_dict["attr"])
            keyObject.setTime(keyObject_dict["time"])
            keyObject.loading()
            noNameSpace=keyObject.getObject().split(":")[-1]

            keyObject_dict={
                "object":noNameSpace,
                "attr":keyObject.getAttr(),
                "time":keyObject.getTime(),
                "value":keyObject.getValue(),
                "inTangentType":keyObject.getInType(),
                "outTangentType":keyObject.getOutType(),
                "inAngle":keyObject.getInAngle(),
                "outAngle":keyObject.getOutAngle()
            }
            keys_dict["keys"].append(keyObject_dict)
        return keys_dict

    #Public Function
    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setKeyObjectDicts(self,validates):
        self._keyObject_dicts=validates
        return self._keyObject_dicts
    def addKeyObjectDicts(self,validates):
        for validate in validates:
            self._keyObject_dicts.append(validate)
        return self._keyObject_dicts
    def getKeyObjectDicts(self):
        return self._keyObject_dicts

    def createKeyObjectDict(self):
        keyObject_dict=self._getObjectKeys_query_dict(self._object)
        return keyObject_dict


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

