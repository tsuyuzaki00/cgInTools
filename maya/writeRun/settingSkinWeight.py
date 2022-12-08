# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from cgInTools.maya.library import objectLB as oLB
from cgInTools.maya.library import jsonLB as jLB
cit.reloads([oLB,jLB])

def classWeihgt_create_list():
    joint01=oLB.JointWeight("joint1","test_geo1")
    joint01.setUseJoint(True)
    joint01.setVertexsValueDict({"vertexs":["test_geo1.vtx[0:261]"],"value":1})

    joint02=oLB.JointWeight("joint2","test_geo1")
    joint02.setUseJoint(True)
    joint02.setVertexsValueDict({"vertexs":["test_geo1.vtx[100:259]","test_geo1.vtx[261]"],"value":1})
    joint02.addVertexsValueDict({"vertexs":["test_geo1.vtx[80:99]"],"value":0.8835})
    joint02.addVertexsValueDict({"vertexs":["test_geo1.vtx[60:79]"],"value":0.4078})
    
    joint03=oLB.JointWeight("joint3","test_geo1")
    joint03.setUseJoint(True)
    joint03.setVertexsValueDict({"vertexs":["test_geo1.vtx[120:259]","test_geo1.vtx[261]"],"value":1})
    joint03.addVertexsValueDict({"vertexs":["test_geo1.vtx[100:119]"],"value":0.5})
    
    joint04=oLB.JointWeight("joint4","test_geo1")
    joint04.setUseJoint(True)
    joint04.setVertexsValueDict({"vertexs":["test_geo1.vtx[160:259]","test_geo1.vtx[261]"],"value":1})
    joint04.addVertexsValueDict({"vertexs":["test_geo1.vtx[140:159]"],"value":0.5})
    
    joint05=oLB.JointWeight("joint5","test_geo1")
    joint05.setUseJoint(True)
    joint05.setVertexsValueDict({"vertexs":["test_geo1.vtx[200:259]","test_geo1.vtx[261]"],"value":1})
    joint05.addVertexsValueDict({"vertexs":["test_geo1.vtx[180:199]"],"value":0.5})

    weights=[joint01,joint02,joint03,joint04,joint05]
    return weights

def dictWeihgt_create_list():
    geo_dict={
        "weights":[
            {
                "use":1,
                "object":"joint1",
                "subject":"test_geo",
                "vertexsValue_dicts":[
                    {"value":1,"vertexs":["test_geo.vtx[0:261]"]}
                ]
            },
            {
                "use":1,
                "object":"joint2",
                "subject":"test_geo",
                "vertexsValue_dicts":[
                    {"value":1,"vertexs":["test_geo.vtx[100:259]","test_geo.vtx[261]"]},
                    {"value":0.8835,"vertexs":["test_geo.vtx[80:99]"]},
                    {"value":0.4078,"vertexs":["test_geo.vtx[60:79]"]}
                ]
            },
            {
                "use":1,
                "object":"joint3",
                "subject":"test_geo",
                "vertexsValue_dicts":[
                    {"value":1,"vertexs":["test_geo.vtx[120:259]","test_geo.vtx[261]"]},
                    {"vertexs":["test_geo.vtx[100:119]"],"value":0.5}
                ]
            },
            {
                "use":0,
                "object":"joint4",
                "subject":"test_geo",
                "vertexsValue_dicts":[
                    {"value":1,"vertexs":["test_geo.vtx[160:259]","test_geo.vtx[261]"]},
                    {"value":0.5,"vertexs":["test_geo.vtx[140:159]"]}
                ]
            },
            {
                "use":1,
                "object":"joint5",
                "subject":"test_geo",
                "vertexsValue_dicts":[
                    {"value":1,"vertexs":["test_geo.vtx[200:259]","test_geo.vtx[261]"]},
                    {"value":0.5,"vertexs":["test_geo.vtx[180:199]"]}
                ]
            }
        ]
    }
    weights=[]
    for weight in geo_dict["weights"]:
        joint=oLB.JointWeight(weight["object"],weight["subject"])
        joint.setUseJoint(weight["use"])
        for vertexsValue_dict in weight["vertexsValue_dicts"]:
            joint.addVertexsValueDict(vertexsValue_dict)
        weights.append(joint)
    
    return weights


class EditedByJoint():
    def __init__(self):
        self._data=""
    
    #Single Function
    def weightUnLock_check_weights(weights):
        for weight in weights:
            if not weight.getSkinClusters() is None:
                cmds.setAttr(weight.getObject()+".liw",0)
            else:
                cmds.error(weight.getSubject()+" is not skin bind")
        return weights

    def writeDict_create_dict(weights):
        weight_list=[]
        for weight in weights:
            vertexsValue_list=[]
            for vertexsValueDict in weight.getVertexsValueDicts():
                vertexsValue_list.append({"value":vertexsValueDict["value"],"vertexs":vertexsValueDict["vertexs"]})
            weight_dict={
                    "use":weight.getUseJoint(),
                    "object":weight.getObject(),
                    "subject":weight.getSubject(),
                    "vertexsValue_dicts":vertexsValue_list
                }
            weight_list.append(weight_dict)
        write_dict={"weights":weight_list}
        return write_dict
    
    #Public Function
    def weightRun(weight):
        for vertexsValueDict in weight.getVertexsValueDicts():
            cmds.skinPercent(weight.getSkinClusters()[0],vertexsValueDict["vertexs"],transformValue=[(weight.getObject(),vertexsValueDict["value"])],nrm=True)
        if not weight.getParent() == None:
            cmds.setAttr(weight.getParent()+".liw",1)

    def main():
        weights=dictWeihgt_create_list()
        #weights=classWeihgt_create_list()
        exportDict(weights)
    
        weightUnLock_check_weights(weights)
        for weight in weights:
            if not weight.getUseJoint() == True:
                return 0
            else:
                weightRun(weight)

main()