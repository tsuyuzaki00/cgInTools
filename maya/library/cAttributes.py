# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class Attrebute():
    def __init__(self,object):
        self.obj=object

    def addAttrVector_create_func(self,name,niceName=None):
        cmds.addAttr(self.obj,ln=name,nn=niceName or name.capitalize(),at="double3")
        cmds.addAttr(self.obj,ln=name+"X",nn=niceName or name.capitalize()+"X",at="double",p=name)
        cmds.addAttr(self.obj,ln=name+"Y",nn=niceName or name.capitalize()+"Y",at="double",p=name)
        cmds.addAttr(self.obj,ln=name+"Z",nn=niceName or name.capitalize()+"Z",at="double",p=name)
        cmds.setAttr(self.obj+"."+name,keyable=True)
        cmds.setAttr(self.obj+"."+name+"X",keyable=True)
        cmds.setAttr(self.obj+"."+name+"Y",keyable=True)
        cmds.setAttr(self.obj+"."+name+"Z",keyable=True)

    def addAttrInt_create_func(self,name,niceName=None,min=0,max=1,defaultValue=0):
        cmds.addAttr(self.obj,ln=name,nn=niceName or name.capitalize(),at="long",min=min,max=max,dv=defaultValue)
        cmds.setAttr(self.obj+"."+name,keyable=True)
    
    def addAttrFroat_create_func(self,name,niceName=None,min=0,max=1,defaultValue=0):
        cmds.addAttr(self.obj,ln=name,nn=niceName or name.capitalize(),at="double",min=min,max=max,dv=defaultValue)
        cmds.setAttr(self.obj+"."+name,keyable=True)
    
    def addAttrBool_create_func(self,name,niceName=None):
        cmds.addAttr(self.obj,ln=name,nn=niceName or name.capitalize(),at="bool")
        cmds.setAttr(self.obj+"."+name,keyable=True)
    
    def addAttrEnum_create_func(self,name,niceName=None,enums=["Green","Blue","Red"]):
        enumSet=""
        for enum in enums:
            enumSet+=enum+":"
        cmds.addAttr(self,ln=name,nn=niceName or name.capitalize(),at="enum",en=enumSet)
        cmds.setAttr(self+"."+name,keyable=True)

    def lockAndHide_edit_func(self,names,value=True):
        for name in names:
            cmds.setAttr(self.obj+"."+name,l=value,k=not value,cb=not value)

    def keyable_quary_list(self,findName=None,keyable=True):
        if findName is None or findName is "":
            attr_list=cmds.listAttr(self.obj,k=keyable)
            return attr_list
        else :
            attr_list=cmds.listAttr(self.obj,k=keyable)
            newNode_list=[node for node in attr_list if findName in node]
            return newNode_list

    def lock_quary_list(self,findName=None,lock=True):
        if findName is None or findName is "":
            attr_list=cmds.listAttr(self.obj,l=lock)
            return attr_list
        else :
            attr_list=cmds.listAttr(self.obj,l=lock)
            newNode_list=[node for node in attr_list if findName in node]
            return newNode_list
