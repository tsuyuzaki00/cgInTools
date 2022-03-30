import maya.cmds as cmds

def oneAnimJsonExport(sel,attrs):
	margeAttr = []
	exportAnim = {}
	for attr in attrs:
		times = cmds.keyframe(sel,at=attr,query=True,timeChange=True)
		values = cmds.keyframe(sel,at=attr,query=True,valueChange=True)
        if not times == None or values == None:
            keys = create_list(times,values)
            oneAttr = {attr : keys}
            margeAttr.append(oneAttr)
            exportAnim[str(sel)] = margeAttr
        else:
            pass
	return exportAnim

def none_check(times,values):
    if not times == None or values == None:
        return times,values
    else:
        pass

def create_list(times,values):
	anim_list = []
	for (time,value) in zip(times,values):
		param_list = (time,value)
		anim_list.append(param_list)
	return anim_list

def get_key_date():
    sels = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    ctls = cmds.listRelatives(sels, p=True)
    for ctl in ctls:
        ex = oneAnimJsonExport(sel=str(ctl),attrs=["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"])
    return ex

def main():
    datas = get_key_date()
    print(datas)

main()