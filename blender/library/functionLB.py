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

def addIntCustomPropertiesToPoseBone(armatureName_str,boneName_str,propertyName_str,defValue_int,minValue_int,maxValue_int):
    armature_Object=bpy.data.objects[armatureName_str]
    bpy.context.view_layer.objects.active=armature_Object
    bpy.ops.object.mode_set(mode='POSE')
    bone_PoseBone=armature_Object.pose.bones[boneName_str]
    
    if propertyName_str not in bone_PoseBone:
        bone_PoseBone[propertyName_str]=int(defValue_int)
        bone_PoseBone.id_properties_ui("IKFK").update(min=minValue_int,max=maxValue_int)

def addDriverBetweenPoseBones(armatureName_str,boneName_str,constraintName_str,propertyName_str,sourceArmature_str,sourceBone_str,sourceProperty_str):
    armature_Object=bpy.data.objects[armatureName_str]
    bpy.context.view_layer.objects.active=armature_Object
    bpy.ops.object.mode_set(mode='POSE')
    bone_PoseBone=armature_Object.pose.bones[boneName_str]
    value_FCurve=bone_PoseBone.constraints[constraintName_str].driver_add(propertyName_str)
    value_FCurve.driver.type='SCRIPTED'
    
    value_DriverVariable=value_FCurve.driver.variables.new()
    value_FCurve.driver.expression='var'
    value_DriverVariable.name='var'
    value_DriverVariable.type='SINGLE_PROP'
    value_DriverVariable.targets[0].id=bpy.data.objects[sourceArmature_str]
    value_DriverVariable.targets[0].data_path='pose.bones["'+sourceBone_str+'"]["'+sourceProperty_str+'"]'

def rename(beforeName,afterName):
    for obj in bpy.data.objects:
        if target_string in obj.name:
            obj.name = obj.name.replace(target_string, new_name)