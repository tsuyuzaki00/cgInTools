# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class SplitGrouping():
    def __init__(self):
        pass

    #{'other': [u'nurbsCircle1'], 'geo': [u'C_model_geo_scene_01']}
    def create_group(self,group_dict):
        for key,value in group_dict.items():
            group = cmds.createNode("transform",n=key+"_grp")
            cmds.parent(value,group)

    # {"mesh":[],"joint":[]...}
    def node_grping(self,objs):
        group = {}
        type_list = []
        for obj in objs:
            type = cmds.nodeType(obj)
            type_list.append(type)
        for type in set(type_list):
            if type == cmds.nodeType(obj):
                pass
        return

    def set_name_grping(self,name,objs):
        name_list = []
        other_list = []
        group = {name:name_list,"other":other_list}
        for obj in objs:
            if name in obj:
                name_list.append(obj)
            else:
                other_list.append(obj)
        return group

    def split_name_grping(self,obj):
        pass

    def pos_grping(self,obj):
        pass

def main():
    objs = cmds.ls(sl=True)
    _splitGrouping = SplitGrouping()
    test = _splitGrouping.node_grping(objs)
    #group_dict = _splitGrouping.set_name_grping("geo",objs)
    #test = _splitGrouping.create_group(group_dict)
    print(test)