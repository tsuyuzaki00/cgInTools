# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import cJson as cj
from cgInTools.maya.library import cFiling as cf
from cgInTools.maya.library import setBaseLB as sb
cit.verReload(cf)

class Test(sb.SetBase):
    def __init__(self):
        