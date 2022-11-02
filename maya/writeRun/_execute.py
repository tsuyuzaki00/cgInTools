#import maya.cmds as cmds
#import pymel.core as pm

"""Reload"""
### Python 2
#from cgInTools.ui import clickSelectUI as UI; reload(UI);
#from cgInTools.maya.library import click as lib; reload(lib);
### Python 3
#import importlib
#from cgInTools.ui import clickSelectUI as UI; importlib.reload(UI);
#from cgInTools.maya.library import click as lib; importlib.reload(lib);

"""Run"""
#from cgInTools.maya.library import cConstraint as ps
#from cgInTools.maya.execute import ctrlOffsetConnect as ps
from cgInTools.maya.manager import ctrlColorChange as ps
ps.main()
