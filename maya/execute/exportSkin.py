# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2

import time

def geoSkinCluster_query_node(obj):
        shape = cmds.listRelatives(obj,c=True,f=True)
        histories = cmds.listHistory(shape[0], pruneDagObjects=True, interestLevel=2)
        try:
            skinCluster_node = cmds.ls(histories, type="skinCluster")[0]
        except IndexError:
            return None
        else:
            return skinCluster_node

selList_MSelectionList=om2.MGlobal.getActiveSelectionList()

_time = time.clock
startTime = _time()

for i in range(selList_MSelectionList.length()):
    
    mesh_MDagPath=selList_MSelectionList.getDagPath(i)
    mesh_MDagPath.extendToShape()

    """
    mesh_MFnDependencyNode=om2.MFnDependencyNode(mesh_MDagPath.node())
    inMesh_MPlug=mesh_MFnDependencyNode.findPlug("inMesh",False)
    inMesh_MObject=inMesh_MPlug.asMObject()
    inMesh_MFnDependencyNode=om2.MFnDependencyNode(inMesh_MObject)
    #print(inMesh_MFnDependencyNode.name())
    """

    skc=geoSkinCluster_query_node(selList_MSelectionList.getDagPath(i))
    skc_MSelectionList=om2.MGlobal.getSelectionListByName(skc)
    skc_MObject=skc_MSelectionList.getDependNode(0)
    skinFn_MFnSkinCluster = oma2.MFnSkinCluster(skc_MObject)

    meshVerItFn_MItMeshVertex=om2.MItMeshVertex(mesh_MDagPath)
    indices_list=range(meshVerItFn_MItMeshVertex.count())

    singleIdComp_MFnSingleIndexedComponent=om2.MFnSingleIndexedComponent()
    vertexComp_MObject=singleIdComp_MFnSingleIndexedComponent.create(om2.MFn.kMeshVertComponent)
    singleIdComp_MFnSingleIndexedComponent.addElements(indices_list)

    infDags = skinFn_MFnSkinCluster.influenceObjects()
    infIndexes = om2.MIntArray(len(infDags),0)
    for x in xrange(len(infDags)):
        infIndexes[x]=int(skinFn_MFnSkinCluster.indexForInfluenceObject(infDags[x]))

    s = _time()
    weightData = skinFn_MFnSkinCluster.getWeights(mesh_MDagPath,vertexComp_MObject)
    #print(weightData)
    get = _time() - s
    print("getWeights()",get,"s")
    #skinFn_MFnSkinCluster.setWeights(mesh_MDagPath,vertexComp_MObject,infIndexes,weightData[0])