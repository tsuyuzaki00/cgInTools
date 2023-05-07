# -*- coding: iso-8859-15 -*-

import cgInTools as cit
from cgInTools.library import jsonLB as jLB
from cgInTools.maya.library import objectLB as oLB
cit.reloads([oLB])

def selfWrite(node=None):
    if not node == None:
        node_SelfNode=oLB.SelfNode()
        node_SelfNode.setNode(node)
        node_SelfNode.setAttr("translateX")
        node_SelfNode.setDoIts(["queryAttr"])
        node_SelfNode.setSetChoices(["DoIts","Node","Attr"])
        write_dict=node_SelfNode.writeDict() 
        return write_dict
    else:
        return None
    
def selfReadAndDo(read_dict=None):
    if not read_dict == None:
        node_SelfNode=oLB.SelfNode()
        node_SelfNode.setReadDict(read_dict)
        node_SelfNode.doIt()

def main():
    selfWrite()
    node_Json=jLB.Json()
    node_Json.setDirectory()
    node_Json.setFile("test")
    node_Json.write()
    
    read_dict=node_Json.read()
    selfReadAndDo(read_dict)

main()