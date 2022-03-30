import pymel.core as pm

sel = pm.selected()[0]

test = sel.nodeType()
print test