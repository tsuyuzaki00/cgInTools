import pymel.core as pm

with pm.window( title='my tools', width=300 ):
    with pm.columnLayout( adjustableColumn=True ):
        
        pm.text( label='radio button' )
        rdoGrp = pm.radioButtonGrp( numberOfRadioButtons=3,label='x/y/z',labelArray3=['x', 'y', 'z'])
        pm.separator()
        
        pm.text(label='check box' )
        boxGrp = pm.checkBoxGrp( numberOfCheckBoxes=3, label='box proup', labelArray3=['X','Y','Z'] )
        pm.separator()
        
        pm.text(label='float field' )
        fField = pm.floatFieldGrp( numberOfFields=1, label='some value' )
        pm.separator()
        
        pm.text(label='slider' )
        sld = pm.floatSliderGrp( label='slider' )
        pm.separator()
        
        pm.text(label='text field' )
        txt = pm.textFieldGrp(label='text field', pht='please input text...', text='hogehoge' )
        pm.separator()
        
        pm.button( label='print' , c='prints()' )

def prints():
    print rdoGrp.getSelect()
    print boxGrp.getValueArray4()
    print fField.getValue()
    print sld.getValue()
    print txt.getText()