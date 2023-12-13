# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ..library import dataLB as dLB
from ..library import selfLB as sLB
from cgInTools.maya.library import meshLB as mLB
cit.reloads([dLB,sLB,mLB])

def createDataFaces(point_tuples,face_dicts):
    point_DataPoints=[]
    for pointNum,point_tuple in enumerate(point_tuples):
        point_DataPoint=dLB.DataPoint(point_tuple)
        point_DataPoint.setID(pointNum)
        point_DataPoints.append(point_DataPoint)

    face_DataFaces=[]
    for faceNum,face_dict in enumerate(face_dicts):
        index_DataVertexs=[]
        for vertexNum,faceIndex_int in enumerate(face_dict.get("DataFace")):
            vertex_DataVertex=dLB.DataVertex()
            vertex_DataPoint=point_DataPoints[faceIndex_int]
            vertex_DataVertex.setDataPoint(vertex_DataPoint)
            vertex_DataVertex.setID(vertexNum)
            index_DataVertexs.append(vertex_DataVertex)
        
        face_DataVertexs=[]
        for index_DataVertex in index_DataVertexs:
            normal_DataVector=dLB.DataVector(face_dict.get("DataVector"))
            index_DataVertex.setDataVector(normal_DataVector)
            face_DataVertexs.append(index_DataVertex)
        
        face_DataFace=dLB.DataFace()
        face_DataFace.setDataVertexs(face_DataVertexs)
        face_DataFace.setID(faceNum)
        face_DataFaces.append(face_DataFace)
    return point_DataPoints,face_DataFaces

def main():
    point_tuples=[
        (-1,1,0),#0
        (-1,0,0),#1
        (1,0,0),#2
        (1,1,0),#3
        (1,1,-1),#4
        (-1,1,-1),#5
    ]

    face_dicts=[
        {
            "DataFace":[0,1,2,3],
            "DataVector":(0,0,1)
        },
        {
            "DataFace":[0,3,4,5],
            "DataVector":(0,1,0)
        }
    ]

    point_DataPoints,face_DataFaces=createDataFaces(point_tuples,face_dicts)
    
    basis3D_DataPointArray=dLB.DataPointArray()
    basis3D_DataPointArray.setDataPoints(point_DataPoints)
    
    mesh_DataMesh=dLB.DataMesh()
    mesh_DataMesh.setDataFaces(face_DataFaces)

    mesh=mLB.AppMeshPolygon()
    mesh.setName("meshData")
    mesh.setDataPointArrayInBasis3D(basis3D_DataPointArray)
    mesh.setDataMesh(mesh_DataMesh)
    mesh.create()

main()