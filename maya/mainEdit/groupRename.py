import pymel.core as pm

def connectFromChbox():
    ctl = pm.selected()[0]
    objs = pm.selected()[1:]
    chList = pm.channelBox( 'mainChannelBox' , q = True , selectedMainAttributes = True )

    if not chList:
        print 'please select channels in channel box...'
        return

    for obj in objs:
        for ch in chList:
            pm.connectAttr( ctl.name()+'.'+ch, obj.name()+'.'+ch,f=True )
