# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
cit.reloads([sbLB])

class Template():
    def __init__(self):
        self._value=""

    def __loading(self):
        self._value=""

#Public Function
    def public(self):
        print(self._value)
        pass

#Private Function
    def _private_mode_func(self):
        print(self._value)
        self.mulch_mode_func()
        self.single_mode_func()
        pass

#Mulch Function
    def mulch_mode_func(self):
        self.single_mode_func()
        pass

#Single Function
    def single_mode_func(self):
        pass