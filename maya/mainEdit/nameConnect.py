import pymel.core as pm

p =  pm.selected()
if len(p) >= 2:
    sel1 = pm.selected()[0]
    sel2 = pm.selected()[1]
else:
    sel1 = ''
    sel2 = ''
    
with pm.window( title='Node Connect', width=300 ):
    with pm.columnLayout( adjustableColumn=True ):
        
        pm.text( label='radio button' )
        rdoGrp = pm.radioButtonGrp( numberOfRadioButtons=2,label='sel/grp',labelArray2=['sel', 'grp'],sl=1)
        pm.separator()
        
        pm.text(label='check box' )
        boxGrp = pm.checkBoxGrp( numberOfCheckBoxes=3, label='connect', labelArray3=['Translate','Rotate','Scale'] )
        pm.separator()
        
        pm.text(label='OutNodeName' )
        connectOut = pm.textFieldGrp(label='connectOut', pht='please connectOut text...',text=sel1)
        pm.separator()
        
        pm.text(label='InNodeName' )
        connectIn = pm.textFieldGrp(label='connectIn', pht='please connectIn text...',text=sel2)
        pm.separator()
        
        pm.button( label='print' , c='main()' )

def main():
    boxTrans = boxGrp.getValue1()
    boxRotate = boxGrp.getValue2()
    boxScale = boxGrp.getValue3()
    outText = connectOut.getText()
    inText = connectIn.getText()
    if boxTrans == True:
        pm.connectAttr( outText+'.'+'translate', inText+'.'+'translate',f=True )
    if boxRotate == True:
        pm.connectAttr( outText+'.'+'rotate', inText+'.'+'rotate',f=True )
    if boxScale == True:
        pm.connectAttr( outText+'.'+'scale', inText+'.'+'scale',f=True )
        
        