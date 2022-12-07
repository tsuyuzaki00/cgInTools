# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.mel as mel
import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
cit.reloads([sbLB])

import os
import re

class Check(sbLB.BaseCheck):
    def __init__(self):
        self._relation=""
        self._same=""
        self._same_list=[]
        self._maxLimit=100
        self._minLimit=0
        self._highLimit=100
        self._lowLimit=0
        self._edit=False
        self._path=""
        self._node=""
        self._attr=""
        self._evaluation_dict={"bool":False}
    
    #Public Function
    #same relation check
    def attrSame(self):
        judge_dict=self.attrSame_check_dict(self._node,self._attr,self._same,self._edit)
        return judge_dict

    def sameRelation(self):
        judge_dict=self.sameRelation_check_dict(self._relation,self._same)
        return judge_dict

    def relationIsSame(self):
        judge_dict=self.relationIsSame_check_dict(self._relation,self._same)
        return judge_dict

    def includedString(self):
        judge_dict=self.includedString_check_dict(self._relation,self._same)
        return judge_dict

    def minRelation(self):
        judge_dict=self.minRelation_check_dict(self._relation,self._minLimit)
        return judge_dict

    def maxRelation(self):
        judge_dict=self.maxRelation_check_dict(self._relation,self._maxLimit)
        return judge_dict

    def minMaxRelation(self):
        judge_dict=self.minMaxRelation_check_dict(self._relation,self._minLimit,self._maxLimit)
        return judge_dict

    def lowRelation(self):
        judge_dict=self.minRelation_check_dict(self._relation,self._lowLimit)
        return judge_dict

    def highRelation(self):
        judge_dict=self.maxRelation_check_dict(self._relation,self._highLimit)
        return judge_dict

    #path check
    def thePath(self):
        judge_dict=self.thePath_check_dict(self._relation)
        return judge_dict

    def pathUnderCount(self):
        judge_dict=self.pathUnderCount_check_dict(self._maxLimit)
        return judge_dict

    def fileUnderCount(self):
        judge_dict=self.fileUnderCount_check_dict(self._maxLimit)
        return judge_dict

    #node check
    def nodeUnLocked(self):
        judge_dict=self.nodeUnLocked_check_dict(self._node)
        return judge_dict

    def sameObjName(self):
        judge_dict=self.sameObjName_check_dict(self._node)
        return judge_dict

    def trashReferences(self):
        judge_dict=self.trashReferences_check_dict(self._node)
        return judge_dict

    def nonChild(self):
        judge_dict=self.nonChild_check_dict(self._node)
        return judge_dict
    
    def nonExpression(self):
        judge_dict=self.nonExpression_check_dict(self._node)
        return judge_dict

    def nonConstrained(self):
        judge_dict=self.nonConstrained_check_dict(self._node)
        return judge_dict
    
    def nonDefaultMatrial(self):
        judge_dict=self.nonDefaultMatrial_check_dict(self._node)
        return judge_dict
    
    def nonDefaultName(self):
        judge_dict=self.nonDefaultName_check_dict(self._node)
        return judge_dict
    
    def nonNameSpace(self):
        judge_dict=self.nonNameSpace_check_dict(self._node)
        return judge_dict
    
    def nonDisplayLayer(self):
        judge_dict=self.nonDisplayLayer_check_dict(self._node)
        return judge_dict
    
    # mel.eval('polyCleanupArgList 4 ...) konoyarou!
    #def nonConcave(self):
        #judge_dict=self.nonConcave_check_dict(self._node)
        #return judge_dict
    
    def pivotIsWorldTransform(self):
        judge_dict=self.pivotIsWorldTransform_check_dict(self._node)
        return judge_dict
    
    def frozenTransform(self):
        judge_dict=self.frozenTransform_check_dict(self._node)
        return judge_dict
    
    def showObject(self):
        judge_dict=self.showObject_check_dict(self._node)
        return judge_dict
    
    def cleanHistory(self):
        judge_dict=self.cleanHistory_check_dict(self._node)
        return judge_dict

    def nonKeyedObject(self):
        judge_dict=self.nonKeyedObject_check_dict(self._node)
        return judge_dict
    
    def limina(self):
        judge_dict=self.limina_check_dict(self._node)
        return judge_dict

    def ngon(self):
        judge_dict=self.ngon_check_dict(self._node)
        return judge_dict
    
    def unlockedNormal(self):
        judge_dict=self.unlockedNormal_check_dict(self._node)
        return judge_dict
    
    def noShapeInTheParents(self):
        judge_dict=self.noShapeInTheParents_check_dict(self._node)
        return judge_dict

    def overlappingUV(self):
        judge_dict=self.overlappingUV_check_dict(self._node)
        return judge_dict

    def noUV(self):
        judge_dict=self.noUV_check_dict(self._node)
        return judge_dict
    
    #same multiple check    
    def andSameRelation(self):
        judge_dict=self.andSameRelation_check_dict(self._relation,self._same_list)
        return judge_dict
    
    def andMatchRelation(self):
        judge_dict=self.andMatchRelation_check_dict(self._relation,self._same_list)
        return judge_dict

    #Private Function

    #Mulch Function
    def pathUnderCount_check_dict(self,maxLimit):
        file_path=cmds.file(q=True,sn=True)
        pathParts_list=file_path.lower().split('/')
        evaluation_dict=self.nameUnderCount_check_dict(pathParts_list,maxLimit)
        return evaluation_dict

    def fileUnderCount_check_dict(self,maxLimit):
        file_path=cmds.file(q=True,sn=True)
        ma_file=os.path.basename(file_path)
        nameParts_list=ma_file.replace('.ma','').lower().split('_')
        evaluation_dict=self.nameUnderCount_check_dict(nameParts_list,maxLimit)
        return evaluation_dict

    def attrSame_check_dict(self,node,attr,same,edit=False):
        relation=cmds.getAttr(node+"."+attr)
        evaluation_dict=self.sameRelation_check_dict(relation,same)
        evaluation_dict["node"]=node
        evaluation_dict["attr"]=attr
        if edit:
            if evaluation_dict["bool"]:
                return evaluation_dict
            else:
                cmds.setAttr(node+"."+attr,same)
                return evaluation_dict
        else:
            return evaluation_dict

    def nameUnderCount_check_dict(self,relations,maxLimit):
        numRelation=len(relations)
        evaluation_dict=self.maxRelation_check_dict(numRelation,maxLimit)
        return evaluation_dict        

    #Single Function
    #same relation check
    def sameRelation_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if relation == same:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def relationIsSame_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if relation is same:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def includedString_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if same in relation:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def minRelation_check_dict(self,relation,minLimit):
        evaluation_dict={"bool":False,"relation":relation,"minLimit":minLimit}
        if minLimit <= relation:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def maxRelation_check_dict(self,relation,maxLimit):
        evaluation_dict={"bool":False,"relation":relation,"maxLimit":maxLimit}
        if relation <= maxLimit:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def minMaxRelation_check_dict(self,relation,minLimit,maxLimit):
        evaluation_dict={"bool":False,"relation":relation,"minLimit":minLimit,"maxLimit":maxLimit}
        if minLimit <= relation and relation <= maxLimit:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def lowRelation_check_dict(self,relation,lowLimit):
        evaluation_dict={"bool":False,"relation":relation,"lowLimit":lowLimit}
        if relation < lowLimit:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def highRelation_check_dict(self,relation,highLimit):
        evaluation_dict={"bool":False,"relation":relation,"highLimit":highLimit}
        if highLimit < relation:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    #path check
    def thePath_check_dict(self,relation):
        evaluation_dict={"bool":False,"relation":relation}
        if os.path.isdir(os.path.dirname(relation)):
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    #node check
    def nodeUnLocked_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if cmds.lockNode(node,q=True)[0]:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def sameObjName_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if ':' in node:
            pass
        if '|' in node:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def trashReferences_check_dict(self,node):
        evaluation_dict={"bool":False,"reference":node}
        try:
            cmds.referenceQuery(node,filename=True)
            evaluation_dict["bool"]=True
            return evaluation_dict
        except RuntimeError:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def nonChild_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        child=cmds.listRelatives(node,ad=True)
        if child is None:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else :
            evaluation_dict["bool"]=True
            return evaluation_dict

    def nonExpression_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        child=cmds.listRelatives(node,ad=True)
        expression=cmds.listConnections(node,type='expression')
        if expression is None:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict
    
    def nonConstrained_check_dict(self,node):
        constraint_list=[
            "parentConstraint",
            "pointConstraint",
            "orientConstraint",
            "scaleConstraint",
            "aimConstraint",
            "poleVectorConstraint"
        ]
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node}
        for constraint in constraint_list:
            if cmds.listConnections(node,type=constraint):
                evaluation_bools.append(True)
        if True in evaluation_bools:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def nonDefaultMatrial_check_dict(self,node):
        defaultMatrial_list=[
            "lambert",
            "blinn",
            "phong",
            "layeredShader",
            "standardSurface",
            "anisotropic",
            "oceanShader",
            "rampShader",
            "shadingMap",
            "surfaceShader",
            "aiStandardSurface",
            "aiWireframe",
            "aiUtility",
            "aiTwoSided",
            "aiToon",
            "aiSwitch",
            "aiStandardHair",
            "aiShadowMatte",
            "aiRaySwitch",
            "aiPassthrough",
            "aiMixShader",
            "aiMatte",
            "aiMaterialXShader",
            "aiLayerShader",
            "aiLambert",
            "aiFlat",
            "aiClipGeo",
            "aiCarPaint",
            "aiAxfShader",
        ]
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node}
        history_list=cmds.listHistory(node,f=1)
        shadingEngine_node=cmds.ls(history_list,type="shadingEngine")[0]
        if not cmds.connectionInfo(shadingEngine_node+".surfaceShader",id=True):
            evaluation_dict["bool"]=False
            return evaluation_dict
        material_node=cmds.listConnections(shadingEngine_node+".surfaceShader",s=True)[0]
        for defaultMatrial in defaultMatrial_list:
            if defaultMatrial in material_node:
                evaluation_bools.append(True)
        if True in evaluation_bools:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict
    
    def nonDefaultName_check_dict(self,node):
        defaultName_list=[
            "pSphere",
            "pCube",
            "pCylinder",
            "pCone",
            "pTorus",
            "pPlane",
            "pDisc",
            "locator",
            "joint",
            "camera",
            "curve",
            "nurbs",
            "Surface",
        ]
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node}
        for defaultName in defaultName_list:
            if defaultName in node:
                evaluation_bools.append(True)
        if True in evaluation_bools:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def nonDisplayLayer_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        displayLayer=cmds.listConnections(node,type="displayLayer")
        if displayLayer == None:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict

    def nonNameSpace_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if ':' in node:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else :
            evaluation_dict["bool"]=True
            return evaluation_dict

    def nonKeyedObject_check_dict(self,node):
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node,"attr":[]}
        keyables=cmds.listAttr(v=True,k=True)
        for keyable in keyables:
            checkKey=cmds.keyframe(node,query=True,at=keyable,timeChange=True)
            if checkKey == None:
                evaluation_bools.append(True)
            else :
                evaluation_bools.append(False)
                evaluation_dict["attr"].append(keyable)
        if False in evaluation_bools:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def pivotIsWorldTransform_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        centerPivot_list=cmds.xform(node,q=1,ws=1,rp=1)
        if centerPivot_list == [0,0,0]:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict
        
    def frozenTransform_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if cmds.nodeType(node) == "joint":
            rotation_tuple=cmds.getAttr(node+".rotate")[0]
            scale_tuple=cmds.getAttr(node+".scale")[0]
            #jointOrient_tuple=cmds.getAttr(node+".jointOrient")[0]
            if rotation_tuple == (0.0,0.0,0.0) and scale_tuple == (1.0,1.0,1.0):
                evaluation_dict["bool"]=True
                return evaluation_dict
            else :
                evaluation_dict["bool"]=False
                return evaluation_dict
        
        translation_list=cmds.xform(node,q=True,worldSpace=True,translation=True)
        rotation_list=cmds.xform(node,q=True,worldSpace=True,rotation=True)
        scale_list=cmds.xform(node,q=True,worldSpace=True,scale=True)
        if translation_list == [0.0,0.0,0.0] and rotation_list == [0.0,0.0,0.0] and scale_list == [1.0,1.0,1.0]:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict

    def showObject_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if cmds.getAttr(node+".visibility") == 1:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict
    
    def cleanHistory_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        shapes=cmds.listRelatives(node,shapes=True,type="mesh")
        historySize_int=len(cmds.listHistory(shapes))
        if historySize_int < 2:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict

    def nonConcave_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node,"concave":[]}
        concaves=mel.eval('polyCleanupArgList 4 { "0","2","1","0","1","1","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
        if concaves == []:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            for concave in concaves:
                evaluation_dict["concave"].append(concave)
            return evaluation_dict

    def limina_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node,"limina":[]}
        liminas=cmds.polyInfo(node,nmv=True,nme=True,nue=True,iv=True,ie=True,lf=True)
        if limina == None:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            for limina in liminas:
                evaluation_dict["limina"].append(limina)
            return evaluation_dict

    def ngon_check_dict(self,node):
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node,"ngon":[]}
        faces=cmds.filterExpand(cmds.polyListComponentConversion(node,tf=True),sm=34)
        for face in faces:
            vertexs=cmds.filterExpand(cmds.polyListComponentConversion(face,tv=True),sm=31)
            if len(vertexs) == 4:
                evaluation_bools.append(True)
            elif len(vertexs) == 3:
                evaluation_bools.append(True)
            else:
                evaluation_bools.append(False)
                evaluation_dict["ngon"].append(face)
        if False in evaluation_bools:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def unlockedNormal_check_dict(self,node):
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node,"lockNormal":[]}
        vertexs=cmds.filterExpand(cmds.polyListComponentConversion(node,tv=True),sm=31)
        for vertex in vertexs:
            locked=cmds.polyNormalPerVertex(vertex,q=True,al=True)[0]
            if locked == False:
                evaluation_bools.append(True)
            else:
                evaluation_bools.append(False)
                evaluation_dict["lockNormal"].append(vertex)
        if True in evaluation_bools:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def overlappingUV_check_dict(self,node):
        evaluation_bools=[]
        evaluation_dict={"bool":False,"node":node,"overlappingUV":[]}
        shape_list=cmds.listRelatives(node,shapes=True,fullPath=True)
        faces=cmds.ls(cmds.polyListComponentConversion(shape_list,tf=True),fl=True)
        overlappings=(cmds.polyUVOverlap(faces,oc=True))
        if overlappings is None:
            evaluation_dict["bool"]=True
            return evaluation_dict    
        else:
            evaluation_dict["bool"]=False
            for overlapping in overlappings:
                evaluation_dict["overlappingUV"].append(overlapping)
            return evaluation_dict  
            
    def noUV_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        try:
            uvMaps=cmds.filterExpand(cmds.polyListComponentConversion(node,tuv=True),sm=35)
            for uvMap in uvMaps:
                uvPos_list=cmds.polyEditUV(uvMap,q=True,v=True,u=True)
                for uvPos in uvPos_list:
                    if float(uvPos) < 0.0 or float(uvPos) > 0.0:
                        evaluation_dict["bool"]=True
                        return evaluation_dict
        except:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def noShapeInTheParents_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        parent_list=cmds.listRelatives(node,p=True)
        shape_list=cmds.listRelatives(parent_list,s=True,type="mesh")
        if shape_list is None:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else :
            evaluation_dict["bool"]=False
            return evaluation_dict

    #same multiple check
    def andSameRelation_check_dict(self,relation,same_list):
        evaluation_bools=[]
        evaluation_dict={"bool":False,"relation":relation,"sameList":same_list}
        for same in same_list:
            if same in relation:
                evaluation_bools.append(True)
        if True in evaluation_bools:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def andMatchRelation_check_dict(self,relation,same_list):
        evaluation_bools=[]
        evaluation_dict={"bool":False,"relation":relation,"sameList":same_list}
        for same in same_list:
            if re.match(same,relation):
                evaluation_bools.append(True)
        if True in evaluation_bools:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict
    