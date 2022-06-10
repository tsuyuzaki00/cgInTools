import maya.cmds as cmds

class CTargetMove():
    def __init__(self,source,target,posNum):
        self.source = source
        self.target = target
        self.posNum = 1 or posNum

    def run(self):
        self.moving_obj(self.source,self.target,self.posNum)

    def moving_obj(self,source_name,target_name,position_id):
        target_pos = self.conpornent_pos(target_name,position_id)
        cmds.move(target_pos[0],target_pos[1],target_pos[2],source_name,a=True)
    
    def conpornent_pos(self,target_name,position_id):
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

def sample():
    dictMoves=[
        ["test00","test01",1]
    ]
    for source,target,posNum in dictMoves:
        _CTgmv = CTargetMove(source,target,posNum)
        _CTgmv.run()
    