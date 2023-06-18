# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class SuperClass(object):
    def __init__(self):
        self._superValue=""
        self._settings=[]

    def inheritance_mode_func(self):
        pass

class Template(SuperClass):
    def __init__(self):
        super(Template,self).__init__()
        self._value=""

    #Single Function
    def single_mode_func(self):
        pass

    #Multi Function
    def _multi_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        pass

    #Inheritance Function
    def _inheritance_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        pass

    #Private Function
    def __private_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        self._inheritance_mode_func()
        self._superValue
        pass

    #Setting Function
    def setSetting(self,variable):
        self._settings=variable
    def addSetting(self,variable):
        self._settings.append(variable)
    def currentSetting(self):
        self._settings=self.single_mode_func()
        return self._settings
    def getSetting(self):
        return self._settings

    #Public Function
    def public(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        self._inheritance_mode_func()
        self.__private_mode_func()
        self._value
        self._superValue
        pass
