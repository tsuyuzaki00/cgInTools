# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from cgInTools.maya.library import objectLB as oLB
cit.reloads([oLB])

def weight_create_list():
    joint01=oLB.JointWeight("joint1")
    joint01.setVertexsValueDict({"vertexs":["test_geo.vtx[0:261]"],"value":1})
    joint01.setUseJoint(True)

    joint02=oLB.JointWeight("joint2")
    joint02.setVertexsValueDict({"vertexs":["test_geo.vtx[100:259]","test_geo.vtx[261]"],"value":1})
    joint02.addVertexsValueDict({"vertexs":["test_geo.vtx[80:99]"],"value":0.8835})
    joint02.addVertexsValueDict({"vertexs":["test_geo.vtx[60:79]"],"value":0.4078})
    joint02.setUseJoint(True)
    
    joint03=oLB.JointWeight("joint3")
    joint03.setVertexsValueDict({"vertexs":["test_geo.vtx[120:259]","test_geo.vtx[261]"],"value":1})
    joint03.addVertexsValueDict({"vertexs":["test_geo.vtx[100:119]"],"value":0.5})
    joint03.setUseJoint(True)
    
    joint04=oLB.JointWeight("joint4")
    joint04.setVertexsValueDict({"vertexs":["test_geo.vtx[160:259]","test_geo.vtx[261]"],"value":1})
    joint04.addVertexsValueDict({"vertexs":["test_geo.vtx[140:159]"],"value":0.5})
    joint04.setUseJoint(True)
    
    joint05=oLB.JointWeight("joint5")
    joint05.setVertexsValueDict({"vertexs":["test_geo.vtx[200:259]","test_geo.vtx[261]"],"value":1})
    joint05.addVertexsValueDict({"vertexs":["test_geo.vtx[180:199]"],"value":0.5})
    joint05.setUseJoint(True)

    weights=[joint01,joint02,joint03,joint04,joint05]
    for weight in weights:
        if not weight.getSkinClusters() is None:
            cmds.setAttr(weight.getObject()+".liw",0)
        else:
            cmds.error(weight.getObject()+" is not skin bind")

    useWeights=[]
    for weight in weights:
        if weight.getUseJoint():
            useWeights.append(weight)
        else:
            return useWeights
    return useWeights

def weightRun(weight):
    for vertexsValueDict in weight.getVertexsValueDicts():
        cmds.skinPercent(weight.getSkinClusters()[0],vertexsValueDict["vertexs"],transformValue=[(weight.getObject(),vertexsValueDict["value"])],nrm=True)
    if not weight.getParent() == None:
        cmds.setAttr(weight.getParent()+".liw",1)

def main():
    weights=weight_create_list()
    for weight in weights:
        weightRun(weight)

main()