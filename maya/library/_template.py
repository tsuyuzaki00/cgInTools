# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class Template():
    def __init__(self):
        self._value=""

    def __loading(self):
        self._value=""

    #Single Function
    def single_mode_func(self):
        pass

    #Multi Function
    def _multi_mode_func(self):
        self.single_mode_func()
        pass

    #Private Function
    def __private_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.external_func()
        self._value
        pass

    #Summary Function
    def __summary(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.__private_mode_func()
        self._value
        pass

    #Public Function
    def public(self):
        print(self._value)
        pass
