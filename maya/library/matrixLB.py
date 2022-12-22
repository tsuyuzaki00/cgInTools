# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class AnimMatrix():
    def __init__(self):
        self._object=""
        self._matrix=[]
        self._time=0
        self._in="linear"
        self._out="linear"

    #Single Function
    def matrix_query_func(self,node):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MDagPath=node_MSelectionList.getDagPath()
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        normal_MMatrix=node_MDagPath.exclusiveMatrix()

        #print()

    #Multi Function
    def _multi_mode_func(self):
        self.single_mode_func()
        pass

    #Private Function
    def _private_mode_func(self):
        print(self._value)
        self._multi_mode_func()
        self.single_mode_func()
        pass

    #Public Function
    def public(self):
        print(self._value)
        pass
