import maya.cmds as cmds

class TargetMove():
    def __init__(self):
        self.source = ""
        self.target = ""
        self.posNum = 4

    def setSource(self,variable):
        self.source=variable
        return self.source

    def setTarget(self,variable):
        self.target=variable
        return self.target

    def setPos(self,variable):
        if variable is 1 or variable is "up":
            self.posNum = 1
            return self.posNum
        elif variable is 2 or variable is "back":
            self.posNum = 2
            return self.posNum
        elif variable is 3 or variable is "left":
            self.posNum = 3
            return self.posNum
        elif variable is 4 or variable is "center":
            self.posNum = 4
            return self.posNum
        elif variable is 5 or variable is "right":
            self.posNum = 5
            return self.posNum
        elif variable is 6 or variable is "front":
            self.posNum = 6
            return self.posNum
        elif variable is 7 or variable is "down":
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
    