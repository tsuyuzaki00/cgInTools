import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class SourceToTarget(sbLB.BasePair):
    def __init__(self):
        self._sourceNode=""
        self._targetNode=""
        self._posNum=4

    def setPos(self,variable):
        if variable is 1 or variable is "up":
            self._posNum = 1
            return self._posNum
        elif variable is 2 or variable is "back":
            self._posNum = 2
            return self._posNum
        elif variable is 3 or variable is "left":
            self._posNum = 3
            return self._posNum
        elif variable is 4 or variable is "center":
            self._posNum = 4
            return self._posNum
        elif variable is 5 or variable is "right":
            self._posNum = 5
            return self._posNum
        elif variable is 6 or variable is "front":
            self._posNum = 6
            return self._posNum
        elif variable is 7 or variable is "down":
            self._posNum = 7
            return self._posNum
    def getPos(self):
        return self._posNum

    def moveToTarget(self):
        self.moveToTarget_edit_func(self._sourceNode,self._targetNode,self._posNum)

    def moveToTarget_edit_func(self,source,target,positionID_int):
        source_vector=self.alignmentPos_quary_vector(source,positionID_int)
        cmds.move(source_vector[0],source_vector[1],source_vector[2],target,a=True)
    
    def alignmentPos_quary_vector(self,object,positionID_int):
        bbox=cmds.exactWorldBoundingBox(object,ignoreInvisible=False)
        if positionID_int == 1:
            up=[(bbox[0]+bbox[3])/2,bbox[4],(bbox[2]+bbox[5])/2]
            return up
        elif positionID_int == 2:
            back=[(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[2]]
            return back
        elif positionID_int == 3:
            left=[bbox[0],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return left
        elif positionID_int == 4:    
            center=[(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return center
        elif positionID_int == 5:
            right=[bbox[3],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return right
        elif positionID_int == 6:
            front=[(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[5]]
            return front
        elif positionID_int == 7:
            down=[(bbox[0]+bbox[3])/2,bbox[1],(bbox[2]+bbox[5])/2]
            return down
    