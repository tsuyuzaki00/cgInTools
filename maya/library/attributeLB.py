# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
from . import setBaseLB as sbLB

class Attribute(sbLB.BaseObject):
    def __init__(self):
        super(Attribute,self).__init__()

    #Single Function
    def addAttr_check_bool(self,node,attr):
        attr_bool=cmds.attributeQuery(attr,node=node,exists=True)
        return attr_bool

    def addAttrVector_create_attrName(self,obj,name,niceName=None):
        XYZs=["","X","Y","Z"]
        for xyz in XYZs:
            if xyz=="":
                cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double3")
            else:
                cmds.addAttr(obj,ln=name+xyz,nn=name.capitalize()+xyz or niceName+xyz,at="double",p=name)
        for xyz in XYZs:
            cmds.setAttr(obj+"."+name+xyz,keyable=True)
        return name

    def addAttrInt_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",dv=defaultValue)
        return name
    
    def addAttrFloat_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",dv=defaultValue)
        return name

    def addAttrIntLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
        return name
    
    def addAttrFloatLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",min=min,max=max,dv=defaultValue)
        return name
    
    def addAttrBool_create_attrName(self,obj,name,niceName=None):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="bool")
        return name

    def addAttrString_create_attrName(self,obj,name,niceName=None):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,dt="string")
        return name
    
    def addAttrEnum_create_attrName(self,obj,name,niceName=None,enums=["Green","Blue","Red"],defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="enum",en=":".join(enums),dv=defaultValue)
        return name

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

    def isProxy_edit_nodeAttr(self,obj,attr,proxy=False):
        if cmds.addAttr(obj+"."+attr,q=True,usedAsProxy=True) == None:
            cmds.error("Cannot be set for standard attributes.")
        nodeAttr=obj+"."+attr
        nodeAttr_MSelectionList=om2.MSelectionList().add(nodeAttr)
        nodeAttr_MPlug=nodeAttr_MSelectionList.getPlug(0)
        nodeAttr_MFnAttribute=om2.MFnAttribute(nodeAttr_MPlug.attribute())
        nodeAttr_MFnAttribute.isProxyAttribute=proxy
        return nodeAttr
    
    #Public Function
    def __loading(self):
        self._niceName=self._attr.capitalize()

    def getKeyableAttrs(self,find=""):
        keyable_list=self.keyable_quary_list(self._object,find)
        return keyable_list

    def getLockAttrs(self,find=""):
        lock_list=self.lock_quary_list(self._object,find)
        return lock_list

    def lockAndHide(self):
        cmds.setAttr(self._object+"."+self._attr,l=self._lockAndHide,k=not self._lockAndHide,cb=not self._lockAndHide)
        return self._attr
    
    def hide(self):
        cmds.setAttr(self._object+"."+self._attr,k=not self._lockAndHide,cb=not self._lockAndHide)
        return self._attr

    def addAttr(self):
        self.__loading()
        attr_bool=self.addAttr_check_bool(self._object,self._attr)
        if not attr_bool:
            if self._attrType == "bool":
                attrName=self.addAttrBool_create_attrName(self._object,self._attr,self._niceName)
            elif self._attrType == "int":
                if self._useMinMax:
                    attrName=self.addAttrIntLimit_create_attrName(self._object,self._attr,self._niceName,self._min,self._max,self._value)
                else:
                    attrName=self.addAttrInt_create_attrName(self._object,self._attr,self._niceName,self._value)
            elif self._attrType == "float":
                if self._useMinMax:
                    attrName=self.addAttrFloatLimit_create_attrName(self._object,self._attr,self._niceName,self._min,self._max,self._value)
                else:
                    attrName=self.addAttrFloat_create_attrName(self._object,self._attr,self._niceName,self._value)
            elif self._attrType == "string":
                attrName=self.addAttrString_create_attrName(self._object,self._attr,self._niceName,self._stringName)
            elif self._attrType == "enum":
                attrName=self.addAttrEnum_create_attrName(self._object,self._attr,self._niceName,self._enums,self._value)
            elif self._attrType == "vector":
                attrName=self.addAttrVector_create_attrName(self._object,self._attr,self._niceName)
            else:
                cmds.error('There is no attribute type "'+self._attrType+'".')
        cmds.setAttr(self._object+"."+self._attr,keyable=True)
        return attrName

    def isProxy(self):
        nodeAttr=self.isProxy_edit_nodeAttr(self._object,self._attr,self._proxy)
        return nodeAttr