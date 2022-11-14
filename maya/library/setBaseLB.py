# -*- coding: iso-8859-15 -*-

class SetName():
    def __init__(self):
        self._object=""
        self._name=""
        self._title=""
        self._node=""
        self._side=""
        self._hierarchy=""
        self._number=00
        self.test=""

    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setName(self,variable):
        self._name=variable
        return self._name
    def getName(self):
        return self._name
    
    def setTitle(self,variable):
        self._title=variable
        return self._title
    def getTitle(self):
        return self._title

    def setNode(self,variable):
        self._node=variable
        return self._node
    def getNode(self):
        return self._node

    def setSide(self,variable):
        self._side=variable
        return self._side
    def getSide(self):
        return self._side

    def setHierarchy(self,variable):
        self._hierarchy=variable
        return self._hierarchy
    def getSide(self):
        return self._hierarchy

    def setNumber(self,variable):
        self._number=variable
        return self._number
    def getNumber(self):
        return self._number

class SetObject():
    def __init__(self):
        self._object=""
        self._parent=""
        self._childs=[]
        self._shape=""
        self._component=""
        self._attr=""
        self._value=0
        self._joint=""

    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setParent(self,variable):
        self._parent=variable
        return self._parent
    def getParent(self):
        return self._parent
    
    def setChilds(self,variable):
        self._childs=variable
        return self._childs
    def getChilds(self):
        return self._childs

    def setShape(self,variable):
        self._shape=variable
        return self._shape
    def getShape(self):
        return self._shape

    def setComponent(self,variable):
        self._component=variable
        return self._component
    def getComponent(self):
        return self._component

    def setAttr(self,variable):
        self._attr=variable
        return self._attr
    def getAttr(self):
        return self._attr

    def setValue(self,variable):
        self._value=variable
        return self._value
    def getValue(self):
        return self._value

    def setJoint(self,variable):
        self._joint=variable
        return self._joint
    def getJoint(self):
        return self._joint

class SetPair():
    def __init__(self):
        self._sourceNode="" # string
        self._targetNode="" # string
        self._sourceAttr="" # string
        self._targetAttr="" # string
        self._sourceComponent=0 # int only
        self._targetComponent=0 # int only
        self._sourceValue="" # float or string
        self._targetValue="" # float or string
        self._sourceJoint="" # string
        self._targetJoint="" # string
        
    def setSourceNode(self,variable):
        self._sourceNode=variable
        return self._sourceNode
    def getSourceNode(self):
        return self._sourceNode

    def setTargetNode(self,variable):
        self._targetNode=variable
        return self._targetNode
    def getTargetNode(self):
        return self._targetNode

    def setSourceAttr(self,variable):
        self._sourceAttr=variable
        return self._sourceAttr
    def getSourceAttr(self):
        return self._sourceAttr

    def setTargetAttr(self,variable):
        self._targetAttr=variable
        return self._targetAttr
    def getTargetAttr(self):
        return self._targetAttr

    def setSourceComponent(self,variable):
        self._sourceComponent=variable
        return self._sourceComponent
    def getSourceComponent(self):
        return self._sourceComponent

    def setTargetComponent(self,variable):
        self._targetComponent=variable
        return self._targetComponent
    def getTargetComponent(self):
        return self._targetComponent

    def setSourceValue(self,variable):
        self._sourceValue=variable
        return self._sourceValue
    def getSourceValue(self):
        return self._sourceValue

    def setTargetValue(self,variable):
        self._targetValue=variable
        return self._targetValue
    def getTargetValue(self):
        return self._targetValue

    def setSourceJoint(self,variable):
        self._sourceJoint=variable
        return self._sourceJoint
    def getSourceJoint(self):
        return self._sourceJoint

    def setTargetJoint(self,variable):
        self._targetJoint=variable
        return self._targetJoint
    def getTargetJoint(self):
        return self._targetJoint

class SetFile():
    def __init__(self):
        self._path=""
        self._file=""
        self._extension="json"
        self._packs=[]

    def setPath(self,variable):
        self._path=variable
        return self._path
    def getPath(self):
        return self._path

    def setFile(self,variable):
        self._file=variable
        return self._file
    def getFile(self):
        return self._file

    def setExtension(self,variable):
        self._extension=variable
        return self._extension
    def getExtension(self):
        return self._extension

    def setPacks(self,variable):
        self._packs=variable
        return self._packs
    def getPacks(self):
        return self._packs
