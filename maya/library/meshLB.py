# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from . import appLB as aLB
from . import dataLB as dLB
cit.reloads([aLB,dLB])
class AppMeshPolygon(object):
    def __init__(self):
        self._name_str=None
        self._basis3D_DataPointArray=None
        self._mesh_DataMesh=None
        self._basis2D_DataPointArray=None
        self._shell_DataShell=None

    #Single Function
    def allVertex_query_Points(self,polygons):
        points=[point for polygon in polygons for point in polygon]
        
        seen_ids=set()
        unique_Points=[]
        for point in points:
            if point.getID() not in seen_ids:
                unique_Points.append(point)
                seen_ids.add(point.getID())

        sorted_Points=sorted(unique_Points,key=lambda x: x.getID())
        return sorted_Points

    def excludeSameVertex_query_DataPoints(self,dataMesh):
        vertex_DataVertexs=[vertex_DataVertex for face_DataFace in dataMesh.getDataFaces() for vertex_DataVertex in face_DataFace.getDataVertexs()]
        
        vertex_DataVertexs=sorted(vertex_DataVertexs,key=lambda x: x.getID())
        vertex_DataVertexs=list(set(vertex_DataVertexs))
        basisPoint_DataPoints=[vertex_DataVertex.getDataPoint() for vertex_DataVertex in vertex_DataVertexs]

        return basisPoint_DataPoints

    def faceInVertexCount_query_ints(self,dataMesh):
        faceInVertexCount_ints=[len(face_DataFace.getDataVertexs()) for face_DataFace in dataMesh.getDataFaces()]
        return faceInVertexCount_ints
    
    def pointID_query_ints(self,dataMesh):
        pointID_ints=[vertex_DataVertex.getDataPoint().getID() for face_DataFace in dataMesh.getDataFaces() for vertex_DataVertex in face_DataFace.getDataVertexs()]
        return pointID_ints

    def uvValues_query_list_list(self,dataMesh):
        faceCount_int=len(dataMesh.getDataFaces())
        uValues=[0,0,1,1]*faceCount_int
        vValues=[0,1,1,0]*faceCount_int
        return uValues,vValues

    def vertexNormal_query_DataVectors(self,dataMesh):
        vertexNormal_DataVectors=[vertex_DataVertex.getDataVector() for face_DataFace in dataMesh.getDataFaces() for vertex_DataVertex in face_DataFace.getDataVertexs()]
        return vertexNormal_DataVectors

    def faceID_query_ints(self,dataMesh):
        faceCount_int=len(dataMesh.getDataFaces())
        for face_DataFace in dataMesh.getDataFaces():
            vertex_DataVertexs=face_DataFace.getDataVertexs()
            vertexCount_int=len(vertex_DataVertexs)
        
        faceID_ints=[]
        for num in range(faceCount_int):
            faceID_ints+=[num]*vertexCount_int
        return faceID_ints

    #Setting Function
    def setName(self,variables):
        self._name_str=variables
        return self._name_str
    def getName(self):
        return self._name_str

    def setDataPointArrayInBasis3D(self,variable):
        self._basis3D_DataPointArray=variable
        return self._basis3D_DataPointArray
    def getDataPointArrayInBasis3D(self):
        return self._basis3D_DataPointArray
    
    def setDataPointArrayInBasis2D(self,variable):
        self._basis2D_DataPointArray=variable
        return self._basis2D_DataPointArray
    def getDataPointArrayInBasis2D(self):
        return self._basis2D_DataPointArray

    def setDataMesh(self,variable):
        self._mesh_DataMesh=variable
        return self._mesh_DataMesh
    def getDataMesh(self):
        return self._mesh_DataMesh

    def setDataShell(self,variable):
        self._shell_DataShell=variable
        return self._shell_DataShell
    def getDataShell(self):
        return self._shell_DataShell

    #Public Function
    def create(self):
        trans_MFnTransform=om2.MFnTransform()
        trans_MObject=trans_MFnTransform.create()
        transName_str=trans_MFnTransform.setName(self._name_str)
        mesh_MFnMesh=om2.MFnMesh()
        
        basisPoint_DataPoints=self._basis3D_DataPointArray.getDataPoints()
        #basisPoint_DataPoints=self.excludeSameVertex_query_DataPoints(self._mesh_DataMesh)
        polygonCount_ints=self.faceInVertexCount_query_ints(self._mesh_DataMesh)
        polygonConnects_ints=self.pointID_query_ints(self._mesh_DataMesh)
        uValues,vValues=self.uvValues_query_list_list(self._mesh_DataMesh)
        #vertexNormal_DataVectors=self.vertexNormal_query_DataVectors(self._mesh_DataMesh)
        #faceID_ints=self.faceID_query_ints(self._mesh_DataMesh)

        mesh_MFnMesh.create(basisPoint_DataPoints,polygonCount_ints,polygonConnects_ints,uValues,vValues,parent=trans_MObject)
        mesh_MFnMesh.setName(transName_str+'Shape')
        mesh_MFnMesh.assignUVs(polygonCount_ints,polygonConnects_ints)
        mesh_MFnMesh.unlockFaceVertexNormals([0],[0])
        #mesh_MFnMesh.setFaceVertexNormals(vertexNormal_DataVectors,faceID_ints,polygonConnects_ints)
        
        cmds.lockNode("initialShadingGroup",l=False,lu=False)
        cmds.sets(transName_str,e=True,forceElement="initialShadingGroup")