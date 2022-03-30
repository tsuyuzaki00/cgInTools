import pymel.core as pm

def main():
    sel = pm.selected()
    parentSel = pm.listRelatives(sel, parent=True)
    if sel != []:
        spaceName = sel[0].replace("jnt_",'space_')
        ctrlName = sel[0].replace("jnt_",'ctrl_')
        trsName = sel[0].replace("jnt_",'trs_')
        
        spaceNode = pm.createNode( 'transform', n=spaceName)
        trsNode = pm.createNode( 'transform', n=trsName)
        
        ctrlNode = pm.curve(p=[(0, 1.11, 0), (0, 0.78, -0.78), (0, 0, -1.11), (0, -0.78, -0.78), (0, -1.11, 0), (0, -0.78, 0.78), (0, 0, 1.11), (0, 0.78, 0.78), (0, 1.11, 0)] )
        pm.rename(ctrlNode ,ctrlName)
        
        pm.parent(trsNode,ctrlNode)
        pm.setAttr(trsNode+'.translate', 0, 0, 0, type="double3")
        pm.setAttr(trsNode+'.rotate', 0, 0, 0, type="double3")
        
        pm.parent(ctrlNode,spaceNode)
        pm.setAttr(ctrlNode+'.translate', 0, 0, 0, type="double3")
        pm.setAttr(ctrlNode+'.rotate', 0, 0, 0, type="double3")
        
        pm.parent(spaceName,sel[0])
        pm.setAttr(spaceNode+'.translate', 0, 0, 0, type="double3")
        pm.setAttr(spaceNode+'.rotate', 0, 0, 0, type="double3")
        
        name_ctrl_grp = (sel[0].split('_'))
        all = pm.ls()
        
        if 'grp_ctrl_'+name_ctrl_grp[2] not in all:
            pm.createNode( 'transform', n='grp_ctrl_'+ name_ctrl_grp[2])

        if parentSel == []:
            pm.parent(spaceNode, 'grp_ctrl_'+ name_ctrl_grp[2])
            pm.pointConstraint(trsNode,sel[0])
            pm.orientConstraint(trsNode,sel[0])
        else :
            offsetName = sel[0].replace("jnt_",'offset_')
            offsetNode = pm.createNode( 'transform', n=offsetName)
            pm.parent(offsetNode,parentSel[0])
            pm.setAttr(offsetNode+'.translate', 0, 0, 0, type="double3")
            pm.setAttr(offsetNode+'.rotate', 0, 0, 0, type="double3")
            
            pm.parent(offsetNode, 'grp_ctrl_'+ name_ctrl_grp[2])
            pm.parent(spaceNode,offsetNode)
            
            pm.pointConstraint(parentSel[0],offsetNode)
            pm.orientConstraint(parentSel[0],offsetNode)
            pm.pointConstraint(trsNode,sel[0])
            pm.orientConstraint(trsNode,sel[0])
            