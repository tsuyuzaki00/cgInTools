import bpy
import math
import bmesh

class SelfOrigin(object):
    def __init__(self):
        self._read_dict={}
        self._setChoices=["DoIts"]
        self._doIts=[]
    
    #Setting Function
    def setReadDict(self,variable):
        self._read_dict=variable
    def getReadDict(self):
        return self._read_dict
    
    def setSetChoices(self,variables):
        self._setChoices=variables
    def getSetChoices(self):
        return self._setChoices
    
    def setDoIts(self,variables):
        self._doIts=variables
    def getDoIts(self):
        return self._doIts
    
    #Public Function
    def writeDict(self,setChoices=None):
        _setChoices=setChoices or self._setChoices

        write_dict={}
        for _selfChoice in _setChoices:
            #print(_selfChoice)
            variable=eval('self.get'+_selfChoice+'()')
            write_dict[_selfChoice]=variable
        return write_dict

    def readDict(self,read_dict=None):
        _read_dict=read_dict or self._read_dict

        setFunctions=list(_read_dict.keys())
        for setFunction in setFunctions:
            #print(_read_dict[setFunction])
            if isinstance(_read_dict[setFunction],str):
                variable='"'+_read_dict[setFunction]+'"'
            else:
                variable=str(_read_dict[setFunction])
            eval('self.set'+setFunction+'('+variable+')')

    def doIt(self,doIts=None):
        _doIts=doIts or self._doIts

        if _doIts == None:
            return
        else:
            for _doIt in _doIts:
                eval("self."+_doIt+"()")

class SelfModifiersMesh(SelfOrigin):
    def __init__(self):
        super(SelfModifiersMesh,self).__init__()
        self._mesh_str=None
        self._subject_str=None
        self._modifier_str=None
        self._modifierType_str=None
        self._setChoices+=[
        ]
        self._doIts+=[
        ]

    #Single Function
    def selectModifiersMesh_query_ObjectModifiers(self,meshName):
        mesh_Object=bpy.data.objects[meshName]
        bpy.context.view_layer.objects.active=mesh_Object
        bpy.ops.object.mode_set(mode='OBJECT')
        mesh_ObjectModifiers=mesh_Object.modifiers
        return mesh_ObjectModifiers

    def modifierTypeDefName_create_str(self,modifier_str):
        if not modifier_str == None:
            modifierSplit_strs=modifier_str.split("_")
            modifierCapitalizes=[modifierSplit_str.capitalize() for modifierSplit_str in modifierSplit_strs]
            modifier_str="".join(modifierCapitalizes)
        return modifier_str

    def modifierApply_edit_func(self,mesh_ObjectModifiers,modifier_str):
        mod=mesh_ObjectModifiers[modifier_str]
        bpy.ops.object.modifier_apply(modifier=mod.name,single_user=True)

    def bakeDataTransfar_edit_func(self,bake_DataTransfarModifier,cage):
        bake_DataTransfarModifier.object=bpy.data.objects[cage]
        bake_DataTransfarModifier.use_vert_data=True
        bake_DataTransfarModifier.data_types_verts={'VGROUP_WEIGHTS'}
        bake_DataTransfarModifier.vert_mapping='POLYINTERP_NEAREST'
        if bake_DataTransfarModifier.name == "DataTransfar_body":
            bake_DataTransfarModifier.vertex_group="mod_fingerAll"
            bake_DataTransfarModifier.invert_vertex_group=True

    def isModifier_query_bool(self,mesh_ObjectModifiers,modifier_str):
        try:
            mesh_ObjectModifiers[modifier_str]
            return True
        except KeyError:
            return False

    #Multi Function
    def _modifierAdd_create_Modifier(self,mesh_ObjectModifiers,modifierType,name):
        modifierDefName_str=self.modifierTypeDefName_create_str(modifierType)
        modifier=name or modifierDefName_str
        mesh_ObjectModifiers.new(name=modifier,type=modifierType)
        return mesh_ObjectModifiers[modifier]

    #Setting Function
    def setMesh(self,variable):
        setattr(self,"_mesh_str",variable)
    def getMesh(self):
        return self._mesh_str
    
    def setSubject(self,variable):
        setattr(self,"_subject_str",variable)
    def getSubject(self):
        return self._subject_str
    
    def setModifier(self,variable):
        setattr(self,"_modifier_str",variable)
    def getModifier(self):
        return self._modifier_str
    
    def setModifierType(self,variable):
        setattr(self,"_modifierType_str",variable)
    def getModifierType(self):
        return self._modifierType_str

    #Public Function
    def modifierApply(self,meshName=None,modifierName=None):
        _mesh_str=meshName or self._mesh_str
        _modifier_str=modifierName or self._modifier_str

        mesh_ObjectModifiers=self.selectModifiersMesh_query_ObjectModifiers(_mesh_str)
        self.modifierApply_edit_func(mesh_ObjectModifiers,_modifier_str)

    def addModifier(self,meshName=None,modifierName=None,modifierType=None):
        _mesh_str=meshName or self._mesh_str
        _modifier_str=modifierName or self._modifier_str
        _modifierType_str=modifierType or self._modifierType_str

        mesh_ObjectModifiers=self.selectModifiersMesh_query_ObjectModifiers(_mesh_str)
        mesh_Modifier=self._modifierAdd_create_Modifier(mesh_ObjectModifiers,_modifierType_str,_modifier_str)
        return mesh_Modifier.name

    def editBakeDataTransfer(self,meshName=None,modifierName=None,cage=None):
        _mesh_str=meshName or self._mesh_str
        _modifier_str=modifierName or self._modifier_str
        _subject_str=cage or self._subject_str

        mesh_ObjectModifiers=self.selectModifiersMesh_query_ObjectModifiers(_mesh_str)
        bake_DataTransfarModifier=mesh_ObjectModifiers[_modifier_str]
        self.bakeDataTransfar_edit_func(bake_DataTransfarModifier,_subject_str)

    def editArmature(self,armatureName=None,meshName=None,modifierName=None):
        _mesh_str=meshName or self._mesh_str
        _modifier_str=modifierName or self._modifier_str
        _armature_str=armatureName or self._subject_str

        mesh_ObjectModifiers=self.selectModifiersMesh_query_ObjectModifiers(_mesh_str)
        if self.isModifier_query_bool(mesh_ObjectModifiers,_modifier_str):
            mesh_ArmatureModifier=mesh_ObjectModifiers[_modifier_str]
        else:
            mesh_ArmatureModifier=self._modifierAdd_create_Modifier(mesh_ObjectModifiers,"ARMATURE",_modifier_str)
        mesh_ArmatureModifier.object=bpy.data.objects[_armature_str]

    def isModifier(self,meshName=None,modifierName=None):
        _mesh_str=meshName or self._mesh_str
        _modifier_str=modifierName or self._modifier_str

        mesh_ObjectModifiers=self.selectModifiersMesh_query_ObjectModifiers(_mesh_str)
        isModifier_bool=self.isModifier_query_bool(mesh_ObjectModifiers,_modifier_str)
        return isModifier_bool

class SelfEditArmature(SelfOrigin):
    def __init__(self):
        super(SelfEditArmature,self).__init__()
        self._armature_str=None
        self._bone_str=None
        self._head_list=None
        self._tail_list=None
        self._roll_float=None
        self._setChoices+=[
            "Armature",
            "Bone",
            "Head",
            "Tail",
            "Roll"
        ]
        self._doIts+=[
            "editHead",
            "editTail",
            "editRoll"
        ]

    def selectEditBone_query_EditBone(self,armatureName,boneName):
        armature_Object=bpy.data.objects[armatureName]
        bpy.context.view_layer.objects.active=armature_Object
        bpy.ops.object.mode_set(mode='EDIT')
        bone_EditBone=armature_Object.data.edit_bones[boneName]
        return bone_EditBone

    def headPos_edit_func(self,bone_EditBone,vector):
        for i in range(3):
            bone_EditBone.head[i]=vector[i]

    def headPos_query_list(self,bone_EditBone):
        head_list=[bone_EditBone.head[i] for i in range(3)]
        return head_list
    
    def tailPos_edit_func(self,bone_EditBone,vector):
        for i in range(3):
            bone_EditBone.tail[i]=vector[i]
    
    def tailPos_query_list(self,bone_EditBone):
        tail_list=[bone_EditBone.tail[i] for i in range(3)]
        return tail_list
    
    def roll_edit_func(self,bone_EditBone,value):
        bone_EditBone.roll=value

    def roll_query_float(self,bone_EditBone):
        roll_float=bone_EditBone.roll
        return roll_float

    #Setting Function
    def setArmature(self,variable):
        self._armature_str=variable
        return self._armature_str
    def getArmature(self):
        return self._armature_str
    
    def setBone(self,variable):
        self._bone_str=variable
        return self._bone_str
    def getBone(self):
        return self._bone_str
    
    def setHead(self,variable):
        self._head_list=variable
        return self._head_list
    def currentHead(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._head_list=self.headPos_query_list(bone_EditBone)
        return self._head_list
    def getHead(self):
        return self._head_list
    
    def setTail(self,variable):
        self._tail_list=variable
        return self._tail_list
    def currentTail(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._tail_list=self.tailPos_query_list(bone_EditBone)
        return self._tail_list
    def getTail(self):
        return self._tail_list
    
    def setRoll(self,variable):
        self._roll_float=variable
        return self._roll_float
    def currentRoll(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._roll_float=self.roll_query_float(bone_EditBone)
        return self._roll_float
    def getRoll(self):
        return self._roll_float

    #Public Function
    def editHead(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _head_list=vector or self._head_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.headPos_edit_func(bone_EditBone,_head_list)
    
    def editTail(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _tail_list=vector or self._tail_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.tailPos_edit_func(bone_EditBone,_tail_list)

    def editRoll(self,value=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _roll_float=value or self._roll_float
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.roll_edit_func(bone_EditBone,_roll_float)

class SelfPoseArmature(SelfOrigin):
    def __init__(self):
        super(SelfPoseArmature,self).__init__()
        self._armature_str=None
        self._bone_str=None
        self._property_str=None
        self._translation_list=None
        self._rotation_list=None
        self._rotationMode_str=None
        self._scale_list=None
        self._translationShape_list=None
        self._scaleShape_list=None
        self._ikfkShape_list=None
        self._curveIn_list=None
        self._curveOut_list=None
        self._customObject_str=None
        self._setChoices+=[
        ]
        self._doIts+=[
        ]

    #Single Function
    def selectPoseBone_query_PoseBone(self,armatureName,boneName):
        armature_Object=bpy.data.objects[armatureName]
        bpy.context.view_layer.objects.active=armature_Object
        bpy.ops.object.mode_set(mode='POSE')

        bone_PoseBone=armature_Object.pose.bones[boneName]
        return bone_PoseBone

    def translation_edit_func(self,bone_PoseBone,translation):
        bone_PoseBone.location=translation
    
    def translation_query_list(self,bone_PoseBone):
        translation_vector=bone_PoseBone.location
        translation_list=[translation_vector[0],translation_vector[1],translation_vector[2]]
        return translation_list
    
    def rotation_edit_func(self,bone_PoseBone,rotation,mode):
        bone_PoseBone.rotation_euler=rotation
        bone_PoseBone.rotation_mode=mode
    
    def rotation_query_list(self,bone_PoseBone):
        rotation_vector=bone_PoseBone.rotation_euler
        rotation_list=[rotation_vector[0],rotation_vector[1],rotation_vector[2]]
        return rotation_list

    def rotationMode_query_list(self,bone_PoseBone):
        rotationMode_str=bone_PoseBone.rotation_mode
        return rotationMode_str

    def scale_edit_func(self,bone_PoseBone,scale):
        bone_PoseBone.scale=scale
    
    def scale_query_list(self,bone_PoseBone):
        scale_vector=bone_PoseBone.scale
        scale_list=[scale_vector[0],scale_vector[1],scale_vector[2]]
        return scale_list

    def customShapeTranslation_edit_func(self,bone_PoseBone,translation):
        bone_PoseBone.custom_shape_translation=translation
    
    def customShapeTranslation_query_list(self,bone_PoseBone):
        translation_vector=bone_PoseBone.custom_shape_translation
        translation_list=[translation_vector[0],translation_vector[1],translation_vector[2]]
        return translation_list
    
    def customShapeScale_edit_func(self,bone_PoseBone,scale):
        bone_PoseBone.custom_shape_scale_xyz=scale
    
    def customShapeScale_query_list(self,bone_PoseBone):
        scale_vector=bone_PoseBone.custom_shape_scale_xyz
        scale_list=[scale_vector[0],scale_vector[1],scale_vector[2]]
        return scale_list

    def IKFKShape_edit_func(self,bone_PoseBone,property_str,param):
        for i in range(len(param)):
            bone_PoseBone[property_str][i]=param[i]

    def IKFKShape_query_list(self,bone_PoseBone,property_str):
        IKFKShape_list=[bone_PoseBone[property_str][i] for i in range(len(bone_PoseBone[property_str]))]
        return IKFKShape_list

    def bendyBone_edit_func(self,bone_PoseBone,curveIn,curveOut):
        #curveIn=(x,z),curveOut=(x,z)    
        bone_PoseBone.bbone_curveinx=curveIn[0]
        bone_PoseBone.bbone_curveinz=curveIn[1]
        bone_PoseBone.bbone_curveoutx=curveOut[0]
        bone_PoseBone.bbone_curveoutz=curveOut[1]
    
    def bendyBone_query_list_list(self,bone_PoseBone):
        #curveIn=(x,z),curveOut=(x,z)
        curveIn_list=[bone_PoseBone.bbone_curveinx,bone_PoseBone.bbone_curveinz]
        curveOut_list=[bone_PoseBone.bbone_curveoutx,bone_PoseBone.bbone_curveoutz]
        return curveIn_list,curveOut_list

    def constraint_edit_func(self,bone_PoseBone,constraint,fromToMinMax,vector):
        constraint_PoseBoneConstraints=bone_PoseBone.constraints[constraint]

    #Setting Function
    def setArmature(self,variable):
        self._armature_str=variable
        return self._armature_str
    def getArmature(self):
        return self._armature_str
    
    def setBone(self,variable):
        self._bone_str=variable
        return self._bone_str
    def getBone(self):
        return self._bone_str
    
    def setProperty(self,variable):
        self._property_str=variable
        return self._property_str
    def getProperty(self):
        return self._property_str
    
    def setTranslation(self,variable):
        self._translation_list=variable
        return self._translation_list
    def currentTranslation(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._translation_list=self.translation_query_list(bone_PoseBone)
        return self._translation_list
    def getTranslation(self):
        return self._translation_list
    
    def setRotation(self,variable):
        self._rotation_list=variable
        return self._rotation_list
    def currentRotation(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._rotation_list=self.rotation_query_list(bone_PoseBone)
        return self._rotation_list
    def getRotation(self):
        return self._rotation_list
    
    def setRotationMode(self,variable):
        self._rotationMode_str=variable
        return self._rotationMode_str
    def currentRotationMode(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._rotationMode_str=self.rotationMode_query_list(bone_PoseBone)
        return self._rotationMode_str
    def getRotationMode(self):
        return self._rotationMode_str
    
    def setScale(self,variable):
        self._scale_list=variable
        return self._scale_list
    def currentScale(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._scale_list=self.scale_query_list(bone_PoseBone)
        return self._scale_list
    def getScale(self):
        return self._scale_list

    def setShapeTranslation(self,variable):
        self._translationShape_list=variable
        return self._translationShape_list
    def currentShapeTranslation(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._translationShape_list=self.customShapeTranslation_query_list(bone_PoseBone)
        return self._translationShape_list
    def getShapeTranslation(self):
        return self._translationShape_list
    
    def setShapeScale(self,variable):
        self._scaleShape_list=variable
        return self._scaleShape_list
    def currentShapeScale(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._scaleShape_list=self.customShapeScale_query_list(bone_PoseBone)
        return self._scaleShape_list
    def getShapeScale(self):
        return self._scaleShape_list
    
    def setIKFKShape(self,variable):
        self._ikfkShape_list=variable
        return self._ikfkShape_list
    def currentIKFKShape(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._ikfkShape_list=self.IKFKShape_query_list(bone_PoseBone,self._property_str)
        return self._ikfkShape_list
    def getIKFKShape(self):
        return self._ikfkShape_list
    
    def setCurveIn(self,variable):
        self._curveIn_list=variable
        return self._curveIn_list
    def currentCurveIn(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._curveIn_list=self.bendyBone_query_list_list(bone_PoseBone)[0]
        return self._curveIn_list
    def getCurveIn(self):
        return self._curveIn_list
    
    def setCurveOut(self,variable):
        self._curveOut_list=variable
        return self._curveOut_list
    def currentCurveOut(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._curveOut_list=self.bendyBone_query_list_list(bone_PoseBone)[1]
        return self._curveOut_list
    def getCurveOut(self):
        return self._curveOut_list

    #Public Function
    def editTranslation(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _translation_list=vector or self._translation_list

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.translation_edit_func(bone_PoseBone,_translation_list)
    
    def editRotation(self,vector=None,mode=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _rotation_list=vector or self._rotation_list
        _mode_str=mode or self._rotationMode_str

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.rotation_edit_func(bone_PoseBone,_rotation_list,_mode_str)
    
    def editScale(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _scale_list=vector or self._scale_list

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.scale_edit_func(bone_PoseBone,_scale_list)
    
    def editCustomShapeTranslation(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _translationShape_list=vector or self._translationShape_list

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.customShapeTranslation_edit_func(bone_PoseBone,_translationShape_list)
    
    def editCustomShapeScale(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _scaleShape_list=vector or self._scaleShape_list

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.customShapeScale_edit_func(bone_PoseBone,_scaleShape_list)

    def editIKFKShape(self,param=None,property_str=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _ikfkShape_list=param or self._ikfkShape_list
        _property_str=property_str or self._property_str

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.IKFKShape_edit_func(bone_PoseBone,_property_str,_ikfkShape_list)

    def editBendyBone(self,curveIn=None,curveOut=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _curveIn_list=curveIn or self._curveIn_list
        _curveOut_list=curveOut or self._curveOut_list

        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.bendyBone_edit_func(bone_PoseBone,_curveIn_list,_curveOut_list)
