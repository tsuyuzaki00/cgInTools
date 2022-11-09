# -*- coding: iso-8859-15 -*-

class SetName():
    def __init__(self):
        self.name=""
        self.node=""
        self.position=""
        self.number=00

    def setName(self,variable):
        self.name=variable
        return self.name

    def setNode(self,variable):
        self.node=variable
        return self.node

    def setPosition(self,variable):
        self.position=variable
        return self.position

    def setNumber(self,variable):
        self.number=variable
        return self.number

    def getName(self):
        return self.name

    def getNode(self):
        return self.node

    def getPosition(self):
        return self.position

    def getNumber(self):
        return self.number

class SetObject():
    def __init__(self):
        self.object=""
        self.parent=""
        self.childs=[]
        self.shape=""
        self.component=""
        self.attr=""
        self.parameter=0
        self.joint=""

    def setObject(self,variable):
        self.object=variable
        return self.object

    def setParent(self,variable):
        self.parent=variable
        return self.parent
    
    def setChilds(self,variable):
        self.childs=variable
        return self.childs

    def setShape(self,variable):
        self.shape=variable
        return self.shape

    def setComponent(self,variable):
        self.component=variable
        return self.component

    def setAttr(self,variable):
        self.attr=variable
        return self.attr

    def setParameter(self,variable):
        self.parameter=variable
        return self.parameter

    def setJoint(self,variable):
        self.joint=variable
        return self.joint

    def getObject(self):
        return self.object

    def getParent(self):
        return self.parent
    
    def getChilds(self):
        return self.childs

    def getShape(self):
        return self.shape

    def getComponent(self):
        return self.component

    def getAttr(self):
        return self.attr

    def getParameter(self):
        return self.parameter

    def getJoint(self):
        return self.joint

class SetPair():
    def __init__(self):
        self.sourceNode="" # string
        self.targetNode="" # string
        self.sourceAttr="" # string
        self.targetAttr="" # string
        self.sourceComponent=0 # int only
        self.targetComponent=0 # int only
        self.sourceParameter="" # float or string
        self.targetParameter="" # float or string
        self.sourceJoint="" # string
        self.targetJoint="" # string
        
    def sPathurceNode(self,variable):
        self.sourceNode=variable
        return self.sourceNode

    def setTargetNode(self,variable):
        self.targetNode=variable
        return self.targetNode

    def setSourceAttr(self,variable):
        self.sourceAttr=variable
        return self.sourceAttr

    def setTargetAttr(self,variable):
        self.targetAttr=variable
        return self.targetAttr

    def setSourceComponent(self,variable):
        self.sourceComponent=variable
        return self.sourceComponent

    def setTargetComponent(self,variable):
        self.targetComponent=variable
        return self.targetComponent

    def setSourceParameter(self,variable):
        self.sourceParameter=variable
        return self.sourceParameter

    def setTargetParameter(self,variable):
        self.targetParameter=variable
        return self.targetParameter

    def setSourceJoint(self,variable):
        self.sourceJoint=variable
        return self.sourceJoint

    def setTargetJoint(self,variable):
        self.targetJoint=variable
        return self.targetJoint

    def gPathurceNode(self):
        return self.sourceNode

    def getTargetNode(self):
        return self.targetNode

    def getSourceAttr(self):
        return self.sourceAttr

    def getTargetAttr(self):
        return self.targetAttr
    
    def getSourceJoint(self):
        return self.sourceJoint

    def getTargetJoint(self):
        return self.targetJoint

    def getSourceComponent(self):
        return self.sourceComponent

    def getTargetComponent(self):
        return self.targetComponent

    def getSourceParameter(self):
        return self.sourceParameter

    def getTargetParameter(self):
        return self.targetParameter

class SetFile():
    def __init__(self):
        self.path=""
        self.file=""
        self.extension=""
        self.packs=[]

    def setPath(self,variable):
        self.path=variable
        return self.path

    def setFile(self,variable):
        self.file=variable
        return self.file

    def setExtension(self,variable):
        self.extension=variable
        return self.extension

    def setPacks(self,variable):
        self.packs=variable
        return self.packs
    
    def getPath(self):
        return self.path

    def getFile(self):
        return self.file

    def getExtension(self):
        return self.extension
    
    def getPacks(self):
        return self.packs