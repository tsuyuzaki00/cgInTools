# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

class Polygon(object):
    def __init__(self):
        self._name_str=None
        self._polygons=None#[[MPoint,MPoint,MPoint,MPoint],[MPoint,MPoint,MPoint,MPoint]]

    #Single Function
    def allVertex_query_MPoints(self,polygons):
        points=[point for polygon in polygons for point in polygon]
        unique_Points=[item for index, item in enumerate(points) if item not in points[:index]]
        sorted_Points=[] 
        for unique_Point in unique_Points:
            for i in range(len(unique_Points)):
                if unique_Point.sameID(i):
                    sorted_Points.append(unique_Point)
        #hikaku=[point.getID() for point in points]
        #unique_Points=set(hikaku)

        #for index, item in enumerate(points):
        #    if item not in points[:index]:
        #        print(item.getID())
        return sorted_Points

    def polygonCount_query_ints(self,polygons):
        polygonCounts=[len(polygon) for polygon in polygons]
        return polygonCounts
    
    def pointID_query_ints(self,polygons):
        #pointIDs=[]
        #for polygon in polygons:
        #    for point in polygon:
        #        id_int=point.getID()
        #        pointIDs.append(id_int)
        pointIDs=[point.getID() for polygon in polygons for point in polygon]
        return pointIDs

    #Setting Function
    def setName(self,variables):
        self._name_str=variables
        return self._name_str
    def getName(self):
        return self._name_str

    def setPolygons(self,variables):
        self._polygons=variables
        return self._polygons
    def getPolygons(self):
        return self._polygons

    #Public Function
    def create(self,vertices):
        trans_fn=om2.MFnTransform()
        trans_obj=trans_fn.create()
        _name_str=trans_fn.setName(self._name_str)
        fn_mesh=om2.MFnMesh()

        #vertices=self.allVertex_query_MPoints(self._polygons)
        polygonCounts=self.polygonCount_query_ints(self._polygons)

        fn_mesh.create(vertices,polygonCounts,polygonConnects,parent=trans_obj)
        fn_mesh.setName(_name_str+'Shape')

class CreateMesh():
    def __init__(self):
        self.name=""
        self.mPointArray=None
        self.mFnMesh=""
        self.faceIDs=[]

    def setName(self,name):
        self.name=name
        return self.name

    def setMPointArray(self,mPointArray):
        self.mPointArray=mPointArray
        return self.mPointArray
    
    def setFaceIDs(self,faceIDs):
        self.faceIDs=faceIDs
        return self.faceIDs
    
    def queryFaceIDs(self):
        return self.faceIDs

    def create(self):
        self.mFnMesh=om2.MFnMesh()
        for mPoints in self.mPointArray:
            faceId=self.mFnMesh.addPolygon(mPoints)
            self.faceIDs.append(faceId)

    def edit(self):
        self.faceIDs=[]
        for mPoints in self.mPointArray:
            faceId=self.mFnMesh.addPolygon(mPoints)
            self.faceIDs.append(faceId)

    #Private
    def replacePointListToMPoint_edit_MPoint_list(self,point_lists=[(1,1,0,1),(-1,1,0,1),(-1,-1,0,1),(1,-1,0,1)]):
        createPlane=[]
        for point in point_lists:
            append_MFloatPoint=om2.MFloatPoint(point[0],point[1],point[2],point[3])
            createPlane.append(append_MFloatPoint)
        return createPlane


class GetFaceVertexs:
    def __init__(self):
        self.obj=""
        self.faceIDs=[]

    #Public
    def setObj(self,obj):
        self.obj=obj
        return self.obj
    
    def setFaceIDs(self,faceIDs):
        self.faceIDs=faceIDs
        return self.faceIDs

    def set(self):
        faceVartexs=self.getPosVertexs_create_MPointArray(self.obj,self.faceIDs)
        return faceVartexs

    def export(self):
        faceVartexs=self.getPosVertexs_create_MPointArray(self.obj,self.faceIDs)
        replace_list=self.replaceMPointToList_create_dict(faceVartexs)
        return replace_list

    #Private
    def faceVertexPos_query_MPoint_list(self,obj,faceID):
        sel_MSelectionList = om2.MSelectionList()
        sel_MSelectionList.add(obj)
        sel_MDagPath = sel_MSelectionList.getDagPath(0)
        sel_MDagPath.extendToShape()
        shape_MItMeshPolygon = om2.MItMeshPolygon(sel_MDagPath)
        shape_MItMeshPolygon.setIndex(faceID)
        shape_MPoint_list=shape_MItMeshPolygon.getPoints()
        return shape_MPoint_list

    def getPosVertexs_create_MPointArray(self,obj,faceIDs=[]):
        test_list=[]
        for faceID in faceIDs:
            MPoint=self.faceVertexPos_query_MPoint_list(obj,faceID)
            test_list.append(MPoint)
        return test_list

    def replaceMPointToList_create_dict(self,vertexs_MPointArray):
        faceVartexs_dict={"faceVartexs":[]}
        for i in range(len(list(vertexs_MPointArray))):
            point00=list(vertexs_MPointArray[i][0])
            point01=list(vertexs_MPointArray[i][1])
            point02=list(vertexs_MPointArray[i][2])
            point03=list(vertexs_MPointArray[i][3])
            hoge_list=[point00,point01,point02,point03]
            faceVartexs_dict["faceVartexs"].append(hoge_list)
        return faceVartexs_dict
