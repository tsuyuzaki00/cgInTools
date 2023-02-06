import maya.cmds as cmds

import cgInTools as cit
from . import objectLB as oLB
from . import jsonLB as jLB
cit.reloads([oLB,jLB])

class MatrixKey():
    def __init__(self):
        pass

class KeyObjects():
    def __init__(self):
        self._object=""
        self._keyObject_dicts=[]

    #Single Function
    def keyAttr_query_dicts(self,obj):
        keyAttr_dicts=[]
        keyAttrs=cmds.listAttr(obj,k=True)
        for keyAttr in keyAttrs:
            times=cmds.keyframe(obj,q=True,at=keyAttr)
            if not times == None:
                for time in times:
                    keyObject_dict={"object":obj,"attr":keyAttr,"time":time}
                    keyAttr_dicts.append(keyObject_dict)
        return keyAttr_dicts

    def keyObject_create_dict(self,obj,attr,time):
        keyObject=oLB.KeyObject(obj)
        keyObject.setAttr(attr)
        keyObject.setTime(time)
        keyObject.loading()
        nameSpace=keyObject.getObject().split(":")[0]
        objectName=keyObject.getObject().split(":")[-1]

        keyObject_dict={
            "nameSpace":nameSpace,
            "object":objectName,
            "attr":keyObject.getAttr(),
            "time":keyObject.getTime(),
            "value":keyObject.getValue(),
            "inTangentType":keyObject.getInTangentType(),
            "outTangentType":keyObject.getOutTangentType(),
            "animCurve":keyObject.getAnimCurve()
        }
        return keyObject_dict

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
        keyAttr_dicts=self.keyAttr_query_dicts(self._object)
        keys_dict={"keys":[]}
        for keyAttr_dict in keyAttr_dicts:
            keyObject_dict=self.keyObject_create_dict(keyAttr_dict["object"],keyAttr_dict["attr"],keyAttr_dict["time"])
            keys_dict["keys"].append(keyObject_dict)
        return keys_dict
