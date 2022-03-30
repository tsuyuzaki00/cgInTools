import pymel.core as pm

sel = pm.ls(sl = True, dag = True)

for name in sel:
    ex = pm.getAttr(name + '.jointOrient')
    pm.setAttr(name + '.jointOrient' , 0,0,0 ,type="double3")
    pm.setAttr(name + '.rotate' , ex ,type="double3")
    
#rotate -r -pcp -os -fo 0 0 180;
#makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;