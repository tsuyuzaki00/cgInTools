import pymel.core as pm

def multiCountKey(interval = 10, keyNum = 4, grpKey = 1, sels = ''):
    pm.select(sels)
    num = keyNum * grpKey
    nowKey = pm.currentTime( query=True )
    for loopNum in range(num):
        pm.currentTime( nowKey )
        pm.setKeyframe()
        nowKey += interval

def countKey(interval = 10, keyNum = 4, grpKey = 1, sels = ''):
    for sel in sels:
        pm.select(sel)
        num = keyNum * grpKey
        nowKey = pm.currentTime( query=True )
        for loopNum in range(num):
            pm.currentTime( nowKey )
            pm.setKeyframe()
            nowKey += interval

def main():
    sels = pm.selected()
    multiCountKey(interval = 5, keyNum = 4, grpKey = 1, sels = sels)
    #countKey(interval = 5, keyNum = 4, grpKey = 1, sels = sels)
