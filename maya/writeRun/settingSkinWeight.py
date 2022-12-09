# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from cgInTools.maya.library import objectLB as oLB
from cgInTools.maya.library import jsonLB as jLB
cit.reloads([oLB,jLB])

def classWeihgt_create_list():
    joint01=oLB.JointWeight("joint1")
    joint01.setSubject("test_geo1")
    joint01.setUseJoint(True)
    joint01.setValue(1)
    joint01.setVertexs(["test_geo1.vtx[0:261]"])
    
    joint02=oLB.JointWeight("joint2")
    joint02.setSubject("test_geo1")
    joint02.setUseJoint(True)
    joint02.setValue(1)
    joint02.setVertexs(["test_geo1.vtx[100:259]","test_geo1.vtx[261]"])
    
    joint03=oLB.JointWeight("joint2")
    joint03.setSubject("test_geo1")
    joint03.setUseJoint(True)
    joint03.setValue(0.8835)
    joint03.setVertexs(["test_geo1.vtx[80:99]"])
    
    joint04=oLB.JointWeight("joint2")
    joint04.setSubject("test_geo1")
    joint04.setUseJoint(True)
    joint04.setValue(0.4078)
    joint04.setVertexs(["test_geo1.vtx[60:79]"])
    
    joint05=oLB.JointWeight("joint3")
    joint05.setSubject("test_geo1")
    joint05.setUseJoint(True)
    joint05.setValue(1)
    joint05.setVertexs(["test_geo1.vtx[120:259]","test_geo1.vtx[261]"])

    joint06=oLB.JointWeight("joint3")
    joint06.setSubject("test_geo1")
    joint06.setUseJoint(True)
    joint06.setValue(0.5)
    joint06.setVertexs(["test_geo1.vtx[100:119]"])
    
    joint07=oLB.JointWeight("joint4")
    joint07.setSubject("test_geo1")
    joint07.setUseJoint(True)
    joint07.setValue(1)
    joint07.setVertexs(["test_geo1.vtx[160:259]","test_geo1.vtx[261]"])
    
    joint08=oLB.JointWeight("joint4")
    joint08.setSubject("test_geo1")
    joint08.setUseJoint(True)
    joint08.setValue(0.5)
    joint08.setVertexs(["test_geo1.vtx[140:159]"])
    
    joint09=oLB.JointWeight("joint5")
    joint09.setSubject("test_geo1")
    joint09.setUseJoint(True)
    joint09.setValue(1)
    joint09.setVertexs(["test_geo1.vtx[200:259]","test_geo1.vtx[261]"])
    
    joint10=oLB.JointWeight("joint5")
    joint10.setSubject("test_geo1")
    joint10.setUseJoint(True)
    joint10.setValue(0.5)
    joint10.setVertexs(["test_geo1.vtx[180:199]"])

    weights=[joint01,joint02,joint03,joint04,joint05,joint06,joint07,joint08,joint09,joint10]
    return weights

def dictWeihgt_create_list():
    geo_dict={
        "weights":[
            {
                "use":1,
                "object":"joint1",
                "subject":"test_geo",
                "value":1,
                "vertexs":["test_geo.vtx[0:261]"]
            },
            {
                "use":1,
                "object":"joint2",
                "subject":"test_geo",
                "value":1,
                "vertexs":["test_geo.vtx[100:259]","test_geo.vtx[261]"]
            },
            {
                "use":1,
                "object":"joint2",
                "subject":"test_geo",
                "value":0.8835,
                "vertexs":["test_geo.vtx[80:99]"]
            },
            {
                "use":1,
                "object":"joint2",
                "subject":"test_geo",
                "value":0.4078,
                "vertexs":["test_geo.vtx[60:79]"]
            },
            {
                "use":1,
                "object":"joint3",
                "subject":"test_geo",
                "value":0.5,
                "vertexs":["test_geo.vtx[100:119]"]
            },
            {
                "use":1,
                "object":"joint3",
                "subject":"test_geo",
                "value":1,
                "vertexs":["test_geo.vtx[120:259]","test_geo.vtx[261]"]
            },
            {
                "use":1,
                "object":"joint4",
                "subject":"test_geo",
                "value":1,
                "vertexs":["test_geo.vtx[160:259]","test_geo.vtx[261]"]
            },
            {
                "use":1,
                "object":"joint4",
                "subject":"test_geo",
                "value":0.5,
                "vertexs":["test_geo.vtx[140:159]"]
            },
            {
                "use":1,
                "object":"joint5",
                "subject":"test_geo",
                "value":1,
                "vertexs":["test_geo.vtx[200:259]","test_geo.vtx[261]"]
            },
            {
                "use":1,
                "object":"joint5",
                "subject":"test_geo",
                "value":0.5,
                "vertexs":["test_geo.vtx[180:199]"]
            }
        ]
    }
    return geo_dict

class EditedByJoint(jLB.Json):
    def __init__(self):
        super().__init__()
        self._weights=[]
    
    #Single Function
    def addWeights_create_JointWeights(self,joint,geo):
        getSkc=oLB.JointWeight(joint)
        getSkc.setSubject(geo)
        vertex_int=cmds.polyEvaluate(geo,v=1)

        valueVertex_lists=[]
        value_list=[]
        for num in range(vertex_int):
            vertex=geo+".vtx["+str(num)+"]"
            value=cmds.skinPercent(getSkc.getSkinClusters()[0],vertex,q=True,transform=getSkc.getObject())
            value_list.append(value)
            valueVertex_lists.append([value,vertex])  
        
        value_list=list(set(value_list))
        value_list.remove(1.0)
        value_list.remove(0.0)

        group_dict={}
        for value in value_list:
            group_dict[value]=[]

        for valueVertex_list in valueVertex_lists:
            if valueVertex_list[0] in value_list:
                group_dict[valueVertex_list[0]].append(valueVertex_list[1])

        for value,vertexs in group_dict.items():
            weight=oLB.JointWeight(joint)
            weight.setSubject(geo)
            weight.setUseJoint(True)
            weight.setValue(value)
            weight.setVertexs(vertexs)
            self._weights.append(weight)
        return self._weights

    def replaceDictWithWeights_query_JointWeights(self,read):
        for weight in read["weights"]:
            joint=oLB.JointWeight(weight["object"])
            joint.setSubject(weight["subject"])
            joint.setUseJoint(weight["use"])
            joint.setValue(weight["value"])
            joint.setVertexs(weight["vertexs"])
            self._weights.append(joint)
        return self._weights

    def replaceWeightsWithDict_create_dict(self,weights):
        weight_list=[]
        
        return write_dict

    def useSkinCluster_check_bool(self,weight):
        if not weight.getSkinClusters() is None:
            return True
        else:
            return False
    
    def weightRun_edit_func(self,weight):
        cmds.skinPercent(weight.getSkinClusters()[0],weight.getVertexs(),transformValue=[(weight.getObject(),weight.getValue())],nrm=True)
        #if not weight.getParent() == None:
            #cmds.setAttr(weight.getParent()+".liw",1)
    
    #Multi Function
    def _weightUnLock_edit_weights(self,weight):
        skinCluster_bool=self.useSkinCluster_check_bool(weight)
        if skinCluster_bool:
            cmds.setAttr(weight.getObject()+".liw",0)
        else:
            cmds.error(weight.getSubject()+" is not skin bind")

    #Public Function
    def setWeights(self,variable):
        self._weights=variable
        return self._weights
    def getWeights(self):
        return self._weights

    def run(self):
        for weight in  self._weights:
            self._weightUnLock_edit_weights(weight)
        for weight in  self._weights:
            if not weight.getUseJoint() == True:
                return 0
            else:
                self.weightRun_edit_func(weight)

    def importWeights(self):
        self._readDict=super().read()
        self._weights=self.replaceDictWithWeights_query_list(self._readDict)
        return self._weights

    def exportWeights(self):
        self._writeDict={"weights":self._weights}
        super().write()

def sample():
    geo_dict=dictWeihgt_create_list()
    test=EditedByJoint()
    test.replaceDictWithWeights_query_JointWeights(geo_dict)
    test.setWriteDict(geo_dict)
    #print(test.getWriteDict())
    #test.setPath()
    #test.setFile()
    #test.setExtension("jweight")
    test.run()
    #weights=test.addWeight_edit_JointWeights("joint2","test_geo")
    #for weight in weights:
        #print(weight.getValue())
        #print(weight.getVertexs())

sample()