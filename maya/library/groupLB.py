# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class Group():
    def __init__(self):
        self._name="group"
        self._parentObjs=[]
        self._choiseNames=[]
        self._choiseType="transform"

    def __loading(self):
        self._grpObjs=self.getInGroup_query_list(self._name)

    def setGrpName(self,variable):
        self._name=variable
        return self._name

    def setParentObjs(self,variable):
        self._parentObjs=variable
        return self._parentObjs
    def addParentObjs(self,variable):
        self._parentObjs.append(variable)
        return self._parentObjs

    def setChoisNames(self,variable):
        self._choiseNames=variable
        return self._choiseNames

    def setSearchType(self,variable):
        self._choiseType=variable
        return self._choiseType
    
    def getGrpObjs(self):
        return self._grpObjs

#Public Function
    def group(self):
        cmds.group(self._parentObjs,n=self._name)
        self.__loading()
        return self._grpObjs

    def groupParent(self):
        name=self.objSence_check_string(self._name)
        cmds.parent(self._parentObjs,name)
        self.__loading()
        return self._grpObjs

    def getGrpChoiseName(self):
        return self.grpNodeChoise_query_list(self,self._grpObjs,self._choiseNames)

    def getGrpChoiseType(self):
        return cmds.ls(self._grpObjs,type=self._choiseType)
        
    def findChoiseName(self):
        pass

    def findChoiseType(self):
        pass

#Single Function
    def grpNodeChoise_query_list(self,grpNodes,choisNames):
        choiseNodes=[]
        for node in grpNodes:
            for choisName in choisNames:
                if choisName in node:
                    choiseNodes.append(node)
        return choiseNodes

    def getInGroup_query_list(self,grpName):
        return cmds.listRelatives(grpName,ad=True)
        
    def objSence_check_string(objName):
        if cmds.objExists(objName):
            return objName
        else:
            cmds.error("There is no name for the group "+"'"+objName+"'")