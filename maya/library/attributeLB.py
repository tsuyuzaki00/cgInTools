# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from . import setBaseLB as sbLB

class Attribute(sbLB.SetObject):
    def __init__(self):
        self._object=""
        self._attr=""
        self._value=0
        self._attrType="bool"
        self._stringName="string"
        self._enums=["Green","Blue","Red"]
        self._useMinMax=False
        self._min=0
        self._max=1
        self._attrs=[]
        self._haveAttr=""
        self._lockandhide=True
    
    def loading(self):
        self._niceName=self._attr.capitalize()

#Public function
    def getObjectAttr(self):
        return self._object+"."+self._haveAttr

    def setAttrType(self,variable):
        self._attrType=variable
        return self._attrType

    def setNiceName(self,variable):
        self._niceName=variable
        return self._niceName

    def setStringName(self,variable):
        self._stringName=variable
        return self._stringName

    def setEnums(self,variable):
        self._enums=variable
        return self._enums

    def setUseMinMax(self,variable):
        self._useMinMax=variable
        return self._useMinMax

    def setMin(self,variable):
        self._min=variable
        return self._min
    
    def setMax(self,variable):
        self._max=variable
        return self._max
    
    def setHaveAttr(self,variable):
        self._haveAttr=variable
        return self._haveAttr
    def getHaveAttr(self):
        return self._haveAttr
    def editHaveAttr(self,variable):
        cmds.setAttr(self._object+"."+self._haveAttr,variable)
    def delHaveAttr(self):
        cmds.deleteAttr(self._object+"."+self._haveAttr)

    def setHideAttrs(self,variable,lah=True):
        self._attrs=variable
        self._lockAndHide=lah
        return self._attrs

    def getKeyableAttrs(self,find=""):
        keyable_list=self.keyable_quary_list(self._object,find)
        return keyable_list

    def getLockAttrs(self,find=""):
        lock_list=self.lock_quary_list(self._object,find)
        return lock_list

    def lockAndHide(self):
        self.lockAndHide_edit_func(self._object,self._attrs,self._lockAndHide)
        return self._attrs
    
    def hide(self):
        self.hide_edit_func(self._object,self._attrs,self._lockAndHide)
        return self._attrs

    def addAttr(self):
        self.loading()
        if self._attrType == "bool":
            attrName=self.addAttrBool_create_attrName(self._object,self._attr,self._niceName)
            return attrName
        elif self._attrType == "int":
            if self._useMinMax:
                attrName=self.addAttrIntLimit_create_attrName(self._object,self._attr,self._niceName,self._min,self._max,self._value)
            else:
                attrName=self.addAttrInt_create_attrName(self._object,self._attr,self._niceName,self._value)
            return attrName
        elif self._attrType == "float":
            if self._useMinMax:
                attrName=self.addAttrFloatLimit_create_attrName(self._object,self._attr,self._niceName,self._min,self._max,self._value)
            else:
                attrName=self.addAttrFloat_create_attrName(self._object,self._attr,self._niceName,self._value)
            return attrName
        elif self._attrType == "string":
            attrName=self.addAttrString_create_attrName(self._object,self._attr,self._niceName,self._stringName)
            return attrName
        elif self._attrType == "enum":
            attrName=self.addAttrEnum_create_attrName(self._object,self._attr,self._niceName,self._enums,self._value)
            return attrName
        elif self._attrType == "vector":
            attrName=self.addAttrVector_create_attrName(self._object,self._attr,self._niceName)
            return attrName
        else:
            cmds.error('There is no attribute type "'+self._attrType+'".')

#Private function
    def addAttrVector_create_attrName(self,obj,name,niceName=None):
        attr_bool=self.addAttr_check_bool(obj,name)
        XYZs=["","X","Y","Z"]
        if not attr_bool:
            for xyz in XYZs:
                if xyz=="":
                    cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double3")
                else:
                    cmds.addAttr(obj,ln=name+xyz,nn=name.capitalize()+xyz or niceName+xyz,at="double",p=name)
        for xyz in XYZs:
            cmds.setAttr(obj+"."+name+xyz,keyable=True)
        return name

    def addAttrInt_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",dv=defaultValue)
        cmds.setAttr(obj+"."+name,keyable=True)
        return name
    
    def addAttrFloat_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",dv=defaultValue)
        cmds.setAttr(obj+"."+name,keyable=True)
        return name

    def addAttrIntLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
        cmds.setAttr(obj+"."+name,keyable=True)
        return name
    
    def addAttrFloatLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",min=min,max=max,dv=defaultValue)
        cmds.setAttr(obj+"."+name,keyable=True)
        return name
    
    def addAttrBool_create_attrName(self,obj,name,niceName=None):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="bool")
        cmds.setAttr(obj+"."+name,keyable=True)
        return name

    def addAttrString_create_attrName(self,obj,name,niceName=None,stringName="string"):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,dt="string")
        cmds.setAttr(obj+"."+name,stringName,type="string")
        return name
    
    def addAttrEnum_create_attrName(self,obj,name,niceName=None,enums=["Green","Blue","Red"],defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="enum",en=":".join(enums),dv=defaultValue)
        cmds.setAttr(obj+"."+name,keyable=True)
        return name

    def addAttr_check_bool(self,node,attr):
        attr_bool=cmds.attributeQuery(attr,node=node,exists=True)
        return attr_bool

    def hide_edit_func(self,obj,names,value=True):
        for name in names:
            cmds.setAttr(obj+"."+name,k=not value,cb=not value)

    def lockAndHide_edit_func(self,obj,names,value=True):
        for name in names:
            cmds.setAttr(obj+"."+name,l=value,k=not value,cb=not value)

    def keyable_quary_list(self,obj,findName=None):
        if findName is None or findName is "":
            attr_list=cmds.listAttr(obj,k=True)
            return attr_list
        else :
            attr_list=cmds.listAttr(obj,k=True)
            newNode_list=[node for node in attr_list if findName in node]
            return newNode_list

    def lock_quary_list(self,obj,findName=None):
        if findName is None or findName is "":
            attr_list=cmds.listAttr(obj,l=True)
            return attr_list
        else :
            attr_list=cmds.listAttr(obj,l=True)
            newNode_list=[node for node in attr_list if findName in node]
            return newNode_list
