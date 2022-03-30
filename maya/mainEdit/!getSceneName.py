import maya.cmds as cmds

fileName = cmds.file(q = True, sceneName = True)

pathList = fileName.split('/')
scenePart = pathList[-1].split('_')

scenePart[0]