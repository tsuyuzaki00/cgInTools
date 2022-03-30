import maya.cmds as cmds

class MayaLayer():
    def add_layer(self,layer_name,connect_node):
        if cmds.objExists(layer_name):
            self.set_layer(layer_name,connect_node)
        else:
            create_layer = cmds.createDisplayLayer(e = True, n = layer_name)
            self.set_layer(create_layer,connect_node)

    def set_layer(self,layer_name,connect_node):
        cmds.connectAttr(layer_name+".drawInfo",connect_node+".drawOverride")
        cmds.setAttr(layer_name + ".displayType", 2)