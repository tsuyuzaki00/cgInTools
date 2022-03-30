import pymel.core as pm

def itemParent():
    exParent = pm.selected()[0]
    itemParents = pm.selected()[1:]
    for itemParent in itemParents:
        part = itemParent.split("_")
        patternName = '_' + part[1] + '_' + part[2]
        nullName = 'null' + patternName
        parentName = 'prc' + patternName
        
        cnd = pm.createNode('condition', n='cnd' + patternName)
        pm.setAttr(cnd + '.colorIfTrueR', 1)
        pm.setAttr(cnd + '.colorIfFalseR', 0)
        
        pm.parentConstraint(exParent, nullName, n = parentName, mo = True, w = 1)
        
        pm.select(itemParent)
        pm.addAttr(ln = 'parent', nn = 'Parent', at = 'enum', en = 'Local:World')
        pm.setAttr(itemParent + '.parent', k = True)
        
        pm.connectAttr(itemParent + ".parent", cnd + ".firstTerm")
        pm.connectAttr(cnd+".outColorR", parentName + "." + exParent + "W0")

itemParent()