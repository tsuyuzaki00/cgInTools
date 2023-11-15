# -*- coding: iso-8859-15 -*-

class SuperClass(object):
    def __init__(self):
        self._superValue=""
        self._settings=[]

    def inheritance_mode_func(self):
        pass

class Template(SuperClass):
    def __init__(self):
        super(Template,self).__init__()
        self._name_value=None
        self._settings=[]

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
    
    #Test Function
    def _test(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        self._inheritance_mode_func()
        self.__private_mode_func()
        self._value
        self._superValue

    #Setting Function
    def setValue(self,variable):
        self._name_value=variable
        return self._name_value
    def getValue(self):
        return self._name_value

    def setSettings(self,variables):
        self._settings=variables
        return self._settings
    def addSettings(self,variables):
        self._settings+=variables
        return self._settings
    def currentSettings(self):
        self._settings=self.single_mode_func()
        return self._settings
    def getSettings(self):
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
