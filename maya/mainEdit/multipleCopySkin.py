import pymel.core as pm

def oneCopySkin():
    cageSel = pm.selected()[0]
    geoSels = pm.selected()[1:]
    exSkin = pm.listHistory(cageSel, type = 'skinCluster')

    for geoSel in  geoSels:
        inSkin = pm.listHistory(geoSel, type = 'skinCluster')
        pm.copySkinWeights(ss = exSkin[0], ds = inSkin[0], nm = True, sa = 'closestPoint', ia = 'closestJoint')


def multiCopySkin():
    cageSels = pm.selected()

    for cageSel in  cageSels:
        exSkin = pm.listHistory(cageSel, type = 'skinCluster')
        geoSel = cageSel.replace("cage_",'geo_')
        inSkin = pm.listHistory(geoSel, type = 'skinCluster')
        pm.copySkinWeights(ss = exSkin[0], ds = inSkin[0], nm = True, sa = 'closestPoint', ia = 'closestJoint')
        
oneCopySkin()
multiCopySkin()