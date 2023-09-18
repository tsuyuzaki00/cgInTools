import maya.cmds as cmds

import cgInTools as cit
from . import objectLB as oLB
from . import jsonLB as jLB
cit.reloads([oLB,jLB])

class Key():
    def __init__(self):
        self._influenceValue_value=None
        self._myValue_value=None
        self._inTangentType_int=None
        self._outTangentType_int=None

class SelfAttributeKey():
    def __init__(self):
        #self._node=None
        #self._attr=None
        pass

    def keyable(self):
        pass

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

class KeyObject():
    def __init__(self,obj):
        super(KeyObject,self).__init__(obj)
        self._time=oma2.MAnimControl.currentTime()
        self._attr=""
        self._value=0.0 #Float. Rotation values are in radians.
        self._inTangentType=0
        self._outTangentType=0
        self._animCurve=8

        self._animTangentReplaceID_dict=RULES_DICT["animTangentReplaceID_dict"]
        self._animTangentReplaceType_list=RULES_DICT["animTangentReplaceType_list"]
        self._animCurveReplaceID_dict=RULES_DICT["animCurveReplaceID_dict"]
        self._animCurveReplaceType_list=RULES_DICT["animCurveReplaceType_list"]

    #Single Function
    def objAttr_query_MFnAnimCurve(self,MObject,attr):
        obj_MFnDependencyNode=om2.MFnDependencyNode(MObject)
        objAttr_MPlug=obj_MFnDependencyNode.findPlug(attr,False)
        objAttr_MFnAnimCurve=oma2.MFnAnimCurve(objAttr_MPlug)
        return objAttr_MFnAnimCurve

    #Multi Function
    def _attrValue_query_float(self,MObject,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(MObject,attr)
        value=objAttr_MFnAnimCurve.evaluate(MTime)
        return value

    def _inTangentType_query_int(self,MObject,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(MObject,attr)
        index=objAttr_MFnAnimCurve.find(MTime)
        inTangentTypeID_int=objAttr_MFnAnimCurve.inTangentType(index)
        return inTangentTypeID_int

    def _outTangentType_query_int(self,MObject,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(MObject,attr)
        index=objAttr_MFnAnimCurve.find(MTime)
        outTangentTypeID_int=objAttr_MFnAnimCurve.outTangentType(index)
        return outTangentTypeID_int

    def _keyFrame_create_func(self,MObject,attr,value,MTime,inTangentTypeID,outTangentTypeID,animCurve):
        obj_MFnDependencyNode=om2.MFnDependencyNode(MObject)
        objAttr_MPlug=obj_MFnDependencyNode.findPlug(attr,False)
        object_str=obj_MFnDependencyNode.name()

        if not objAttr_MPlug.isDestination:
            animCurve_MFnAnimCurve=oma2.MFnAnimCurve()
            animCurve_MObject=animCurve_MFnAnimCurve.create(animCurve)
            animCurve_MFnDependencyNode=om2.MFnDependencyNode(animCurve_MObject)
            animCurve_MFnDependencyNode.setName(object_str+"_"+attr)
            animCurve_MPlug=animCurve_MFnDependencyNode.findPlug("output",False)

            keyConnect_MDGModifier=om2.MDGModifier()
            keyConnect_MDGModifier.connect(animCurve_MPlug,objAttr_MPlug)
            keyConnect_MDGModifier.doIt()
        
        objAttr_MFnAnimCurve=oma2.MFnAnimCurve(objAttr_MPlug)
        objAttr_MFnAnimCurve.addKey(MTime,value,inTangentTypeID,outTangentTypeID)

    #Public Function
    def __loading(self):
        self._value=self._attrValue_query_float(self._object_MObject,self._attr,self._time)
        self._inTangentType=self._inTangentType_query_int(self._object_MObject,self._attr,self._time)
        self._outTangentType=self._outTangentType_query_int(self._object_MObject,self._attr,self._time)
        self.setCurrentAnimCurve()

    def setAttr(self,variable):
        self._attr=variable
        return self._attr
    def getAttr(self):
        return self._attr

    def setTime(self,variable):
        fpsUnitType_int=om2.MTime.uiUnit()
        MTime=om2.MTime(variable,fpsUnitType_int)
        self._time=MTime
        return self._time
    def setCurrentTime(self):
        self._time=oma2.MAnimControl.currentTime()
        return self._time
    def getTime(self,unit=None):
        fpsUnitType_int=unit or om2.MTime.uiUnit()
        time=self._time.asUnits(fpsUnitType_int)
        return time

    def setValue(self,variable):
        self._value=variable
        return self._value
    def setCurrentValue(self,unit=None):
        MTime=oma2.MAnimControl.currentTime()
        self._value=self._attrValue_query_float(self._object_MObject,attr,MTime)
        return self._value
    def getValue(self):
        return self._value

    def setInTangentType(self,variable):
        self._inTangentType=self._animTangentReplaceID_dict[variable]
        return self._inTangentType
    def setCurrentInTangentType(self):
        MTime=oma2.MAnimControl.currentTime()
        self._inTangentType=self._inTangentType_query_int(self._object_MObject,self._attr,MTime)
        return self._inTangentType
    def getInTangentType(self):
        inTangentType=self._animTangentReplaceType_list[self._inTangentType]
        return inTangentType
    
    def setOutTangentType(self,variable):
        self._outTangentType=self._animTangentReplaceID_dict[variable]
        return self._outTangentType
    def setCurrentOutTangentType(self):
        MTime=oma2.MAnimControl.currentTime()
        self._outTangentType=self._outTangentType_query_int(self._object_MObject,self._attr,MTime)
        return self._outTangentType
    def getOutTangentType(self):
        outTangentType=self._animTangentReplaceType_list[self._outTangentType]
        return outTangentType
    
    def setAnimCurve(self,variable):
        self._animCurve=self._animCurveReplaceID_dict[variable]
        return self._animCurve
    def setCurrentAnimCurve(self):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(self._object_MObject,self._attr)
        self._animCurve=objAttr_MFnAnimCurve.animCurveType
        return self._animCurve
    def getAnimCurve(self):
        animCurve=self._animCurveReplaceType_list[self._animCurve]
        return animCurve

    def loading(self):
        self.__loading()

    def setKey(self):
        self._keyFrame_create_func(self._object_MObject,self._attr,self._value,self._time,self._inTangentType,self._outTangentType,self._animCurve)