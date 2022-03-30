import pymel.core as pm

def selectConnect(connectGrp):
    print connectGrp
    if connectGrp == 1:
        connection = connectAttrs( exText.getText(), inText.getText())
    elif connectGrp == 2:
        connection = disConnectAttrs( exText.getText(), inText.getText())

def disConnectAttrs(exAttr, inAttr):
    exSel = pm.selected()[0]
    inSels = pm.selected()[1:]
    
    for inSel in inSels:
        pm.disconnectAttr(exSel + '.' + exAttr , inSel + '.' + inAttr )

def connectAttrs(exAttr, inAttr):
    exSel = pm.selected()[0]
    inSels = pm.selected()[1:]
    
    for inSel in inSels:
        pm.connectAttr(exSel + '.' + exAttr , inSel + '.' + inAttr )
    
with pm.window( title = 'connectAttrs', ret = True):
    with pm.columnLayout( adjustableColumn = True ):
        connectGrp = pm.radioButtonGrp( numberOfRadioButtons = 2, label = 'connection', labelArray2 = [ 'Connect', 'diCconnect' ])        
        pm.text( label = 'please attribute name' )
        exText = pm.textFieldGrp( label = 'exAttr')
        inText = pm.textFieldGrp( label = 'inAttr')
        pm.button( label = 'connection', c = 'selectConnect( connectGrp.getSelect() )')