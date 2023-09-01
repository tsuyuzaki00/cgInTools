# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

class SelfMeshVertex(object):
    def __init__(self):
        self.point_Point=None
        pass

class SelfMeshEdge(object):
    def __init__(self):
        self.vertex_SelfMeshVertexs=[]
        pass

class SelfMeshFace(object):
    def __init__(self):
        self.vertex_SelfMeshVertexs=[]
        self.edge_SelfMeshEdges=[]
        pass


class SelfMeshPolygon(object):
    def __init__(self):
        self._name_str=None
        self._polygons=None#[[Point,Point,Point,Point],[Point,Point,Point,Point]]

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

    def polygonCount_query_ints(self,polygons):
        polygonCounts=[len(polygon) for polygon in polygons]
        return polygonCounts
    
    def pointID_query_ints(self,polygons):
        """
        pointIDs=[]
        for polygon in polygons:
            for point in polygon:
                id_int=point.getID()
                pointIDs.append(id_int)
        """
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
    def create(self):
        trans_fn=om2.MFnTransform()
        trans_obj=trans_fn.create()
        _name_str=trans_fn.setName(self._name_str)
        fn_mesh=om2.MFnMesh()

        vertices=self.allVertex_query_Points(self._polygons)
        polygonCounts=self.polygonCount_query_ints(self._polygons)
        polygonConnects=self.pointID_query_ints(self._polygons)

        fn_mesh.create(vertices,polygonCounts,polygonConnects,parent=trans_obj)
        fn_mesh.setName(_name_str+'Shape')
