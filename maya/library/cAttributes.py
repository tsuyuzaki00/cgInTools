# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class Attribute():
    def __init__(self):
        self.obj="null"
        self.attrType="bool"
        self.name="name"
        self.niceName=self.name.capitalize()
        self.stringName="string"
        self.enums=["Green","Blue","Red"]
        self.useMinMax=False
        self.min=0
        self.max=1
        self.defautValue=0
        self.attrLists=[]
        self.haveAttr=""
        self.lah=True

#Public function
    def setObj(self,variable):
        self.obj=variable
        return self.obj

    def setAttrType(self,variable):
        self.attrType=variable
        return self.attrType

    def setName(self,variable):
        self.name=variable
        return self.name

    def setNiceName(self,variable):
        self.niceName=variable
        return self.niceName

    def setStringName(self,variable):
        self.stringName=variable
        return self.stringName

    def setEnums(self,variable):
        self.enums=variable
        return self.enums

    def setMin(self,variable):
        self.min=variable
        return self.min
    
    def setMax(self,variable):
        self.max=variable
        return self.max

    def setUseMinMax(self,variable):
        self.useMinMax=variable
        return self.useMinMax

    def setHaveAttr(self,variable):
        self.haveAttr=variable
        return self.haveAttr
    
    def setDefautValue(self,variable):
        self.defautValue=variable
        return self.defautValue

    def setHideAttrs(self,variable,lah=True):
        self.attrLists=variable
        self.lah=lah
        return self.attrLists

    def getCreateAttr(self):
        return self.haveAttr
    
    def getObjAttr(self):
        return self.obj+"."+self.haveAttr

    def getKeyableAttrs(self,find=""):
        keyable_list=self.keyable_quary_list(self.obj,find)
        return keyable_list

    def getLockAttrs(self,find=""):
        lock_list=self.lock_quary_list(self.obj,find)
        return lock_list

    def lockAndHide(self):
        self.lockAndHide_edit_func(self.obj,self.attrLists,self.lah)
        return self.attrLists
    
    def hide(self):
        self.hide_edit_func(self.obj,self.attrLists,self.lah)
        return self.attrLists

    def addAttr(self):
        if self.attrType == "bool":
            attrName=self.addAttrBool_create_attrName(self.obj,self.name,self.niceName)
            return attrName
        elif self.attrType == "int":
            if self.useMinMax:
                attrName=self.addAttrIntLimit_create_attrName(self.obj,self.name,self.niceName,self.min,self.max,self.defautValue)
            else:
                attrName=self.addAttrInt_create_attrName(self.obj,self.name,self.niceName,self.defautValue)
            return attrName
        elif self.attrType == "float":
            if self.useMinMax:
                attrName=self.addAttrFloatLimit_create_attrName(self.obj,self.name,self.niceName,self.min,self.max,self.defautValue)
            else:
                attrName=self.addAttrFloat_create_attrName(self.obj,self.name,self.niceName,self.defautValue)
            return attrName
        elif self.attrType == "string":
            attrName=self.addAttrString_create_attrName(self.obj,self.name,self.niceName,self.stringName)
            return attrName
        elif self.attrType == "enum":
            attrName=self.addAttrEnum_create_attrName(self.obj,self.name,self.niceName,self.enums)
            return attrName
        elif self.attrType == "vector":
            attrName=self.addAttrVector_create_attrName(self.obj,self.name,self.niceName)
            return attrName
        else:
            cmds.error('There is no attribute type "'+self.attrType+'".')

    def editHaveAttr(self,variable):
        cmds.setAttr(self.obj+"."+self.haveAttr,variable)

    def delHaveAttr(self):
        cmds.deleteAttr(self.obj+"."+self.haveAttr)

#Private function
    def addAttrVector_create_attrName(self,obj,name,niceName=None):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
            cmds.setAttr(obj+"."+name+"X",keyable=True)
            cmds.setAttr(obj+"."+name+"Y",keyable=True)
            cmds.setAttr(obj+"."+name+"Z",keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double3")
            cmds.addAttr(obj,ln=name+"X",nn=name.capitalize() or niceName+"X",at="double",p=name)
            cmds.addAttr(obj,ln=name+"Y",nn=name.capitalize() or niceName+"Y",at="double",p=name)
            cmds.addAttr(obj,ln=name+"Z",nn=name.capitalize() or niceName+"Z",at="double",p=name)
            cmds.setAttr(obj+"."+name,keyable=True)
            cmds.setAttr(obj+"."+name+"X",keyable=True)
            cmds.setAttr(obj+"."+name+"Y",keyable=True)
            cmds.setAttr(obj+"."+name+"Z",keyable=True)
        return name

    def addAttrInt_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
        return name
    
    def addAttrFloat_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
        return name

    def addAttrIntLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
        return name
    
    def addAttrFloatLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",min=min,max=max,dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
        return name
    
    def addAttrBool_create_attrName(self,obj,name,niceName=None):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="bool")
            cmds.setAttr(obj+"."+name,keyable=True)
        return name

    def addAttrString_create_attrName(self,obj,name,niceName=None,stringName="string"):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,stringName,type="string")
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,dt="string")
            cmds.setAttr(obj+"."+name,stringName,type="string")
        return name
    
    def addAttrEnum_create_attrName(self,obj,name,niceName=None,enums=["Green","Blue","Red"]):
        attr_bool=self.addAttr_check_bool(obj,name)
        enumSet=""
        for enum in enums:
            enumSet+=enum+":"
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="enum",en=enumSet)
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
