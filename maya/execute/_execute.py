#import maya.cmds as cmds
#import pymel.core as pm
''' Reload '''
#from cgInTools.ui import clickSelectUI as UI; reload(UI);
#from cgInTools.maya.library import click as lib; reload(lib);

''' Run '''
#from mgear_guide._tools.Maya.Manager import facialExportCurvesOP as ps
from cgInTools.maya.execute import ctrlOffsetConnect as ps
from cgInTools.maya.library import cConstraint as cct
reload(ps); ps.main()
