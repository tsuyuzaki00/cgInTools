# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.mel as mel

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
cit.reloads([sbLB,jLB])

rules_dict=jLB.getJson(cit.mayaSettings_path,"library")

class MayaRender(sbLB.BaseRender):
    def __init__(self):
        super(MayaRender,self).__init__()
        self._wrkPath=cmds.workspace(q=True,rd=True)

    def __loading(self):
        self._imageFormat_dict=rules_dict["imageFormat_dict"]
        self._exportPath=self._path+"/"+self._exportFolder

    #Single Function
    def shotImage_create_func(self,path,file,imageFormat,camera,width,height,isRenderer):
        cameraShape_list=cmds.listRelatives(camera,s=True)
        if cameraShape_list == None:
            return
        cmds.workspace(path,o=True)
        cmds.setAttr("perspShape"+".renderable",0)
        cmds.setAttr("defaultRenderGlobals.animation",0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix",file,type="string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer",isRenderer,type="string")
        cmds.setAttr("defaultResolution.width",width)
        cmds.setAttr("defaultResolution.height",height)
        cmds.setAttr("defaultRenderGlobals.imageFormat",imageFormat)
        cmds.setAttr(cameraShape_list[0]+".renderable",1)
        cmds.render(b=True,rep=True)

    def sequence_create_func(self,path,file,imageFormat,camera,width,height,isRenderer,startFrame,endFrame):
        cameraShape_list=cmds.listRelatives(camera,s=True)
        if cameraShape_list == None:
            return
        cmds.workspace(path,o=True)
        cmds.setAttr("perspShape" + ".renderable", 0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix",file,type="string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer",isRenderer,type="string")
        cmds.setAttr("defaultResolution.width",width)
        cmds.setAttr("defaultResolution.height",height)
        cmds.setAttr("defaultRenderGlobals.imageFormat",imageFormat)
        cmds.setAttr(cameraShape_list[0]+".renderable",1)
        cmds.setAttr("defaultRenderGlobals.startFrame",startFrame)
        cmds.setAttr("defaultRenderGlobals.endFrame",endFrame)
        cmds.setAttr("defaultRenderGlobals.animation",1)
        cmds.setAttr("defaultRenderGlobals.animationRange",0)
        cmds.setAttr("defaultRenderGlobals.extensionPadding",3)
        cmds.setAttr("defaultRenderGlobals.outFormatControl",0)
        cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt",1)
        cmds.setAttr("defaultRenderGlobals.periodInExt",2)
        mel.eval("RenderSequence")
    
    def batch_create_func(self,path,file,imageFormat,camera,width,height,isRenderer,startFrame,endFrame):
        cameraShape_list=cmds.listRelatives(camera,s=True)
        if cameraShape_list == None:
            return
        cmds.workspace(path,o=True)
        cmds.setAttr("perspShape" + ".renderable", 0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix",file,type="string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer",isRenderer,type="string")
        cmds.setAttr("defaultResolution.width",width)
        cmds.setAttr("defaultResolution.height",height)
        cmds.setAttr("defaultRenderGlobals.imageFormat",imageFormat)
        cmds.setAttr(cameraShape_list[0]+".renderable",1)
        cmds.setAttr("defaultRenderGlobals.startFrame",startFrame)
        cmds.setAttr("defaultRenderGlobals.endFrame",endFrame)
        cmds.setAttr("defaultRenderGlobals.animation",1)
        cmds.setAttr("defaultRenderGlobals.animationRange",0)
        cmds.setAttr("defaultRenderGlobals.extensionPadding",3)
        cmds.setAttr("defaultRenderGlobals.outFormatControl",0)
        cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt",1)
        cmds.setAttr("defaultRenderGlobals.periodInExt",2)
        mel.eval("BatchRender")

    def playblast_create_func(self,path,file,camera,width,height,startFrame,endFrame):
        cmds.workspace(path,o=True)
        cmds.lookThru(camera)
        cmds.playblast(st=startFrame,et=endFrame,fo=True,w=width,h=height,v=False,c="h264",orn=True,fmt="qt",p=100,f=path+"/"+file)

    #(仮)
    def wireFrameImage_create_func(self,path,file,imageFormat,camera,width,height,isRenderer):
        cameraShape_list=cmds.listRelatives(camera,s=True)
        if cameraShape_list == None:
            return
        cmds.workspace(path,o=True)
        cmds.setAttr("perspShape"+".renderable",0)
        cmds.setAttr("defaultRenderGlobals.animation",0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix",file,type = "string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer",isRenderer,type = "string")
        cmds.setAttr("defaultResolution.width",width)
        cmds.setAttr("defaultResolution.height",height)
        cmds.setAttr("defaultRenderGlobals.imageFormat",imageFormat)
        cmds.setAttr(cameraShape_list[0]+".renderable",1)
        cmds.render(b=True,rep=True)

    #Public Function
    def shotImage(self):
        self.__loading()
        self._imageFormat=self._imageFormat_dict[self._extension]
        self.shotImage_create_func(self._exportPath,self._file,self._imageFormat,self._camera,self._width,self._height,self._isRenderer)
    
    def sequence(self):
        self.__loading()
        self._imageFormat=self._imageFormat_dict[self._extension]
        self.sequence_create_func(self._exportPath,self._file,self._imageFormat,self._camera,self._width,self._height,self._isRenderer,self._start,self._end)
    
    def batch(self):
        self.__loading()
        self._imageFormat=self._imageFormat_dict[self._extension]
        self.batch_create_func(self._exportPath,self._file,self._imageFormat,self._camera,self._width,self._height,self._isRenderer,self._start,self._end)
    
    def playblast(self):
        self.batch_create_func(self._exportPath,self._file,self._camera,self._width,self._height,self._start,self._end)

class CameraSettings():
    def __init__(self):
        self._cameras=[]

    # カメラorライトを配置する関数
    def photo_create_obj2(self,typeName="camera",trs=(0,100,500),rot=(0,0,0)):
        if typeName == "camera":
            cam = self.camera_create()
            self.position_setting(cam,trs,rot)
            return cam
        if typeName == "light":
            lit = self.light_create()
            self.position_setting(lit,trs,rot)
            return lit

    # カメラ自体を作成する関数
    def camera_create_obj2(self):
        cam = cmds.camera(name="")
        return cam

    # ライト自体を作成する関数
    def light_create_obj2(self):
        lit = cmds.directionalLight()
        lit = cmds.pointLight()
        lit = cmds.spotLight()
        lit = cmds.ambientLight()
        return lit

    # カメラかライトの位置を決める関数
    def position_edit_obj(self,obj,trs=(0,0,5),rot=(0,0,0)):
        cmds.setAttr(obj+".translate",trs[0],trs[1],trs[2],type="double3")
        cmds.setAttr(obj+".rotate",rot[0],rot[1],rot[2],type="double3")

    # viewに存在するカメラを取得する
    def camera_query_obj():
        pass

    def renderGlobal_query_func():
        cmds.select("defaultRenderGlobals")

class GetCameraRender():
    def __init__(self):
        self._cameras=[]