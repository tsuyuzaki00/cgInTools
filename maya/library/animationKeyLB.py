import maya.cmds as cmds

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

class EditKey():
    def __init__(self):
        self._path=""
        self._file=""
        self._object=""
        self._keyObject_dicts=[]

    def getKeyObject_query_dicts(self,obj):
        keyAttrs=cmds.listAttr(obj,k=True)
        name=obj.split(":")[-1]
        keys_dict={"keys":[]}
        for keyAttr in keyAttrs:
            times=cmds.keyframe(q=True,at=keyAttr)
            if not times == None:
                for time in times:
                    value=cmds.getAttr(obj+"."+keyAttr,t=time)
                    inType=cmds.keyTangent(obj,q=True,at=keyAttr,itt=True,t=(time,time))
                    outType=cmds.keyTangent(obj,q=True,at=keyAttr,ott=True,t=(time,time))
                    keyObject_dict={"object":name,"attr":keyAttr,"time":time,"value":value,"inTangentType":inType[0],"outTangentType":outType[0]}
                    keys_dict["keys"].append(keyObject_dict)
        return keys_dict

    def importJson_query_dict(self,path,file,extension):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting_dict=setting.read()
        return setting_dict

    def exportJson_edit_func(self,path,file,extension,keyObject_dicts):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setExtension(extension)
        for keyObject_dict in keyObject_dicts:
            write_dict={
                "object":keyObject_dict.getObject(),
                "attr":keyObject_dict.getAttr(),
                "time":keyObject_dict.getTime(),
                "value":keyObject_dict.getValue(),
                "inTangentType":keyObject_dict.getInTangentType(),
                "outTangentType":keyObject_dict.getOutTangentType()
            }
            setting.setWritePackDict(write_dict,keyObject_dict.getObject())
        setting.writePacks()

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
    def getOutTangentType(self):
        return self._keyObject_dicts

    def __import(self):
        pass

    def __export(self):
        self.exportJson_edit_func(self._path,self._file,extension="anim",keyObject_dicts=self._keyObject_dicts)

    def getKeyObjectDicts(self):
        keyObject_dicts=self.getKeyObject_query_dicts(self._object)
        return keyObject_dicts

    def export(self):
        self.__export()


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

