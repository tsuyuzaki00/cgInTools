import pymel.core as pm

with pm.window( title = 'Rename', ret = True):
    with pm.columnLayout( adjustableColumn = True ):
        pm.text( label = 'set Object' )
        pm.separator()
        partObject = pm.intFieldGrp( label='ObjectPart', numberOfFields = 1)
        pm.separator()
        part1 = pm.attrEnumOptionMenuGrp( l='part[0]', ei = [(0, 'NodeName'),(1, 'ObjectName'), (2, 'SceneName'),(3, 'Position')])
        pm.separator()
        part2 = pm.attrEnumOptionMenuGrp( l='part[1]', ei=[(0, 'ObjectName'),(1, 'NodeName'), (2, 'SceneName'),(3, 'Position')])
        pm.separator()
        part3 = pm.attrEnumOptionMenuGrp( l='part[2]', ei=[(0, 'SceneName'),(1, 'ObjectName'), (2, 'NodeName'),(3, 'Position'), (4, 'None')])
        pm.separator()
        part4 = pm.attrEnumOptionMenuGrp( l='part[3]', ei=[(0, 'None'),(1, 'Position'), (2, 'ObjectName'),(3, 'SceneName'), (4, 'NodeName')])
        pm.separator()
        pm.text( label = str(part1))
        pm.button( label = 'Rename', c = 'main( partObject.getValue())')
        
def main(objectPart):
    sels = pm.selected()
    for sel in sels:
        part = sel.split("_")
        set1 = part[objectPart[0]]
        set2 = part[1]
        set3 = part[2]
        set4 = part[3]
        
        pm.rename(sel, set1 + '_' + set2 + '_' + set3 + '_' + set4)