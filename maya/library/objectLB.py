# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class jointWeight():
    def __init__(self):
        self._joint=""
        self._vertexsValue_list=[]#[(["",""],0),(["",""],0)]

    def __loading(self):
        self._parent_list=cmds.listRelatives(self._joint,p=True)
        self._skinCluster_list=cmds.listConnections(self._joint+".objectColorRGB",d=True)
        self._child_list=cmds.listRelatives(self._joint,c=True)

    def setJoint(self,variable):
        self._joint=variable
        self.__loading()
        return self._joint
    def getJoint(self):
        return self._joint
    
    def setVertexsValueList(self,variable):
        self._vertexsValue_list=[variable]
        return self._vertexsValue_list
    def addVertexsValueList(self,variable):
        self._vertexsValue_list.append(variable)
        return self._vertexsValue_list
    def getVertexsValueList(self):
        return self._vertexsValue_list

    def getParentList(self):
        return self._parent_list
    
    def getSkinClusterList(self):
        return self._skinCluster_list
    
    def getChildList(self):
        return self._child_list

    def loading(self):
        self.__loading()

def main():
    joint01=jointWeight()
    joint01.setJoint("joint1")
    joint01.setVertexsValueList((["test_geo.vtx[0:261]"],1))

    joint02=jointWeight()
    joint02.setJoint("joint2")
    joint02.setVertexsValueList((["test_geo.vtx[100:259]","test_geo.vtx[261]"],1))
    joint02.addVertexsValueList((["test_geo.vtx[80:99]"],0.8835))
    joint02.addVertexsValueList((["test_geo.vtx[60:79]"],0.4078))
    
    joint03=jointWeight()
    joint03.setJoint("joint3")
    joint03.setVertexsValueList((["test_geo.vtx[120:259]","test_geo.vtx[261]"],1))
    joint03.addVertexsValueList((["test_geo.vtx[100:119]"],0.5))
    
    joint04=jointWeight()
    joint04.setJoint("joint4")
    joint04.setVertexsValueList((["test_geo.vtx[160:259]","test_geo.vtx[261]"],1))
    joint04.addVertexsValueList((["test_geo.vtx[140:159]"],0.5))
    
    joint05=jointWeight()
    joint05.setJoint("joint5")
    joint05.setVertexsValueList((["test_geo.vtx[200:259]","test_geo.vtx[261]"],1))
    joint05.addVertexsValueList((["test_geo.vtx[180:199]"],0.5))

    #weights=[joint01,joint02,joint03]
    weights=[joint01,joint02,joint03,joint04,joint05]
    for weight in weights:
        cmds.setAttr(weight.getJoint()+".liw",0)
    for weight in weights:
        for vertexsValue in weight.getVertexsValueList():
            cmds.skinPercent(weight.getSkinClusterList()[0],vertexsValue[0],transformValue=[(weight.getJoint(),vertexsValue[1])],nrm=True)
        if not weight.getParentList() == None:
            cmds.setAttr(weight.getParentList()[0]+".liw",1)

#main()