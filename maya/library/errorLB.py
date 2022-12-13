# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
cit.reloads([jLB])

class Error(sbLB.BaseFile):
    def __init__(self):
        super().__init__()
        json_dict=jLB.getJson(self._path,self._file)

    def __loading(self):
        self._value=""

    #Single Function
    def menuError_check_func(self):
        menu_dict=jLB.getJson(cit.menu_path,"mayaMenu")
        pass

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
