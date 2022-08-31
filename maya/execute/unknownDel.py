# -*- coding: iso-8859-15 -*-
from maya import cmds

def delUnknownNode_edit_func():
    unknown_nodes = cmds.ls(type = 'unknown')
    cmds.delete(unknown_nodes)
    unknown_plugins = cmds.unknownPlugin(q=True, l=True)
    if unknown_plugins:
        for p in unknown_plugins:
            cmds.unknownPlugin(p, r=True)
            print('Removed unknown plugin : {}'.format(p))

def main():
    delUnknownNode_edit_func()