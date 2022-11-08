# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

# 複数選択をしていてもジョイントを作成出来る用にしている
def jointOnly(**kwargs):
    cmds.select(cl=True)
    joint=cmds.joint(**kwargs)
    return joint