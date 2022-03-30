import maya.mel as mel
import maya.cmds as cmds

def grp_shape_connect(grp,search,replace):
    nCollider_grp = cmds.listRelatives(grp)
    check_collider = cmds.ls("*" + search)
    nCollider_sims = set(nCollider_grp) & set(check_collider)
    for nCollider_sim in list(nCollider_sims):
        nCollider_geo = nCollider_sim.replace(search,replace)
        nCollider_sim_shape = cmds.listRelatives(nCollider_sim, s = True)
        nCollider_geo_shape = cmds.listRelatives(nCollider_geo, s = True)
        try:
            cmds.connectAttr(nCollider_geo_shape[0] + ".outMesh", nCollider_sim_shape[0] + ".inMesh")
        except SyntaxError:
            pass
        except RuntimeError:
            pass

def alembic_maya_export(start,end,root,save_name):
    root = "-root |geo_grp -root |sim_grp|dfrm_grp"
    save_path = "D:/GMR/sim_for_test/cache/alembic/" + save_name + ".abc"
    mel.eval('AbcExport -j "-frameRange {0} {1} -uvWrite -writeFaceSets -worldSpace -writeUVSets -dataFormat ogawa {2} -file {3}"'.format(start,end,root,save_path))

def set_sim_anim(root_grp,deform_grp,geo_grp):
    cmds.parent(deform_grp, root_grp)
    cmds.parent(geo_grp, root_grp)
    cmds.setAttr("C_fullBody_geo" + ".visibility", 0)
    layer_name = "sim_layer"
    if cmds.objExists(layer_name):
        cmds.editDisplayLayerMembers(layer_name, root_grp, nr = True)
        cmds.setAttr(layer_name + ".displayType", 2)
    else:
        layer = cmds.createDisplayLayer(n = layer_name)
        cmds.editDisplayLayerMembers(layer, root_grp, nr = True)
        cmds.setAttr(layer + ".displayType", 2)
    deform_list = cmds.listRelatives(deform_grp)
    for deform in deform_list:
        geo = deform.replace("_dfrm","_geo")
        cmds.setAttr(geo + ".visibility", 0)

def main():
    #grp_shape_connect("collider_grp","_sim","_geo")
    #grp_shape_connect("input_grp","_inp","_geo")
    #alembic_maya_export("-50","550",["geo_grp","dfrm_grp"],"joe_cut_sim")
    set_sim_anim("root_grp","dfrm_grp","geo_grp")

main()