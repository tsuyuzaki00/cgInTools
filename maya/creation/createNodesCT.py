import cgInTools as cit
from ...library import jsonLB as jLB
from ..library import selfLB as sLB
from ..library import dataLB as dLB
cit.reloads([jLB,sLB,dLB])

def main(readFile_str="init",writeFile_str="init",name_str="createNodes"):
    read_DataPath=dLB.DataPath()
    read_DataPath.setAbsoluteDirectory(cit.mayaSettings_dir)
    read_DataPath.setRelativeDirectory(name_str)
    read_DataPath.setFile(readFile_str)
    read_DataPath.setExtension("json")

    write_DataPath=dLB.DataPath()
    write_DataPath.setAbsoluteDirectory(cit.mayaSettings_dir)
    write_DataPath.setRelativeDirectory(name_str)
    write_DataPath.setFile(writeFile_str)
    write_DataPath.setExtension(name_str)

    menu_AppJson=jLB.AppJson()
    menu_AppJson.setDataPath(read_DataPath)
    menu_dict=menu_AppJson.read()

    createNode_SelfObjectArray=sLB.SelfObjectArray()
    createNode_SelfObjectArray.setOriginDataPath(write_DataPath)

    for createNode_dict in menu_dict.get("createNodes"):
        createNode_DataNode=dLB.DataNode()
        createNode_DataNode.setName(createNode_dict.get("Name"))
        createNode_DataNode.setType(createNode_dict.get("Type"))

        createNode_SelfDGNode=sLB.SelfDGNode()
        createNode_SelfDGNode.setOriginDataPath(write_DataPath)
        createNode_SelfDGNode.setDataNode(createNode_DataNode)
        createNode_SelfDGNode.setDoItStrs(["createNodeNormal"])
        
        createNode_SelfObjectArray.addObjects([createNode_SelfDGNode])
    
    createNode_SelfObjectArray.writeData()