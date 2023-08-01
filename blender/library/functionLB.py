import os
import bpy

def getStartDirectory():
    thisPath_str=bpy.data.filepath
    thisPath_list=thisPath_str.split("\\")
    thisPath_list.pop(-1)
    thisPath_list.pop(-1)
    startDirectory="\\".join(thisPath_list)
    return startDirectory

def savePath(directory,fileName):
    savePath=os.path.join(directory,fileName)
    bpy.ops.wm.save_as_mainfile(filepath=savePath)

def rename(beforeName,afterName):
    for obj in bpy.data.objects:
        if target_string in obj.name:
            obj.name = obj.name.replace(target_string, new_name)