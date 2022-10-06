import maya.cmds as cmds

class TargetMove():
    def __init__(self):
        self.source = ""
        self.target = ""
        self.posNum = 4

    def setSource(self,obj):
        self.source=obj
        return self.source

    def setTarget(self,obj):
        self.target=obj
        return self.target

    def setPos(self,var):
        if var is "up" or 1:
            self.posNum = 1
            return self.posNum
        elif var is "back" or 2:
            self.posNum = 2
            return self.posNum
        elif var is "left" or 3:
            self.posNum = 3
            return self.posNum
        elif var is "center" or 4:
            self.posNum = 4
            return self.posNum
        elif var is "right" or 5:
            self.posNum = 5
            return self.posNum
        elif var is "front" or 6:
            self.posNum = 6
            return self.posNum
        elif var is "down" or 7:
            self.posNum = 7
            return self.posNum

    def run(self):
        self.movingObj_edit_func(self.source,self.target,self.posNum)

    def movingObj_edit_func(self,source_name,target_name,position_id):
        source_vector = self.alignmentPos_quary_vector(source_name,position_id)
        cmds.move(source_vector[0],source_vector[1],source_vector[2],target_name,a=True)
    
    def alignmentPos_quary_vector(self,target_name,position_id):
        #bbox = cmds.xform(source_name, query=True, boundingBox=True, ws=True)
        bbox = cmds.exactWorldBoundingBox(target_name,ignoreInvisible=False)
        if position_id == 1:
            up = [(bbox[0]+bbox[3])/2,bbox[4],(bbox[2]+bbox[5])/2]
            return up
        elif position_id == 2:
            back = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[2]]
            return back
        elif position_id == 3:
            left = [bbox[0],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return left
        elif position_id == 4:    
            center = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return center
        elif position_id == 5:
            right = [bbox[3],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
            return right
        elif position_id == 6:
            front = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[5]]
            return front
        elif position_id == 7:
            down = [(bbox[0]+bbox[3])/2,bbox[1],(bbox[2]+bbox[5])/2]
            return down
    