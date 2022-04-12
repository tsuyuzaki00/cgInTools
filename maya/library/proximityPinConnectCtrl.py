import mgear.rigbits as rb
import maya.cmds as cmds
import pymel.core as pm

class ProximityPinCtrl():
    def proximityPin_create_func(self,geo,ctrls):
        bind_shape,orig_shape = self.bindShape_check_bindMesh_origMesh(geo)
        proxPin_node = self.proximityPinSetting_create_node(geo)

        cmds.connectAttr(str(orig_shape)+".outMesh",str(proxPin_node)+".originalGeometry")
        cmds.connectAttr(str(bind_shape)+".worldMesh[0]",str(proxPin_node)+".deformedGeometry")

        matrix_index = 0
        for ctrl in ctrls:
            ctrl_npo = rb.addNPO(objs = pm.PyNode(ctrl))
            worldMatrix_node = self.multMatrixSetting_create_node(ctrl,"worldMatrix",geo+"WdMx")
            parentInverseMatrix_node = self.multMatrixSetting_create_node(ctrl,"parentInverseMatrix",geo+"PrIMx",set_index=1)

            cmds.connectAttr(str(worldMatrix_node)+".matrixSum",str(proxPin_node)+".inputMatrix["+str(matrix_index)+"]")
            cmds.connectAttr(str(proxPin_node)+".outputMatrix["+str(matrix_index)+"]",str(parentInverseMatrix_node)+".matrixIn[0]")
            cmds.connectAttr(str(parentInverseMatrix_node)+".matrixSum",str(ctrl_npo[0])+".offsetParentMatrix")

            matrix_index = matrix_index + 1

    def proximityPin_add(self,geo,ctrls):
        pass
        
            
    def bindShape_check_bindMesh_origMesh(self,geo):
        child_check = cmds.listRelatives(geo,c=True)
        if len(child_check) == 2:
            bind_shape = child_check[0]
            orig_shape = child_check[1]
            return bind_shape,orig_shape
        else:
            cmds.warning("Bind to the mesh.")
            
    def proximityPinSetting_create_node(self,node_name):
        proxPin_node = cmds.createNode("proximityPin", n=node_name+"_pxmp")
        cmds.setAttr(str(proxPin_node)+".coordMode", 1)# Uses UV for coordinate mode
        cmds.setAttr(str(proxPin_node)+".normalAxis", 0)# Uses X for Normal Axis
        cmds.setAttr(str(proxPin_node)+".tangentAxis", 1)# Uses Y for Tanget Axis
        cmds.setAttr(str(proxPin_node)+".offsetTranslation", 1)
        cmds.setAttr(str(proxPin_node)+".offsetOrientation", 1)
        return proxPin_node

    def multMatrixSetting_create_node(self,node,matrix_name,rename,set_index=0):
        multMatrix_node = cmds.createNode("multMatrix",n=rename+"_mtmx")
        get_matrix = cmds.getAttr(node+"."+matrix_name+"[0]")
        cmds.setAttr(multMatrix_node+".matrixIn["+str(set_index)+"]",get_matrix,type="matrix")
        return multMatrix_node

def main():
    _Pxmp = ProximityPinCtrl()
    _Pxmp.proximityPin_create_func("test_geo",["test1_ctrl","test2_ctrl"])