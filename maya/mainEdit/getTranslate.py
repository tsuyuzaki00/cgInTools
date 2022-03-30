import pymel.core as pm

def getTranslateWolld():
    sel = pm.selected()
    getObj = sel[0].getTranslation('world')
    pm.setAttr(sel[1]+'.translate',getObj)
    
getTranslateWolld()