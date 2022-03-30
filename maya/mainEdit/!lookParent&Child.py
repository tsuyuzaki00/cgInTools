import pymel.core as pm
sels = pm.selected()

parent = pm.listRelatives(sels[0], p = True)
allParents = pm.listRelatives(sels[0], ap = True)
children = pm.listRelatives(sels[0], c = True)
allDescendents = pm.listRelatives(sels[0], ad = True)
noIntermediate = pm.listRelatives(sels[0], ni = True)

shows = [parent, allParents, children, noIntermediate, allDescendents]
for show in shows:
	print show