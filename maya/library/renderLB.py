# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.mel as mel

class MayaRender():
    def __init__(self):
        self.rootDirectory = cmds.workspace(q=True,rd=True)

    # 画像を出力する関数
    def shotImage_create_func(self,fileName,camera,width,height,imageFormat,isRenderer):
        camera_shape = cmds.listRelatives(camera)[0]
        mel.eval('setProject "%s";' % self.rootDirectory)
        cmds.setAttr("perspShape"+".renderable",0)
        cmds.setAttr("defaultRenderGlobals.animation",0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix",fileName,type = "string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer",isRenderer,type = "string")
        cmds.setAttr("defaultResolution.width",width)
        cmds.setAttr("defaultResolution.height",height)
        cmds.setAttr("defaultRenderGlobals.imageFormat",imageFormat)
        cmds.setAttr(camera_shape+".renderable",1)
        cmds.render(b=True,rep=True)

    # シーケンスを出力する関数
    def sequence_create_func(self,fileName,camera,width,height,imageFormat,isRenderer,startFrame,endFrame):
        camera_shape = cmds.listRelatives(camera)[0]
        mel.eval('setProject "%s";' % self.rootDirectory)
        cmds.setAttr("perspShape" + ".renderable", 0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix", fileName, type = "string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer", isRenderer, type = "string")
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        cmds.setAttr("defaultRenderGlobals.imageFormat", imageFormat)
        cmds.setAttr(camera_shape + ".renderable", 1)
        cmds.setAttr("defaultRenderGlobals.startFrame", startFrame)
        cmds.setAttr("defaultRenderGlobals.endFrame", endFrame)
        cmds.setAttr("defaultRenderGlobals.animation", 1)
        cmds.setAttr("defaultRenderGlobals.animationRange", 0)
        cmds.setAttr("defaultRenderGlobals.extensionPadding", 3)
        cmds.setAttr("defaultRenderGlobals.outFormatControl", 0)
        cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt", 1)
        cmds.setAttr("defaultRenderGlobals.periodInExt", 2)
        mel.eval("BatchRender")
        #mel.eval("RenderSequence")

    # プレイブラストで動画を出力する関数
    def playblast_create_func(self,fileName,camera,width,height,startFrame,endFrame):
        mel.eval('setProject "%s";' % self.rootDirectory)
        path = cmds.workspace(q=True,rootDirectory=1)+"movies/"
        cmds.lookThru(camera)
        cmds.playblast(st=startFrame,et=endFrame,fo=True,w=width,h=height,v=False,c="h264",orn=True,fmt="qt",p=100,f=path+fileName)

    # ワイヤーフレームで画像を出力する関数(仮)
    def wireFrameImage_create_func(self,fileName,camera,width,height,imageFormat,isRenderer):
        camera_node = camera[0]
        camera_shape = camera[1]
        mel.eval('setProject "%s";' % self.rootDirectory)
        cmds.setAttr("perspShape"+".renderable",0)
        cmds.setAttr("defaultRenderGlobals.animation",0)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix",fileName,type = "string")
        cmds.setAttr("defaultRenderGlobals.currentRenderer",isRenderer,type = "string")
        cmds.setAttr("defaultResolution.width",width)
        cmds.setAttr("defaultResolution.height",height)
        cmds.setAttr("defaultRenderGlobals.imageFormat",imageFormat)
        cmds.setAttr(camera_shape+".renderable",1)
        cmds.render(b=True,rep=True)
class CameraSettings():
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