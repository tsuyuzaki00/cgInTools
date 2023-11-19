# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from ...library import pathLB as pLB
from ...library import serializeLB as sLB
from ...library import _testLB as tLB
from ..library import dataLB as dLB
from ..library import nodeAttrLB as naLB
from ..library import matrixLB as mLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,sLB,tLB,dLB,naLB,mLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    
    node_DataNode=dLB.DataNode()
    node_DataNode.setName("pCube1")
    node_DataNode.setType("transform")

    translateX_DataAttribute=dLB.DataAttributeFloat()
    translateX_DataAttribute.setName("translateX")
    translateX_DataAttribute.setValue(10)

    bool_DataAttribute=dLB.DataAttributeBoolean()
    bool_DataAttribute.setName("booleanSan")
    bool_DataAttribute.setShortName("bsan")
    bool_DataAttribute.setValue(False)
    int_DataAttribute=dLB.DataAttributeInt()
    int_DataAttribute.setName("intSan")
    int_DataAttribute.setShortName("isan")
    int_DataAttribute.setValue(0)
    #int_DataAttribute.setMax(20)
    #int_DataAttribute.setMin(0)
    float_DataAttribute=dLB.DataAttributeFloat()
    float_DataAttribute.setName("floatSan")
    float_DataAttribute.setShortName("fsan")
    float_DataAttribute.setValue(5.64)
    #float_DataAttribute.setMax(20.0)
    #float_DataAttribute.setMin(0.0)
    str_DataAttribute=dLB.DataAttributeString()
    str_DataAttribute.setName("stringSan")
    str_DataAttribute.setShortName("ssan")
    str_DataAttribute.setValue("hoge")
    vector_DataAttribute=dLB.DataAttributeVector()
    vector_DataAttribute.setName("vectorSan")
    vector_DataAttribute.setShortName("vsan")
    vector_DataAttribute.setValue([0.0,0.0,0.0])
    
    plug_DataPlugs=[]
    for attr_DataAttribute in [int_DataAttribute,float_DataAttribute,bool_DataAttribute,str_DataAttribute,translateX_DataAttribute]:
        plug_DataPlug=dLB.DataPlug()
        plug_DataPlug.setDataNode(node_DataNode)
        plug_DataPlug.setDataAttribute(attr_DataAttribute)
        plug_DataPlugs.append(plug_DataPlug)
    
    node_SelfDGNode=naLB.SelfDGNode()
    node_SelfDGNode.setDataPlugs(plug_DataPlugs)
    node_SelfDGNode.editAttr()
    

main()