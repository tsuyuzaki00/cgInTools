# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class DisplayLayer():
    def __init__(self):
        self._name="layer"
        self._parentObjs=[]

    def __loading(self):
        self._disLayerObjs=self.getInDisplayLayer_query_list(self._name)

    def setGrpName(self,variable):
        self._name=variable
        return self._name
    def getGrpName(self):
        return self._name

    def setParentObjs(self,variable):
        self._parentObjs=variable
        return self._parentObjs
    def addParentObjs(self,variable):
        self._parentObjs.append(variable)
        return self._parentObjs
    def getParentObjs(self):
        return self._parentObjs
        
    def getDisplayLayerObjs(self):
        return self._disLayerObjs

#Public Function
    def create(self):
        name=cmds.createDisplayLayer(n=self._name)
        cmds.editDisplayLayerMembers(name,self._parentObjs)
        self.__loading()
        return self._disLayerObjs

    def add(self):
        name=self.layerSence_check_string(self._name)
        cmds.editDisplayLayerMembers(name,self._parentObjs)
        self.__loading()
        return self._disLayerObjs

    def findChoiseName(self):
        pass

    def findChoiseType(self):
        pass

#Single Function
    def getInDisplayLayer_query_list(self,grpName):
        return cmds.editDisplayLayerMembers(grpName,q=True)
        
    def layerSence_check_string(self,layerName):
        displayLayers=cmds.ls(type="displayLayer")
        for displayLayer in displayLayers:
            if displayLayer == layerName:
                return layerName
        cmds.error("There is no name for the displayLayer "+"'"+layerName+"'")

