#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pymel.core as pm

class PyNodes():
    def change_pyNode(self,obj_list):
        pyList = []
        for obj in obj_list:
            pyList.append(pm.PyNode(obj))
        return pyList