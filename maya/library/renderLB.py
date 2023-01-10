# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.mel as mel

import cgInTools as cit
from . import setBaseLB as sbLB
from . import objectLB as oLB
from . import jsonLB as jLB
cit.reloads([sbLB,oLB,jLB])

rules_dict=jLB.getJson(cit.mayaSettings_dir,"library")

class MayaRender(sbLB.BaseRender):
    def __init__(self):
        super(MayaRender,self).__init__()
        self._wrkPath=cmds.workspace(q=True,rd=True)

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
    def __loading(self):
        self._imageFormat_dict=rules_dict["imageFormat_dict"]
        self._exportPath=self._path+"/"+self._exportFolder
        
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

class EquipmentSettings():
    def __init__(self):
        self._settings=[]
        self._settingIndex=0

    #Single Function
    def matrixLayout_create_func(self,settings):
        for setting in settings:
            shapes=setting.getShapeTypes()
            run=setting.getRunMatrix()
            normal=setting.getNormalMatrix()
            world=setting.getWorldMatrix()
            parent=setting.getParentMatrix()
            obj=setting.getObject()
            if not shapes == None:
                shape=cmds.createNode(shapes[0],ss=True)
                node=cmds.listRelatives(shape,p=True)[0]
                create=oLB.MatrixObject(node)
                create.setRunMatrix(run)
                create.setNormalMatrix(normal)
                create.setWorldMatrix(world)
                create.setParentMatrix(parent)
                create.runMovement()
    
    def matrixLayout_edit_func(self,settings):
        for setting in settings:
            setting.runMovement()

    #Public Function
    def setSetting(self,variable):
        self._settings=[variable]
        return self._settings
    def addSetting(self,variable):
        self._settings.append(variable)
        return self._settings
    def getSettings(self):
        return self._settings

    def setSettingIndex(self,variable):
        self._settingIndex=variable
        return self._settingIndex
    def getSettingIndex(self):
        return self._settingIndex

    def querySettingIndex(self):
        return self._settings[self._settingIndex]

    def removeSettingIndex(self):
        self._settings.pop(self._settingIndex)
        return self._settings

    def createLayout(self):
        self.matrixLayout_create_func(self._settings)

    def editLayout(self):
        self.matrixLayout_edit_func(self._settings)