# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

"""
Attribute memo
アトリビュート自体を作成
アトリビュート自体の編集
"""
class Attribute():
    def __init__(self):
        self._longName_str=None
        self._shortName_str=None
        self._niceName_str=None
        self._value_value=None
        self._createType_str=None
        self._min_float=None
        self._max_float=None

    def __str__(self):
        return self._longName_str

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
    
    #Setting Function
    def setLongName(self,variable):
        self._longName_str=variable
        return self._longName_str
    def getLongName(self):
        return self._longName_str
    
    def setShortName(self,variable):
        self._shortName_str=variable
        return self._shortName_str
    def getShortName(self):
        return self._shortName_str

    def setNiceName(self,variable):
        self._niceName_str=variable
        return self._niceName_str
    def getNiceName(self):
        return self._niceName_str
    
    def setValue(self,variable):
        self._value_value=variable
        return self._value_value
    def getValue(self):
        return self._value_value

    def setCreateType(self,variable):
        self._createType_str=variable
        return self._createType_str
    def getCreateType(self):
        return self._createType_str

    def setKeyLockState(self,variable):
        self._keyLock_bool=variable
        return self._keyLock_bool
    def getKeyLockState(self):
        return self._keyLock_bool
    
    def setValueLockState(self,variable):
        self._valueLock_bool=variable
        return self._valueLock_bool
    def getValueLockState(self):
        return self._valueLock_bool
    
    def setHideState(self,variable):
        self._hide_bool=variable
        return self._hide_bool
    def getHideState(self):
        return self._hide_bool
    
    def setMinState(self,variable):
        self._min_bool=variable
        return self._min_bool
    def getMinState(self):
        return self._min_bool
    
    def setMaxState(self,variable):
        self._max_bool=variable
        return self._max_bool
    def getMaxState(self):
        return self._max_bool
    
    def setMinValue(self,variable):
        self._min_float=variable
        return self._min_float
    def getMinValue(self):
        return self._min_float
    
    def setMaxValue(self,variable):
        self._max_float=variable
        return self._max_float
    def getMaxValue(self):
        return self._max_float
    
    #Public Function
    def create(self):
        pass

    def edit(self):
        pass

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

    def createAttr(self):
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
    
"""
Plug memo
アトリビュートの変数の編集
アトリビュートの変数を取得
ノード同士のコネクト
アニメーションキーの設定
ドリブンキーの設定
"""
class Plug():
    def __init__(self):
        self._node_Node=None
        self._attr_Attribute=None
        self._animKey_Keys=[]
        self._target_Node=None
        self._source_Node=None

    #Setting Function
    def setNodeName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getNodeName(self):
        return self._nodeName_str
    
    def setAttribute(self,variable):
        self._attr_Attribute=variable
        return self._attr_Attribute
    def getAttribute(self):
        return self._attr_Attribute
    
    def setAnimKeys(self,variables):
        self._animKey_Keys=variables
        return self._animKey_Keys
    def addAnimKeys(self,variables):
        self._animKey_Keys+=variables
        return self._animKey_Keys
    def getAnimKeys(self):
        return self._animKey_Keys
    
    def setTargetNode(self,variable):
        self._target_Node=variable
        return self._target_Node
    def getTargetNode(self):
        return self._target_Node

    def setSourceNode(self,variable):
        self._source_Node=variable
        return self._source_Node
    def getSourceNode(self):
        return self._source_Node

    #Public Function
    def editAttr(self):
        pass
    
    def queryAttr(self):
        pass

    def connectTarget(self):
        pass
    
    def connectSource(self):
        pass

    def createAnimKey(self):
        pass

    def deleteAnimKey(self):
        pass