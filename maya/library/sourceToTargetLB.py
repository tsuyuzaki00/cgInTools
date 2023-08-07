import maya.cmds as cmds
import cgInTools as cit

class SourceToTarget():
    def __init__(self):
        self._sourceNode=None
        self._targetNode=None
        self._corePosition_str=None
    
    #Single Function
    def corePosition_quary_vector3(self,node_str,corePosition_str):
        bbox=cmds.exactWorldBoundingBox(node_str,ignoreInvisible=False)
        if corePosition_str is "up":
            node_vector3=[(bbox[0]+bbox[3])/2,bbox[4],(bbox[2]+bbox[5])/2]
            return node_vector3
        elif corePosition_str is "back":
            node_vector3=[(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[2]]
            return node_vector3
        elif corePosition_str is "left":
            node_vector3=[bbox[0],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return node_vector3
        elif corePosition_str is "center":    
            node_vector3=[(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return node_vector3
        elif corePosition_str is "right":
            node_vector3=[bbox[3],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return node_vector3
        elif corePosition_str is "front":
            node_vector3=[(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[5]]
            return node_vector3
        elif corePosition_str is "down":
            node_vector3=[(bbox[0]+bbox[3])/2,bbox[1],(bbox[2]+bbox[5])/2]
            return node_vector3
    
    #Setting Function
    def setSourceNode(self,variable):
        self._sourceNode=variable
        return self._sourceNode
    def getSourceNode(self):
        return self._sourceNode
    
    def setTargetNode(self,variable):
        self._targetNode=variable
        return self._targetNode
    def getTargetNode(self):
        return self._targetNode
    
    def setCorePosition(self,variable):
        self._corePosition_str=variable
        return self._corePosition_str
    def getCorePosition(self):
        return self._corePosition_str    

    #Public Function
    def moveToTarget(self,sourceNode=None,targetNode=None,corePos=None):
        _sourceNode=sourceNode or self._sourceNode
        _targetNode=targetNode or self._targetNode
        _corePosition_str=corePos or self._corePosition_str or "center"

        targetPos_vector3=self.corePosition_quary_vector3(_targetNode,_corePosition_str)
        cmds.move(targetPos_vector3[0],targetPos_vector3[1],targetPos_vector3[2],_sourceNode,a=True)