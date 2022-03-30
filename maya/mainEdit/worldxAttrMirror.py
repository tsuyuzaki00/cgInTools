import pymel.core as pm

def main ():
    sels = pm.selected()
    for sel in sels:
        reverseName = sel.replace('_L','_R')
        trsX = pm.getAttr(sel + '.translateX')
        trsY = pm.getAttr(sel + '.translateY')
        trsZ = pm.getAttr(sel + '.translateZ')
        
        rotX = pm.getAttr(sel + '.rotateX')
        rotY = pm.getAttr(sel + '.rotateY')
        rotZ = pm.getAttr(sel + '.rotateZ')
        
        pm.setAttr(reverseName + '.translateX', trsX * 1)
        pm.setAttr(reverseName + '.translateY', trsY * 1)
        pm.setAttr(reverseName + '.translateZ', trsZ * 1)
        
        pm.setAttr(reverseName + '.rotateX', rotX * 1)
        pm.setAttr(reverseName + '.rotateY', rotY * 1)
        pm.setAttr(reverseName + '.rotateZ', rotZ * 1)
main()