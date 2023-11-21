# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ..library import dataLB as dLB
from ..library import objectLB as oLB
from ..library import appLB as aLB
from cgInTools.maya.library import meshLB as mLB
cit.reloads([dLB,oLB,aLB,mLB])

point_DataPoints=[
    dLB.DataPoint(-1,1,0),
    dLB.DataPoint(-1,0,0),
    dLB.DataPoint(1,0,0),
    dLB.DataPoint(1,1,0),
    dLB.DataPoint(1,2,0),
    dLB.DataPoint(-1,2,0)
]

face_lists=[
    [0,1,2,3],
    [0,3,4,5]
]

def createDataFaces(point_DataPoints):
    vertex_DataVertexs=[]
    for num,point_DataPoint in enumerate(point_DataPoints):
        vertex_DataVertex=dLB.DataVertex()
        vertex_DataVertex.setDataPoint(point_DataPoint)
        vertex_DataVertex.setID(num)
        vertex_DataVertexs.append(vertex_DataVertex)

    face_DataFaces=[]
    for num,face_list in enumerate(face_lists):
        index_DataVertexs=[vertex_DataVertexs[face_index] for face_index in face_list]
        face_DataFace=dLB.DataFace()
        face_DataFace.setDataVertexs(index_DataVertexs)
        face_DataFace.setID(num)
        face_DataFaces.append(face_DataFace)
    return face_DataFaces

def main():
    face_DataFaces=createDataFaces(point_DataPoints)
    mesh_DataMesh=dLB.DataMesh()
    mesh_DataMesh.setDataFaces(face_DataFaces)

    basis3D_DataPointArray=dLB.DataPointArray()
    basis3D_DataPointArray.setDataPoints(point_DataPoints)

    mesh=mLB.SelfMeshPolygon()
    mesh.setName("meshData")
    mesh.setDataPointArrayInBasis3D(basis3D_DataPointArray)
    mesh.setDataMesh(mesh_DataMesh)
    mesh.create()

main()