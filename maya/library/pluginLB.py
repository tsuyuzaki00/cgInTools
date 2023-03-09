# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def loadedOnOff_edit_func(pluginName=None):
    if pluginName == None:
        return
    if cmds.pluginInfo(pluginName,q=True,l=True):
        cmds.unloadPlugin(pluginName)
        print(pluginName+" OFF"),
    elif not cmds.pluginInfo(pluginName,q=True,l=True):
        cmds.loadPlugin(pluginName)
        print(pluginName+" ON")