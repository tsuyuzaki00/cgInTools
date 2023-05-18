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

class SelfObject(SelfOrigin):
    def __init__(self):
        super(SelfObject,self).__init__()
        self._object_str=None
        self._translation_list=None
        self._rotation_list=None
        self._rotationMode_str=None
        self._scale_list=None
        self._doParent_str=None

    #Single Function
    def selectObject_query_Object(self,objName_str):
        bpyTypes_Object=bpy.data.objects[objName_str]
        bpy.context.view_layer.objects.active=bpyTypes_Object
        bpy.ops.object.mode_set(mode='OBJECT')
        return bpyTypes_Object

    def translation_edit_func(self,obj_Object,translation):
        obj_Object.location=translation

    def translation_query_list(self,obj_Object):
        translation_vector=obj_Object.location
        translation_list=[translation_vector[0],translation_vector[1],translation_vector[2]]
        return translation_list

    def rotation_edit_func(self,obj_Object,rotation,mode):
        obj_Object.rotation_euler=rotation
        obj_Object.rotation_mode=mode
    
    def rotation_query_list(self,obj_Object):
        rotation_vector=obj_Object.rotation_euler
        rotation_list=[rotation_vector[0],rotation_vector[1],rotation_vector[2]]
        return rotation_list

    def rotationMode_query_str(self,obj_Object):
        rotationMode_str=obj_Object.rotation_mode
        return rotationMode_str

    def scale_edit_func(self,obj_Object,scale):
        obj_Object.scale=scale

    def scale_query_list(self,obj_Object):
        scale_vector=obj_Object.scale
        scale_list=[scale_vector[0],scale_vector[1],scale_vector[2]]
        return scale_list

    #Setting Function
    def setObject(self,variable):
        self._object_str=variable
    def getObject(self):
        return self._object_str

    def setTranslation(self,variable):
        self._translation_list=variable
    def currentTranslation(self):
        obj_Object=self.selectObject_query_Object(self._object_str)
        self._translation_list=self.translation_query_list(obj_Object)
        return self._translation_list
    def getTranslation(self):
        return self._translation_list
    
    def setRotation(self,variable):
        self._rotation_list=variable
    def currentRotation(self):
        obj_Object=self.selectObject_query_Object(self._object_str)
        self._rotation_list=self.rotation_query_list(obj_Object)
        return self._rotation_list
    def getRotation(self):
        return self._rotation_list
    
    def setRotationMode(self,variable):
        self._rotationMode_str=variable
    def currentRotationMode(self):
        obj_Object=self.selectObject_query_Object(self._object_str)
        self._rotationMode_str=self.rotationMode_query_str(obj_Object)
        return self._rotationMode_str
    def getRotationMode(self):
        return self._rotationMode_str
    
    def setScale(self,variable):
        self._scale_list=variable
    def currentScale(self):
        obj_Object=self.selectObject_query_Object(self._object_str)
        self._scale_list=self.scale_query_list(obj_Object)
        return self._scale_list
    def getScale(self):
        return self._scale_list

    def setParent(self,variable):
        self._doParent_str=variable
    def getParent(self):
        return self._doParent_str

    #Public Function
    def translation(self,vector=None,objectName=None):
        _object_str=objectName or self._object_str
        _translation_list=vector or self._translation_list

        object_Object=self.selectObject_query_Object(_object_str)
        self.translation_edit_func(object_Object,_translation_list)
    
    def rotation(self,vector=None,mode=None,objectName=None):
        _object_str=objectName or self._object_str
        _rotation_list=vector or self._rotation_list
        _rotationMode_str=mode or self._rotationMode_str

        object_Object=self.selectObject_query_Object(_object_str)
        self.rotation_edit_func(object_Object,_rotation_list,_rotationMode_str)
    
    def scale(self,vector=None,objectName=None):
        _object_str=objectName or self._object_str
        _scale_list=vector or self._scale_list

        object_Object=self.selectObject_query_Object(_object_str)
        self.scale_edit_func(object_Object,_scale_list)

    def parent(self,objectName=None,parentName=None):
        _object_str=objectName or self._object_str
        _doParent_str=parentName or self._doParent_str

        object_Object=self.selectObject_query_Object(_object_str)
        parent_Object=self.selectObject_query_Object(_doParent_str)

        object_Object.parent=parent_Object
        object_Object.matrix_parent_inverse=parent_Object.matrix_world.inverted()

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
        self._parentBone_str=None
        self._parentConnect_bool=False
        self._head_list=None
        self._tail_list=None
        self._roll_float=None
        self._layerNums=None
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

    def editBone_create_EditBone(self,armature_str,bone_str):
        armature_Object=bpy.data.objects[armature_str]
        bpy.context.view_layer.objects.active=armature_Object
        bpy.ops.object.mode_set(mode='EDIT')

        newBone_EditBone=armature_Object.data.edit_bones.new(bone_str)
        return newBone_EditBone.name

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

    def parentBone_edit_func(self,bone_EditBone,parent_EditBone,connect=False):
        bone_EditBone.parent=parent_EditBone
        bone_EditBone.use_connect=connect

    def layer_edit_func(self,bone_EditBone,layerNums):
        lists=[False]*32
        for layerNum in layerNums:
            bone_EditBone.layers[layerNum]=True
            lists[layerNum]=True
        for i,b in enumerate(lists):
            bone_EditBone.layers[i]=b

    def layer_query_ints(self,bone_EditBone):
        layerNums=[i for i, value in enumerate(bone_EditBone.layers) if value is True]
        return layerNums

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
    
    def setParentBone(self,variable):
        self._parentBone_str=variable
        return self._parentBone_str
    def currentParentBone(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        parentBone_EditBone=bone_EditBone.parent
        self._parentBone_str=parentBone_EditBone.name
        return self._parentBone_str
    def getParentBone(self):
        return self._parentBone_str

    def setParentConnect(self,variable):
        self._parentConnect_bool=variable
        return self._parentConnect_bool
    def currentParentConnect(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._parentConnect_bool=bone_EditBone.use_connect
        return self._parentConnect_bool
    def getParentConnect(self):
        return self._parentConnect_bool
    
    def setLayerNums(self,variables):
        self._layerNums=variables
        return self._layerNums
    def currentLayerNums(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._layerNums=self.layer_query_ints(bone_EditBone)
        return self._layerNums
    def getLayerNums(self):
        return self._layerNums

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
    def createBone(self,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        
        self._bone_str=self.editBone_create_EditBone(_armature_str,_bone_str)
        return self._bone_str

    def parent(self,parentBoneName=None,boneName=None,armatureName=None,parentConnect=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _parentBone_str=parentBoneName or self._parentBone_str
        _parentConnect_bool=parentConnect or self._parentConnect_bool

        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        parentBone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_parentBone_str)
        self.parentBone_edit_func(bone_EditBone,parentBone_EditBone,_parentConnect_bool)

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

    def editLayer(self,layer=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _layerNums=layer or self._layerNums

        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.layer_edit_func(bone_EditBone,_layerNums)

class SelfPoseArmature(SelfOrigin):
    def __init__(self):
        super(SelfPoseArmature,self).__init__()
        self._armature_str=None
        self._bone_str=None
        self._property_str=None
        self._boneConstraint_str=None
        self._attr_str=None
        self._value=None
        self._translation_list=None
        self._rotation_list=None
        self._rotationMode_str=None
        self._scale_list=None
        self._translationShape_list=None
        self._scaleShape_list=None
        self._ikfkShape_list=None
        self._curveIn_list=None
        self._curveOut_list=None
        self._colorIndex_int=None
        self._customShape_str=None
        self._customShapePath_str=None
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
        translation_list=[translation for translation in translation_vector]
        return translation_list
    
    def rotation_edit_func(self,bone_PoseBone,rotation,mode):
        bone_PoseBone.rotation_euler=rotation
        bone_PoseBone.rotation_mode=mode
    
    def rotation_query_list(self,bone_PoseBone):
        rotation_vector=bone_PoseBone.rotation_euler
        rotation_list=[rotation for rotation in rotation_vector]
        return rotation_list

    def rotationMode_query_str(self,bone_PoseBone):
        rotationMode_str=bone_PoseBone.rotation_mode
        return rotationMode_str

    def scale_edit_func(self,bone_PoseBone,scale):
        bone_PoseBone.scale=scale
    
    def scale_query_list(self,bone_PoseBone):
        scale_vector=bone_PoseBone.scale
        scale_list=[scale for scale in scale_vector]
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

    def boneConstraint_edit_func(self,bone_PoseBone,boneConstraint,attr,value):
        constraint_PoseBoneConstraints=bone_PoseBone.constraints[boneConstraint]
        exec("constraint_PoseBoneConstraints"+"."+attr+"="+str(value))
    
    def boneConstraint_query_value(self,bone_PoseBone,boneConstraint,attr):
        constraint_PoseBoneConstraints=bone_PoseBone.constraints[boneConstraint]
        boneConstraintValue_value=eval("constraint_PoseBoneConstraints"+"."+attr)
        return boneConstraintValue_value

    def colorIndex_edit_func(self,bone_PoseBone,colorIndex):
        bone_PoseBone.bone_group_index=colorIndex

    def colorIndex_query_int(self,bone_PoseBone):
        colorIndex=bone_PoseBone.bone_group_index
        return colorIndex

    def customShape_edit_func(self,bone_PoseBone,customShape_str,customShapePath_str):
        bone_PoseBone.custom_shape=bpy.data.objects[customShape_str,customShapePath_str]

    def customShape_query_str(self,bone_PoseBone):
        customShape_str=bone_PoseBone.custom_shape.name
        return customShape_str

    def customShapePath_query_str(self,bone_PoseBone):
        customShapePath_str=bone_PoseBone.custom_shape.library.filepath
        customShapePath_raw=repr(customShapePath_str)
        customShapePath_str=customShapePath_raw.replace("'","",2)
        return customShapePath_str

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
    
    def setBoneConstraint(self,variable):
        self._boneConstraint_str=variable
        return self._boneConstraint_str
    def getBoneConstraint(self):
        return self._boneConstraint_str

    def setAttr(self,variable):
        self._attr_str=variable
    def getAttr(self):
        return self._attr_str

    def setValue(self,variable):
        self._value=variable
    def getValue(self):
        return self._value
    
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
        self._rotationMode_str=self.rotationMode_query_str(bone_PoseBone)
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

    def setColorIndex(self,variable):
        self._colorIndex_int=variable
        return self._colorIndex_int
    def currentColorIndex(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._colorIndex_int=self.colorIndex_query_int(bone_PoseBone)
        return self._colorIndex_int
    def getColorIndex(self):
        return self._colorIndex_int    
    
    def setCustomShape(self,variable):
        self._customShape_str=variable
        return self._customShape_str
    def currentCustomShape(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._customShape_str=self.customShape_query_str(bone_PoseBone)
        return self._customShape_str
    def getCustomShape(self):
        return self._customShape_str    
    
    def setCustomShapePath(self,variable):
        self._customShapePath_str=variable
        return self._customShapePath_str
    def currentCustomShapePath(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._customShapePath_str=self.customShapePath_query_str(bone_PoseBone)
        return self._customShapePath_str
    def getCustomShapePath(self):
        return self._customShapePath_str    
    
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

    def editBoneConstraint(self,value=None,attr=None,boneConstraint=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _boneConstraint_str=boneConstraint or self._boneConstraint_str
        _attr_str=attr or self._attr_str
        _value=value or self._value
        
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.boneConstraint_edit_func(bone_PoseBone,_boneConstraint_str,_attr_str,_value)

    def queryBoneConstraint(self,attr=None,boneConstraint=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _boneConstraint_str=boneConstraint or self._boneConstraint_str
        _attr_str=attr or self._attr_str
        
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        value=self.boneConstraint_query_value(bone_PoseBone,_boneConstraint_str,_attr_str)
        return value

    def editCustomShape(self,shape=None,colorIndex=None,shapePath=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _customShape_str=shape or self._customShape_str
        _colorIndex_int=colorIndex or self._colorIndex_int
        _customShapePath_str=shapePath or self._customShapePath_str
        
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        bone_PoseBone.rotation_mode="XYZ"
        self.customShape_edit_func(bone_PoseBone,_customShape_str,_customShapePath_str)
        bone_PoseBone.bone.show_wire=True
        self.colorIndex_edit_func(bone_PoseBone,_colorIndex_int)

class SelfLattice(SelfObject):
    def __init__(self):
        super(SelfLattice,self).__init__()

class SelfVertexGroups(SelfOrigin):
    def __init__(self):
        super(SelfVertexGroups,self).__init__()
        self._self_list=[]
        self._mesh_str=None
        self._vertexGroup_strs=None

    #Single Function
    def selectMesh_query_Mesh(self,meshName):
        mesh_Object=bpy.data.objects[meshName]
        bpy.context.view_layer.objects.active=mesh_Object
        bpy.ops.object.mode_set(mode='OBJECT')
        return mesh_Object

    def vertexGroup_create_str(self,mesh_Object,groupName_str):
        mesh_vertexGroup=mesh_Object.vertex_groups.new(name=groupName_str)
        return mesh_vertexGroup.name

    #Setting Function
    def setSelfList(self,variables):
        self._self_list=[variable for variable in variables]
    def addSelfList(self,variables):
        self._self_list+=[variable for variable in variables]
    def getSelfList(self):
        return self._self_list

    def setMesh(self,variable):
        self._mesh_str=variable
    def getMesh(self):
        return self._mesh_str
    
    def setVertexGroups(self,variables):
        self._vertexGroup_strs=[variable for variable in variables]
    def addVertexGroups(self,variables):
        self._vertexGroup_strs+=[variable for variable in variables]
    def getVertexGroups(self):
        return self._vertexGroup_strs

    #Public Function
    def createJsonDicts(self):
        write_dicts=[]
        for _self in self._self_list:
            _self.setSetChoices(["DoIts","Mesh","VertexGroup","VertexID","Weight"])
            _self.setDoIts(["editWeight"])
            write_dict=_self.writeDict()
            write_dicts.append(write_dict)
        return write_dicts

    def queryMesh(self,mesh=None):
        _mesh_str=mesh or self._mesh_str

        mesh_VertexGroup=SelfVertexGroup()
        mesh_VertexGroup.setMesh(_mesh_str)
        mesh_Object=self.selectMesh_query_Mesh(_mesh_str)

        mesh_Mesh=mesh_Object.data
        verticeIDs=[]
        for vertexGroup_vertexGroup in mesh_Object.vertex_groups:
            mesh_VertexGroup.setVertexGroup(vertexGroup_vertexGroup.name)
            for vertex in mesh_Mesh.vertices:
                for group in vertex.groups:
                    if group.group == vertexGroup_vertexGroup.index:
                        verticeIDs.append(vertex.index)
            for verticeID in verticeIDs:
                mesh_VertexGroup.setVertexID(verticeID)
                weight_float=vertexGroup_vertexGroup.weight(verticeID)
                mesh_VertexGroup.setWeight(weight_float)
                self._self_list.append(mesh_VertexGroup)
        return self._self_list

    def queryVertexGroups(self,mesh=None,vertexGroups=None):
        _mesh_str=mesh or self._mesh_str
        _vertexGroup_strs=vertexGroups or self._vertexGroup_strs

        mesh_VertexGroup=SelfVertexGroup()
        mesh_VertexGroup.setMesh(_mesh_str)
        mesh_Object=self.selectMesh_query_Mesh(_mesh_str)

        mesh_Mesh=mesh_Object.data
        verticeIDs=[]
        for _vertexGroup_str in _vertexGroup_strs:
            vertexGroup_vertexGroup=mesh_Object.vertex_groups[_vertexGroup_str]
            mesh_VertexGroup.setVertexGroup(_vertexGroup_str)
            for vertex in mesh_Mesh.vertices:
                for group in vertex.groups:
                    if group.group == vertexGroup_vertexGroup.index:
                        verticeIDs.append(vertex.index)
            for verticeID in verticeIDs:
                mesh_VertexGroup.setVertexID(verticeID)
                weight_float=vertexGroup_vertexGroup.weight(verticeID)
                mesh_VertexGroup.setWeight(weight_float)
                self._self_list.append(mesh_VertexGroup)
        return self._self_list

class SelfVertexGroup(SelfOrigin):
    def __init__(self):
        super(SelfVertexGroup,self).__init__()
        self._mesh_str=None
        self._vertexGroup_str=None
        self._vertexID_int=None
        self._weight_float=None
        self._setChoices+=[
        ]
        self._doIts+=[
        ]

    #Single Function
    def selectMesh_query_Mesh(self,meshName):
        mesh_Object=bpy.data.objects[meshName]
        bpy.context.view_layer.objects.active=mesh_Object
        bpy.ops.object.mode_set(mode='OBJECT')
        return mesh_Object

    def vertexGroup_create_str(self,mesh_Object,groupName_str):
        mesh_vertexGroup=mesh_Object.vertex_groups.new(name=groupName_str)
        return mesh_vertexGroup.name

    def convertMeshObject_create_vertexGroup(self,mesh_Object,vertexGroup_str):
        mesh_vertexGroup=mesh_Object.vertex_groups[vertexGroup_str]
        return mesh_vertexGroup

    def weight_edit_func(self,mesh_vertexGroup,vertexID_int,weight_float):
        mesh_vertexGroup.add([vertexID_int],weight_float,'REPLACE')
    
    def weight_query_func(self,mesh_vertexGroup,vertexID_int):
        weight_float=mesh_vertexGroup.weight(vertexID_int)
        return weight_float

    #Setting Function
    def setMesh(self,variable):
        self._mesh_str=variable
    def getMesh(self):
        return self._mesh_str
    
    def setVertexGroup(self,variable):
        self._vertexGroup_str=variable
    def getVertexGroup(self):
        return self._vertexGroup_str

    def setVertexID(self,variable):
        self._vertexID_int=variable
    def getVertexID(self):
        return self._vertexID_int

    def setWeight(self,variable):
        self._weight_float=variable
    def currrentWeight(self):
        mesh_Mesh=self.selectMesh_query_Mesh(self._mesh_str)
        mesh_vertexGroup=self.convertMeshObject_create_vertexGroup(mesh_Mesh,self._vertexGroup_str)
        self._weight_float=self.weight_query_func(mesh_vertexGroup,self._vertexID_int)
        return self._weight_float
    def getWeight(self):
        return self._weight_float

    #Public Function
    def createVertexGroup(self,mesh=None,vertexGroupName=None):
        _mesh_str=mesh or self._mesh_str
        _vertexGroup_str=vertexGroupName or self._vertexGroup_str

        mesh_Mesh=self.selectMesh_query_Mesh(_mesh_str)
        self.vertexGroup_create_str(mesh_Mesh,_vertexGroup_str)

    def editWeight(self,mesh=None,vertexGroupName=None,vertexID=None,weight=None):
        _mesh_str=mesh or self._mesh_str
        _vertexGroup_str=vertexGroupName or self._vertexGroup_str
        _vertexID_int=vertexID or self._vertexID_int
        _weight_float=weight or self._weight_float
        
        mesh_Mesh=self.selectMesh_query_Mesh(_mesh_str)
        mesh_vertexGroup=self.convertMeshObject_create_vertexGroup(mesh_Mesh,_vertexGroup_str)
        self.weight_edit_func(mesh_vertexGroup,_vertexID_int,_weight_float)

class SelfVertexWeight(SelfOrigin):
    def __init__(self):
        super(SelfVertexGroup,self).__init__()
        self._object_str=None
        self._subject_str=None
        self._vertexID_int=None
        self._weight_float=None
        self._setChoices+=[
        ]
        self._doIts+=[
        ]