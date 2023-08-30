# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

class Point(om2.MPoint):
    def __init__(self,*points):
        super(Point,self).__init__(*points)
        self._point_list3=None
        self._id_int=None

    #Setting Function
    def setPosition(self,variables):
        self._point_list3=variables
        return self._point_list3
    def getPosition(self):
        return self._point_list3

    def setID(self,variable):
        self._id_int=variable
        return self._id_int
    def getID(self):
        return self._id_int
    def sameID(self,variable):
        if self._id_int is variable:
            return True
        else:
            return False


def setTargetPos_edit_obj(source,target):
    cmds.parent(source,target)
    cmds.move(0,0,0,ls=True)
    cmds.rotate(0,0,0,os=True)
    cmds.parent(source,w=True)

def vertexPos_query_func(vertexs):
    node_MSelectionList=om2.MSelectionList()
    for vertex in vertexs:
        node_MSelectionList.add(vertex)
    compo_MObject=node_MSelectionList.getComponent(0)[1]

    componentFn=om2.MFnSingleIndexedComponent(compo_MObject)
    verticesIndex=componentFn.elementCount
    verticeIDs=componentFn.getElements()

    compo_MDagPath=node_MSelectionList.getComponent(0)[0]
    mesh_MFnMesh=om2.MFnMesh(compo_MDagPath)

    for vertexID in verticeIDs:
        point=mesh_MFnMesh.getPoint(vertexID,om2.MSpace.kWorld)
        print("Vertex ID: ",vertexID, "Position: ",point)

def moveCenter(sources,targets):
    bb=cmds.xform(targets,q=True,bb=True)
    centerX=(bb[0]+bb[3])/2
    centerY=(bb[1]+bb[4])/2
    centerZ=(bb[2]+bb[5])/2
    for source in sources:
        cmds.move(centerX,centerY,centerZ,source,a=True)

def moveWorldPos(source,target):
    pos=cmds.xform(target,q=True,t=True,ws=True)
    cmds.move(pos[0],pos[1],pos[2],source,a=True)