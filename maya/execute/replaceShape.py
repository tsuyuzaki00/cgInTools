

def replaceShape(source=None, targets=None, *args):
    """Replace the shape of one object by another.

    Args:
        source (None, PyNode): Source object with the original shape.
        targets (None, list of pyNode): Targets object to apply the
            source shape.
        *args: Maya's dummy

    Returns:

        None: Return non if nothing is selected or the source and targets
        are none

    """
    if not source and not targets:
        oSel = pm.selected()
        if len(oSel) < 2:
            pm.displayWarning("At less 2 objects must be selected")
            return None
        else:
            source = oSel[0]
            targets = oSel[1:]

    for target in targets:
        source2 = pm.duplicate(source)[0]
        shape = target.getShapes()
        cnx = []
        if shape:
            cnx = shape[0].listConnections(plugs=True, c=True)
            cnx = [[c[1], c[0].shortName()] for c in cnx]
            # Disconnect the conexion before delete the old shape
            for s in shape:
                for c in s.listConnections(plugs=True, c=True):
                    pm.disconnectAttr(c[0])
        pm.delete(shape)
        pm.parent(source2.getShapes(), target, r=True, s=True)

        for i, sh in enumerate(target.getShapes()):
            # Restore shapes connections
            for c in cnx:
                pm.connectAttr(c[0], sh.attr(c[1]))
            pm.rename(sh, target.name() + "_%s_Shape" % str(i))

        pm.delete(source2)