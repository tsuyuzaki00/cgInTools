''' Reload '''
#from cgInTools.ui import clickSelectUI as UI; reload(UI);
#from cgInTools.maya.library import click as lib; reload(lib);

''' Run '''
#from mgear_guide._tools.Maya.Manager import facialExportCurvesOP as ps
from cgInTools.maya.manager import clickSelect as ps
reload(ps); ps.main()

#import pymel.core as pm
#import maya.cmds as cmd