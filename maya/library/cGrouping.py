# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class GroupIng():
    def __init__(self):
        self.name="group"
        self.parentObjs=[]
        self.choisNames=[]
        self.searchType="transform"
        self.grpObjs=[]

    def setGrpName(self,variable):
        self.name=variable
        self.grpObjs=self.getInGroup_query_list(self.name)
        return self.name

    def setParentObjs(self,variable):
        self.parentObjs=variable
        return self.parentObjs

    def setChoisNames(self,variable):
        self.choisNames=variable
        return self.choisNames

    def setSearchType(self,variable):
        self.searchType=variable
        return self.searchType

    def addParentObjs(self,variable):
        self.parentObjs.append(variable)
        return self.parentObjs

    def group(self):
        groupName=cmds.group(self.parentObjs,n=self.name)
        self.grpObjs=self.getInGroup_query_list(groupName)
        return self.grpObjs

    def groupParent(self):
        name=self.objSence_check_string(self.name)
        cmds.parent(self.parentObjs,name)
        self.grpObjs=self.getInGroup_query_list(name)
        return self.grpObjs

    def queryGrpObjs(self):
        return self.grpObjs

    def choise(self):
        return self.grpNodeChoise_query_list(self,self.grpObjs,self.choisNames)

    def choiseType(self):
        return cmds.ls(self.grpObjs,type=self.searchType)
        
    def grpNodeChoise_query_list(self,grpNodes,choisNames):
        choiseNodes=[]
        for node in grpNodes:
            for choisName in choisNames:
                if choisName in node:
                    choiseNodes.append(node)
        return choiseNodes

    def getInGroup_query_list(self,grpName):
        grpNode_objs=cmds.ls(grpName,dag=True)
        if grpNode_objs == []:
            return grpNode_objs
        else :
            grpNode_list=list(grpNode_objs)
            grpNode_list.remove(grpName)
            return grpNode_list
        
    def objSence_check_string(objName):
        if cmds.objExists(objName):
            return objName
        else:
            cmds.error("There is no name for the group "+"'"+objName+"'")
