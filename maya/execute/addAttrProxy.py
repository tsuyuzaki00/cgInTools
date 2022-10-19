import maya.cmds as cmds

def proxy_connect_attr(source,target,attr_name):
    if(target == None or target == ''):
        return
    cmds.select(target)
    source_value = cmds.getAttr(source+"."+attr_name)
    source_type = cmds.getAttr(source+"."+attr_name,typ=True)
    cmds.addAttr(longName=attr_name,attributeType=source_type,defaultValue=source_value,k=False,proxy=source+"."+ attr_name)
    cmds.setAttr(target+"."+attr_name,cb=True)