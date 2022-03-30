import pymel.core as pm

class JointSetting():
    def createJoint():
        pass

    def addJoint(self, sel = '', name = 'name', trs = (0,0,0), rot = (0,0,0), pos = 'C', num = '00'):
        defName = '_'.join( [name, pos, num, 'space'] )
        jntName = defName.replace('space', 'jnt')
        space = pm.createNode('transform', n = defName)
        jnt = pm.joint(r = True, rad= 0.5, n = jntName)
        pm.parent(space, sel)
        pm.setAttr(space + '.translate', trs)
        pm.setAttr(space + '.rotate', rot)

    def jointLabelling(self, sel = '', side = 0, type = 0, other = ''):
        pm.setAttr(sel + '.side', side) # 0 = Center 1 = Left 2 = Right 3 = None
        pm.setAttr(sel + '.type' , type) # 18 = Other
        pm.setAttr(sel + '.otherType', other, type = 'string')