import pymel.core as pm

def addChild(child, attrName):
    sels = pm.selected()
    for sel in sels:
        createChild = pm.createNode('nurbsSurface', n = child)
        pm.addAttr(ln = attrName, nn = attrName.title(), at = 'float', dv = 1)
        pm.setAttr(createChild + '.' + attrName, k = True)
        pm.parent('surface1|' + child , sel , add = True, s = True)
        pm.delete('surface1')

with pm.window( title = 'add Child', ret = True):
    with pm.columnLayout( adjustableColumn = True ):
        pm.text( label = 'child Name' )
        txtNode = pm.textFieldGrp( label = 'nodeName')
        txtAttr = pm.textFieldGrp( label = 'attrName')        
        pm.button( label = 'createChild', c = 'addChild( txtNode.getText(), txtAttr.getText() )')