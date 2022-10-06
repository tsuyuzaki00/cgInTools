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
        self.min=0
        self.max=1
        self.defautValue=0
        self.attrLists=[]
        self.lah=True

#Public function
    def setObj(self,obj):
        self.obj=obj
        return self.obj

    def setAttrType(self,attrType):
        self.attrType=attrType
        return self.attrType

    def setName(self,name):
        self.name=name
        return self.name

    def setNiceName(self,niceName):
        self.niceName=niceName
        return self.niceName

    def setStringName(self,stringName):
        self.stringName=stringName
        return self.stringName

    def setEnums(self,enums):
        self.enums=enums
        return self.enums

    def setMin(self,min):
        self.min=min
        return self.min
    
    def setMax(self,max):
        self.max=max
        return self.max
    
    def setDefautValue(self,defautValue):
        self.defautValue=defautValue
        return self.defautValue

    def setHideAttrs(self,attrLists,lah=True):
        self.attrLists=attrLists
        self.lah=lah
        return self.attrLists

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
            self.addAttrBool_create_func(self.obj,self.name,self.niceName)
        elif self.attrType == "int":
            self.addAttrInt_create_func(self.obj,self.name,self.niceName,self.min,self.max,self.defautValue)
        elif self.attrType == "float":
            self.addAttrFloat_create_func(self.obj,self.name,self.niceName,self.min,self.max,self.defautValue)
        elif self.attrType == "string":
            self.addAttrString_create_func(self.obj,self.name,self.niceName,self.stringName)
        elif self.attrType == "enum":
            self.addAttrEnum_create_func(self.obj,self.name,self.niceName,self.enums)
        elif self.attrType == "vector":
            self.addAttrVector_create_func(self.obj,self.name,self.niceName)
        else:
            cmds.error('There is no attribute type "'+self.attrType+'".')

#Private function
    def addAttrVector_create_func(self,obj,name,niceName=None):
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

    def addAttrInt_create_func(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
    
    def addAttrFloat_create_func(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",min=min,max=max,dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
    
    def addAttrBool_create_func(self,obj,name,niceName=None):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="bool")
            cmds.setAttr(obj+"."+name,keyable=True)

    def addAttrString_create_func(self,obj,name,niceName=None,stringName="string"):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,stringName,type="string")
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,dt="string")
            cmds.setAttr(obj+"."+name,stringName,type="string")
    
    def addAttrEnum_create_func(self,obj,name,niceName=None,enums=["Green","Blue","Red"]):
        attr_bool=self.addAttr_check_bool(obj,name)
        enumSet=""
        for enum in enums:
            enumSet+=enum+":"
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="enum",en=enumSet)
            cmds.setAttr(obj+"."+name,keyable=True)

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
