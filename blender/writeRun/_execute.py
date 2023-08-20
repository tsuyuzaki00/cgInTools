import bpy

def selectPoseBone_query_PoseBone(armature_str,bone_str):
    armature_Object=bpy.data.objects[armature_str]
    bpy.context.view_layer.objects.active=armature_Object
    bpy.ops.object.mode_set(mode='POSE')
    bone_PoseBone=armature_Object.pose.bones[bone_str]
    return bone_PoseBone

bone_strs=[
    'cnt_axs_hood005_02_R',
    'cnt_axs_hood006_02_R',
    'cnt_axs_hood007_02_R',
    'cnt_axs_hood008_02_R',
    'cnt_axs_hood009_02_R',
    'cnt_axs_hood010_02_R',
    'cnt_axs_hood011_02_R',
    'cnt_axs_hood012_02_R',
    'cnt_axs_hood013_02_R',
    'cnt_axs_hood014_02_R',
    'cnt_axs_hood015_02_R'
]

for bone_str in bone_strs:
    bone_PoseBone=selectPoseBone_query_PoseBone("zolaS_rig_armature",bone_str)
    bone_PoseBone.constraints["Copy Scale"].target=bpy.data.objects["zolaS_rig_armature"]
    bone_PoseBone.constraints["Copy Scale"].subtarget="cnt_all_hood"
    bone_PoseBone.constraints["Copy Scale"].use_offset=True
    bone_PoseBone.constraints["Copy Scale"].owner_space='CUSTOM'
    bone_PoseBone.constraints["Copy Scale"].space_object=bpy.data.objects["zolaS_rig_armature"]
    bone_PoseBone.constraints["Copy Scale"].space_subtarget="cnt_all_hood"
