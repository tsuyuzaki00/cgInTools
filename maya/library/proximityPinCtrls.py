import maya.cmds as cmds
import mgear.rigbits as rb
import pymel.core as pm

class CProximityPin():
    def __init__(self,geo,ctrls):
        self.geo = geo
        self.ctrls = ctrls

    def run(self):
        bind_shape,orig_shape = self.bindShape_check_bindMesh_origMesh(self.geo)
        proxPin_node = self.proximityPin_create_node(self.geo)

        geoMeshConnects = [
            [str(orig_shape)+".outMesh",str(proxPin_node)+".originalGeometry"],
            [str(bind_shape)+".worldMesh[0]",str(proxPin_node)+".deformedGeometry"],
        ]
        self.connectAttr_for_func(geoMeshConnects)

        matrix_index = 0

        for ctrl in self.ctrls:
            ctrl_npo = rb.addNPO(objs = pm.PyNode(ctrl))
            worldMatrix_node = self.multMatrix_create_node(ctrl,"worldMatrix",self.geo+"WdMx"+str(matrix_index).zfill(2)+"_mtmx")
            parentInverseMatrix_node = cmds.createNode("multMatrix",n=self.geo+"PrIMx"+str(matrix_index).zfill(2)+"_mtmx")
            decomposeMatirix_node = cmds.createNode("decomposeMatrix",n=self.geo+str(matrix_index).zfill(2)+"_dcmx")

            matrixConnects = [
                [str(worldMatrix_node)+".matrixSum",str(proxPin_node)+".inputMatrix["+str(matrix_index)+"]"],
                [str(proxPin_node)+".outputMatrix["+str(matrix_index)+"]",str(parentInverseMatrix_node)+".matrixIn[0]"],
                [str(ctrl_npo[0])+".parentInverseMatrix[0]",str(parentInverseMatrix_node)+".matrixIn[1]"],
                [str(parentInverseMatrix_node)+".matrixSum",str(decomposeMatirix_node)+".inputMatrix"],
                [str(decomposeMatirix_node)+".outputTranslate",str(ctrl_npo[0])+".translate"],
                [str(decomposeMatirix_node)+".outputRotate",str(ctrl_npo[0])+".rotate"],
                [str(decomposeMatirix_node)+".outputShear",str(ctrl_npo[0])+".shear"],
            ]
            self.connectAttr_for_func(matrixConnects)
            matrix_index = matrix_index + 1

    def bindShape_check_bindMesh_origMesh(self,geo):
        child_check = cmds.listRelatives(geo,c=True)
        if len(child_check) == 2:
            bind_shape = child_check[0]
            orig_shape = child_check[1]
            return bind_shape,orig_shape
        else:
            cmds.error("Bind to the mesh.")
            return None
            
    def proximityPin_create_node(self,node_name):
        proxPin_node = cmds.createNode("proximityPin", n=node_name+"_pxmp")
        proxPinSetAttrs = [
            [str(proxPin_node)+".coordMode", 1], # Uses UV for coordinate mode
            [str(proxPin_node)+".normalAxis", 0], # Uses X for Normal Axis
            [str(proxPin_node)+".tangentAxis", 1], # Uses Y for Tanget Axis
            [str(proxPin_node)+".offsetTranslation", 1],
            [str(proxPin_node)+".offsetOrientation", 1],
        ]
        self.setAttr_for_func(proxPinSetAttrs)
        return proxPin_node

    def multMatrix_create_node(self,node,matrix_name,rename,set_index=0):
        multMatrix_node = cmds.createNode("multMatrix",n=rename)
        get_matrix = cmds.getAttr(node+"."+matrix_name+"[0]")
        cmds.setAttr(multMatrix_node+".matrixIn["+str(set_index)+"]",get_matrix,type="matrix")
        return multMatrix_node

    def connectAttr_for_func(self,twoConnects):
        for sourcs,target in twoConnects:
            cmds.connectAttr(sourcs,target)
    
    def setAttr_for_func(self,twoSetNode):
        for nodeAttr,value in twoSetNode:
            cmds.setAttr(nodeAttr,value)

def sample():
    twoConnects = [
        ["test00_geo",["test01_ctrl","test02_ctrl"]],
        ["test01_geo",["test11_ctrl","test12_ctrl"]],
        ["test02_geo",["test21_ctrl","test22_ctrl"]],
    ]
    for geo,ctrls in twoConnects:
        _CPxmp = CProximityPin(geo,ctrls)
        _CPxmp.run()
