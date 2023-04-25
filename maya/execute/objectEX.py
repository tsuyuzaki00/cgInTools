# -*- coding: iso-8859-15 -*-

import cgInTools as cit
from cgInTools.library import jsonLB as jLB
from cgInTools.maya.library import objectLB as oLB
cit.reloads([oLB])

data_dict={
    "selfNode_dicts":[
        {
            "node":"pCube1",
            "setting_dicts":[
                {
                    "function":"attr",
                    "value":"translateX"
                },
                {
                    "function":"value",
                    "value":"1"
                },
            ],
            "doIts":[
                "editAttr",
            ]
        },
        {
            "node":"pCube1",
            "setting_dicts":[
                {
                    "function":"Attr",
                    "value":"translateY"
                },
                {
                    "function":"Value",
                    "value":"5"
                },
            ],
            "doIts":[
                "editAttr",
            ]
        },
    ],
    
}

def selfNode(self_dicts=[]):
    if not self_dicts == []:
        for self_dict in self_dicts:
            node_SelfNode=oLB.SelfNode(self_dict["node"])
            for setting_dict in self_dict["setting_dicts"]:
                node_SelfNode.setting(setting_dict["function"],setting_dict["value"])
            for doIt_str in self_dict["doIts"]:
                node_SelfNode.doIt(doIt_str)
    else:
        return None



def main():
    selfNode(data_dict["selfNode_dicts"])
    pass

main()