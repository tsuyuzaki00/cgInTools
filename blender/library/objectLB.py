import bpy

class SelfEditArmature(object):
    def __init__(self):
        self._armature_str=None
        self._bone_str=None
        self._head_list=None
        self._tail_list=None
        self._roll_float=None

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
    def writeDict(self):
        write_dict={
            "armature":self._armature_str,
            "bone":self._bone_str,
            "head":self._head_list,
            "tail":self._tail_list,
            "roll":self._roll_float
        }
        return write_dict

    def readDict(self,read_dict):
        self._armature_str=read_dict["armature"]
        self._bone_str=read_dict["bone"]
        self._head_list=read_dict["head"]
        self._tail_list=read_dict["tail"]
        self._roll_float=read_dict["roll"]

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

class SelfPoseArmature(object):
    def __init__(self):
        self._armature_str=None
        self._bone_str=None
        self._property_str=None
        self._trans_list=None
        self._scale_list=None
        self._FKIKShape_list=None
        self._curveIn_list=None
        self._curveOut_list=None

    #Single Function
    def selectPoseBone_query_PoseBone(self,armatureName,boneName):
        armature_Object=bpy.data.objects[armatureName]
        bpy.context.view_layer.objects.active=armature_Object
        bpy.ops.object.mode_set(mode='POSE')

        bone_PoseBone=armature_Object.pose.bones[boneName]
        return bone_PoseBone

    def customShapeTrans_edit_func(self,bone_PoseBone,trans)
        bone_PoseBone.custom_shape_translation=trans
    
    def customShapeTrans_query_list(self,bone_PoseBone)
        trans_list=bone_PoseBone.custom_shape_translation
        return trans_list
    
    def customShapeScale_edit_func(self,bone_PoseBone,scale)
        bone_PoseBone.custom_shape_scale_xyz=scale
    
    def customShapeScale_query_list(self,bone_PoseBone)
        scale_list=bone_PoseBone.custom_shape_scale_xyz
        return scale_list

    def IKFKShape_edit_func(bone_PoseBone,property,param):
        for i in range(len(param)):
            bone_PoseBone[property][i]=param[i]

    def IKFKShape_query_list(bone_PoseBone,property):
        IKFKShape_list=[bone_PoseBone[property][i] for i in range(bone_PoseBone[property])]
        return IKFKShape_list

    def bendyBone_edit_func(bone_PoseBone,curveIn,curveOut):
        #curveIn=(x,z),curveOut=(x,z)    
        bone_PoseBone.bbone_curveinx=curveIn[0]
        bone_PoseBone.bbone_curveinz=curveIn[1]
        bone_PoseBone.bbone_curveoutx=curveOut[0]
        bone_PoseBone.bbone_curveoutz=curveOut[1]
    
    def bendyBone_query_list_list(bone_PoseBone):
        #curveIn=(x,z),curveOut=(x,z)
        curveIn_list=[bone_PoseBone.bbone_curveinx,bone_PoseBone.bbone_curveinz]
        curveOut_list=[bone_PoseBone.bbone_curveoutx,bone_PoseBone.bbone_curveoutz]
        return curveIn_list,curveOut_list

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
    
    def setTrans(self,variable):
        self._trans_list=variable
        return self._trans_list
    def currentTrans(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._trans_list=self.customShapeTrans_query_list(bone_EditBone)
        return self._trans_list
    def getTrans(self):
        return self._trans_list
    
    def setScale(self,variable):
        self._scale_list=variable
        return self._scale_list
    def currentScale(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._scale_list=self.customShapeScale_query_list(bone_EditBone)
        return self._scale_list
    def getScale(self):
        return self._scale_list
    
    def setFKIKShape(self,variable):
        self._FKIKShape_list=variable
        return self._FKIKShape_list
    def currentFKIKShape(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._FKIKShape_list=self.IKFKShape_query_list(bone_EditBone,self._property_str)
        return self._FKIKShape_list
    def getFKIKShape(self):
        return self._FKIKShape_list
    
    def setCurveIn(self,variable):
        self._curveIn_list=variable
        return self._curveIn_list
    def currentCurveIn(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._curveIn_list=self.bendyBone_query_list_list(bone_EditBone)[0]
        return self._curveIn_list
    def getCurveIn(self):
        return self._curveIn_list
    
    def setCurveOut(self,variable):
        self._curveOut_list=variable
        return self._curveOut_list
    def currentCurveOut(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._curveOut_list=self.bendyBone_query_list_list(bone_EditBone)[1]
        return self._curveOut_list
    def getCurveOut(self):
        return self._curveOut_list

    #Public Function
    def writeDict(self):
        write_dict={
            "armature":self._armature_str,
            "bone":self._bone_str,
            "property":self._property_str
            "trans":self._trans_list
            "scale":self._scale_list
            "FKIKShape":self._FKIKShape_list
            "curveIn":self._curveIn_list
            "curveOut":self._curveOut_list
        }
        return write_dict

    def readDict(self,read_dict):
        self._armature_str=read_dict["armature"]
        self._bone_str=read_dict["bone"]
        self._property_str=read_dict["property"]
        self._trans_list=read_dict["trans"]
        self._scale_list=read_dict["scale"]
        self._FKIKShape_list=read_dict["FKIKShape"]
        self._curveIn_list=read_dict["curveIn"]
        self._curveOut_list=read_dict["curveOut"]

    def editTrans(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _trans_list=vector or self._trans_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.customShapeTrans_edit_func(bone_EditBone,_trans_list)
    
    def editScale(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _scale_list=vector or self._scale_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.customShapeScale_edit_func(bone_EditBone,_scale_list)

    def editFKIKShape(self,param=None,property=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _FKIKShape_list=param or self._FKIKShape_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.roll_edit_func(bone_EditBone,_FKIKShape_list)
