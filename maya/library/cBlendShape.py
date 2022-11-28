# -*- coding: iso-8859-15 -*-
import json
import os

import maya.api.OpenMaya as om
import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel

#
def get_ref_node_from_namespace(ns):
    # namespace ha ":" tsuki
    node = cmds.ls(ns+'*')[0]
    ref_node = cmds.referenceQuery(node, referenceNode=True)
    return ref_node
    
def get_bounding_box_center(obj):
    bb = cmds.exactWorldBoundingBox(obj)
    center_x = (bb[0]+bb[1])/2.0
    center_y = (bb[2]+bb[3])/2.0
    center_z = (bb[4]+bb[5])/2.0
    
    return om.MVector([center_x,center_y,center_z])
    
def get_center_diff_of_two_objs(obj1,obj2):
    bbc1 = get_bounding_box_center(obj1)
    bbc2 = get_bounding_box_center(obj2)
    diff = bbc2 - bbc1
    
    return diff

def get_diff_of_two_vtx(vtx1,vtx2):
    pos1 = om.MVector(cmds.pointPosition(vtx1,w=True))
    pos2 = om.MVector(cmds.pointPosition(vtx2,w=True))
    
    return pos1-pos2

def get_poly_count_in_a_scene():
    top_grps = cmds.ls(assemblies=True)
    top_grps = [grp for grp in top_grps if cmds.listRelatives(grp,type='transform') or cmds.listRelatives(grp,type='mesh')]
    geos = set()
    for grp in top_grps:
        geos = geos | set(get_exact_type_obj_in_grp(grp, 'mesh',shape=False))


    for geo in geos:
        poly += cmds.polyEvaluate(geo,t=True)
    return poly


def check_is_visible_of_a_obj(obj):
    # print(obj)
    visibility = cmds.getAttr('{}.visibility'.format(obj))
    display_override = cmds.getAttr('{}.overrideEnabled'.format(obj))
    display_type = cmds.getAttr('{}.overrideDisplayType'.format(obj))
    hidden_in_override = (display_type == 1 or not cmds.getAttr('{}.overrideVisibility'.format(obj)))
    # print(visibility,display_override,hidden_in_override)

    is_visible = visibility and not (display_override and hidden_in_override)

    return is_visible

def check_is_visible_of_a_geo(geo):
    """_summary_

    Args:
        geo (str): transfrom node name of a geometry 

    Returns:
        _type_: _description_
    """
    is_visible_in_tx = check_is_visible_of_a_obj(geo)
    shape = cmds.listRelatives(geo,type='mesh')
    if shape:
        shape = shape[0]
        is_visible_in_shape = check_is_visible_of_a_obj(shape)
    # print(is_visible_in_shape)

    return is_visible_in_tx and is_visible_in_shape


def is_a_geo_actually_visible(geo):
    is_visible = check_is_visible_of_a_geo(geo)
    parent = cmds.listRelatives(geo,p=True)
    while parent:
        parent = parent[0]
        is_visible = is_visible and check_is_visible_of_a_obj(parent)
        parent = cmds.listRelatives(parent,p=True)
    
    return is_visible

def change_path_for_mel(path):
    path = str(path).replace('\\','/')
    return path

class MayaError(Exception):
    pass

#returns the closest vertex given a mesh and a position [x,y,z] in world space.
#Uses om.MfnMesh.getClosestPoint() returned face ID and iterates through face's vertices.
def getClosestVertex(mayaMesh,pos=[0,0,0]):
    mVector = om.MVector(pos)#using MVector type to represent position
    selectionList = om.MSelectionList()
    selectionList.add(mayaMesh)
    dPath= selectionList.getDagPath(0)
    mMesh=om.MFnMesh(dPath)
    ID = mMesh.getClosestPoint(om.MPoint(mVector),space=om.MSpace.kWorld)[1] #getting closest face ID
    list=cmds.ls( cmds.polyListComponentConversion (mayaMesh+'.f['+str(ID)+']',ff=True,tv=True),flatten=True)#face's vertices list
    #setting vertex [0] as the closest one
    d=mVector-om.MVector(cmds.xform(list[0],t=True,ws=True,q=True))
    smallestDist2=d.x*d.x+d.y*d.y+d.z*d.z #using distance squared to compare distance
    closest=list[0]
    #iterating from vertex [1]
    for i in range(1,len(list)) :
        d=mVector-om.MVector(cmds.xform(list[i],t=True,ws=True,q=True))
        d2=d.x*d.x+d.y*d.y+d.z*d.z
        if d2<smallestDist2:
            smallestDist2=d2
            closest=list[i]      
    return closest


def get_top_parent(obj):
    parent = get_parent(obj)
    top = parent
    while parent:
        top = parent
        parent = get_parent(parent)
    
    return top


def get_parent(obj):
    parent_list = cmds.listRelatives(obj,p=True,pa=True)
    parent = None
    if parent_list:
        parent = parent_list[0]
    
    return parent


def has_parent_of_this_name(obj,prt_name):
    parent = get_parent(obj)
    while parent:
        if prt_name in parent.split('|'):
            return True
        else:
            parent = get_parent(parent)
    return False
    
def has_name_overlap(obj):
    if len(cmds.ls(obj)) > 1:
        return True
    else:
        return False


def has_same_top(objs):
    check_set = set()
    for obj in objs:
        check_set.add(get_top_parent(obj))
    if len(objs)==len(check_set):
        return False
    else:
        return True

def change_PyNode_to_str(obj):
    if isinstance(obj,pm.PyNode):
        return obj._name
    elif isinstance(obj,str):
        return obj
    else:
        raise TypeError('{} is not PyNode or str'.format(obj))


def is_visible(obj):
    result = bool(cmds.getAttr('{}.visibility'.format(obj)))
    parent = get_parent(obj)

    while result and parent:
        result = bool(cmds.getAttr('{}.visibility'.format(parent)))
        parent = get_parent(parent)

    return result


def remove_overlap_from_parent(obj,prt_name):
    if has_name_overlap(obj):
        overlap = cmds.ls(obj)
        obj_bools = [{'obj':obj,'bool':has_parent_of_this_name(obj,prt_name)} for obj in overlap]
        objs_has_same_parent = [obj_with_bool for obj_with_bool in obj_bools if obj_with_bool['bool']]
        if len(objs_has_same_parent) >> 1:
            objs = [obj_bool['obj'] for obj_bool in objs_has_same_parent]
            raise MayaError('parent name overlapping.{}'.format(objs))
        elif len(objs_has_same_parent) == 0:
            raise MayaError('object {} has no parent named {}'.format(obj,prt_name))
        else:
            return objs_has_same_parent[0]['obj']
    else:
        return obj

def remove_overlaps_from_parent(tgt_list,prt_name):
    new_list = [remove_overlap_from_parent(obj,prt_name) for obj in tgt_list]
    return new_list

def remove_overlap_from_top(obj,top):
    if has_name_overlap(obj):
        overlap = cmds.ls(obj)
        if has_same_top(overlap):
            raise MayaError('top node ga onazi deha dousiyoumonai, koitsura kakunin sitene.{}'.format(overlap))
        else:
            for obj in overlap:
                obj_top = get_top_parent(obj)
                if obj_top == top:
                    return obj
    else:
        return obj

            
def remove_overlaps_from_top(tgt_list,top):
    new_list = [remove_overlap_from_top(obj,top) for obj in tgt_list]
    return new_list

def obj_exists(objs):
    for obj in objs:
       if not cmds.objExists(obj):
           return False
    
    return True

def check_two_DAG(obj1,obj2):
    pass

def align_objs_to_parent(parent,children):
    wpos = cmds.xform(parent,ws=1,q=1,t=1)
    wrot = cmds.xform(parent,ws=1,q=1,ro=1)
    for child in children:
        cmds.xform(child,ws=1,t=wpos)
        cmds.xform(child,ws=1,ro=wrot)


def get_bldshp_nodes_from_obj(obj):
    
    shapes = cmds.listRelatives(obj,s=True)
    bldshp_nodes = set()
    for shape in shapes:
        connections = cmds.listConnections(shape)
        if connections:
            connections = set(connections)
            for con in connections:
                if cmds.objectType(con,isType='objectSet'):
                    deformers = set(cmds.listConnections(con))
                    for deformer in deformers:
                        if cmds.objectType(deformer,isType='blendShape'):
                            bldshp_nodes.add(deformer)
    return list(bldshp_nodes)


def get_all_tgt_names_from_bldshp(bs_node):
    
    # Probably correct, but it assumes that a blendshape target always has an alias.
    alias_list = cmds.aliasAttr(bs_node,q=True)
    tgt_names = [tgt for i,tgt in enumerate(alias_list) if i%2==0]
    return tgt_names

def create_new_tgt_to_bldshp(bldshp_node,base,tgt,index=0):
    cmds.blendShape(bldshp_node,e=True,t=(base,index,tgt,1.0))

def get_max_bs_tgt_index(bldshp_node):

    # I can't come up with good idea to get max tgt index of bs_node
    # so I treat it as the same number as that of weight count
    weight_count = cmds.blendShape(bldshp_node,q=True,wc=True)
    
    return weight_count


def set_bldshp_tgt_name(bs_node,tgt_index,new_name):
    mel_cmd = 'blendShapeRenameTargetAlias "{}" "{}" "{}";'.format(bs_node,tgt_index,new_name)
    mel.eval(mel_cmd)


def connect_bldshp(base,tgt,weight=1.0,foc=True,bs_name = None,tgt_name=None):
    bs_nodes = get_bldshp_nodes_from_obj(base)
    actual_bs_name = bs_name or 'blendShape'
    actual_tgt_name = tgt_name or tgt
    tgt_index = 0
    
    if not bs_nodes:
        # cmds.blendShape returns list like ['blendShape1'] so take index 0
        bs_node = cmds.blendShape(tgt,base,weight=(0,weight),foc=foc,n=actual_bs_name)[0]
        if tgt_name:
            tgt_index = 0 # when creating new blendshape, new target index is already 0
            set_bldshp_tgt_name(bs_node,tgt_index,tgt_name) 
    
    else:
        if bs_name:
            cmds.warning('base geo already has a blendshape, new target is connected to the one. blendshape name was ignored')
        if len(bs_nodes) > 1:
            raise MayaError('two or more blendshape node are connected')
        else:
            bs_node = bs_nodes[0]
            tgt_index = get_max_bs_tgt_index(bs_node)+1
            cmds.blendShape(bs_node,e=True,t=(base,tgt_index,tgt,1.0),w=(tgt_index,weight))
            if tgt_name:
                set_bldshp_tgt_name(bs_node,tgt_index,tgt_name)
    return {'bs_node':bs_node,'tgt_name':actual_tgt_name,'tgt_index':tgt_index}    

def get_attr_from_alias(node,alias):
    alias_list = cmds.aliasAttr(node,q=True)

    if alias in alias_list:
        actual_attr_index = alias_list.index(alias)+1
        actual_attr = alias_list[actual_attr_index]   
        return actual_attr
    else:
        raise NameError('{} is not used in {}'.format(alias,node))

def get_bldshp_tgt_index_from_tgt_name(bs_node,tgt_name):
    attr = get_attr_from_alias(bs_node,tgt_name)
    
    # returns "weight[index]"
    index = int(attr.replace('weight','')[1:-1])
    return index


def copy_bldshp_weight(src_geo,src_bsp,src_tgt,tgt_geo,tgt_bsp,tgt_tgt):
    src_vtx_count = cmds.polyEvaluate(src_geo,v=True)
    tgt_vtx_count = cmds.polyEvaluate(tgt_geo,v=True)
    
    if not src_vtx_count == tgt_vtx_count:
        cmds.warning('{} and {} have different topology'.format(src_bsp,tgt_geo))
    else:
        # catch the error basically from get_attr_from_alias in get_bldshp_tgt_index_from_tgt_name 
        try:
            src_tgt_index = get_bldshp_tgt_index_from_tgt_name(src_bsp,src_tgt)
            weight_list = cmds.getAttr(
                    '{}.inputTarget[0]'.format(src_bsp)
                    +'.inputTargetGroup[{}]'.format(src_tgt_index)
                    +'.targetWeights[0:{}]'.format(src_vtx_count-1)
                    )
            tgt_tgt_index = get_bldshp_tgt_index_from_tgt_name(tgt_bsp,tgt_tgt)
            cmds.setAttr(
                    '{}.inputTarget[0]'.format(tgt_bsp)
                    +'.inputTargetGroup[{}]'.format(tgt_tgt_index)
                    +'.targetWeights[0:{}]'.format(tgt_vtx_count-1)
                    ,*weight_list)
        except NameError as e:
            print(e)
    

# create dictorynary including weights of tgts per geometry
def export_bldshp_weights_as_dict(base_geo,bs_node,tgt_names):
    result_dict = {}
    result_dict['name'] = base_geo
    result_dict['bs_node'] = bs_node

    vtx_count = cmds.polyEvaluate(base_geo,v=True)
    result_dict['vtx_count'] = vtx_count

    result_dict['tgts'] = []
    for tgt_name in tgt_names:
        
        # sometimes we want to use tgt list without cheking if tgt_name actually exists
        # so we have to check tgt actully exists
        if cmds.objExists('{}.{}'.format(bs_node,tgt_name)):
            tgt_index = get_bldshp_tgt_index_from_tgt_name(bs_node,tgt_name)
            weight_list = cmds.getAttr(
                '{}.inputTarget[0]'.format(bs_node)
                +'.inputTargetGroup[{}]'.format(tgt_index)
                +'.targetWeights[0:{}]'.format(vtx_count-1)
                )

            result_dict['tgts'].append({'name':tgt_name,'weights':weight_list})
    """result_dict = {'name':base_geo,

                    'tgts':[{
                        'name':tgt_name,
                        'weights':weight_list
                    },...],

                    'vtx_count':vtx_count}
    """

    return result_dict


def export_bldshp_weights_as_json(geo_and_tgts_list,path):
    # geo_and_tgts_list : [(geo1,[tgt1,tgt2,...]),(geo2,[tgt1,tgt2,...]),....]
    # ignoring the case that the same geometry has more than one blendshape.
    weight_info = []
    for geo_and_tgts in geo_and_tgts_list:
        base_geo = geo_and_tgts[0]
        tgt_names = geo_and_tgts[1]
        bs_nodes = get_bldshp_nodes_from_obj(base_geo)
        if len(bs_nodes) == 1:
            bs_node = bs_nodes[0]
        else:
            raise ValueError('there is no object or are multiple bs node')
        weight = export_bldshp_weights_as_dict(base_geo,bs_node,tgt_names)
        weight_info.append(weight)
    
    with open(path,'w') as f:
        json.dump(weight_info,f,indent=4)

def export_bldshp_weight_from_objs(objs,path,tgt_to_omit=None):
    geo_and_tgts_list = generate_geo_and_tgts_list(objs,tgt_to_omit=tgt_to_omit)
    export_bldshp_weights_as_json(geo_and_tgts_list,path)
    

def generate_geo_and_tgts_list(objs,tgt_to_omit=None):
    geo_and_tgts_list = []
    tgt_to_omit = tgt_to_omit or []
    for obj in objs:
            bs_nodes = get_bldshp_nodes_from_obj(obj)
            if bs_nodes:
                bs_node = bs_nodes[0]
                all_tgts = get_all_tgt_names_from_bldshp(bs_node)
                tgts = [tgt for tgt in all_tgts if tgt not in tgt_to_omit ]
                geo_and_tgts_list.append((obj,tgts))
            else:
                print('{} has no blendshape'.format(obj))
    return geo_and_tgts_list

# this function works on "one" object 
def _import_bldshp_weight_from_dict(tgt_geo,tgt_bs,tgt_tgt,src_tgt,weight_dict):
    """[summary]

    Args:
        tgt_geo ([type]): [description]
        tgt_bs ([type]): [description]
        tgt_tgt ([type]): [description]
        src_tgt ([type]): [description]
        weight_dict (dict): a dict which defines the target weight
                            {'name':geo_name,'tgts':[{'name':tgt_name,'weights':[...]}]}

    Raises:
        MayaError: [description]
        MayaError: [description]
        MayaError: [description]
    """
    tgt_vtx_count = cmds.polyEvaluate(tgt_geo,v=True)
    src_vtx_count = weight_dict['vtx_count']
    if not tgt_vtx_count == src_vtx_count:
        raise MayaError('sorce geometry and target geometry have different topologies')
    else:
        tgt_list = [tgt for tgt in weight_dict['tgts'] if tgt['name'] == src_tgt]

        if not len(tgt_list):
            raise MayaError('target named {} does not exist in dictionary'.format(tgt_tgt))
        elif len(tgt_list) > 1:
            raise MayaError('there are two or more weight info named {} in dictionary'.format(tgt_tgt))
        else:
            weghit_list = tgt_list[0]['weights']
            tgt_tgt_index = get_bldshp_tgt_index_from_tgt_name(tgt_bs,tgt_tgt)

            cmds.setAttr(
                '{}.inputTarget[0]'.format(tgt_bs)
                +'.inputTargetGroup[{}]'.format(tgt_tgt_index)
                +'.targetWeights[0:{}]'.format(tgt_vtx_count-1),
                *weghit_list)

def import_bldshp_weights_from_dict(tgt_geo,tgt_bs,tgt_src_list,weight_dict):
    # tgt_src_list = [(tgt_tgt1,src_tgt1),(tgt_tgt2,src_tgt2),...]
    # the list above defines which src_target weight is transferred to which tgt_tgt weight  
    for tgt_src in tgt_src_list:
        tgt_tgt = tgt_src[0]
        src_tgt = tgt_src[1]
        _import_bldshp_weight_from_dict(tgt_geo,tgt_bs,tgt_tgt,src_tgt,weight_dict)

def import_bldshp_weight_from_json(tgt_src_tgts,path):
    """[summary]

    Args:
        tgt_src_tgts (list): [(tgt_geo1,src_geo1,[(tgt_tgt1,src_tgt1),(tgt_tgt2,src_tgt2),
                            (tgt_geo2,src_geo2,[(tgt_tgt1,src_tgt1),(tgt_tgt2,src_tgt2)...]),.....]
        path (str): json file path
    """
    with open(path,'r') as f:
        weight_info = json.load(f)
    
    for info in tgt_src_tgts:
        tgt_geo = info[0]
        src_geo = info[1]
        tgt_src_list = info[2]
        
        weight_dicts = [weight for weight in weight_info if weight['name']==src_geo]
        
        if not len(weight_dicts) == 1:
            raise MayaError('there is no, or are multiple info about {} in dictionary'.format(src_geo))
        
        else:
            weight_dict = weight_dicts[0]
            tgt_bs = get_bldshp_nodes_from_obj(tgt_geo)[0] #it assumes that the tgt_geo has only one blendshape node.
            
            
            import_bldshp_weights_from_dict(tgt_geo,tgt_bs,tgt_src_list,weight_dict)

def import_same_bldshp_weight_from_json(path):
    
    with open(path,'r') as f:
        weight_info = json.load(f)
    
    for weight_dict in weight_info:
        src_geo = weight_dict['name']
        tgt_geo = weight_dict['name']
        if cmds.objExists(tgt_geo) and cmds.objExists(src_geo):
            try:
                tgt_bs = get_bldshp_nodes_from_obj(tgt_geo)[0]
                tgts = [tgt_info['name'] for tgt_info in weight_dict['tgts']]

                for tgt in tgts:
                    src_tgt = tgt
                    tgt_tgt = tgt
                    try:
                        _import_bldshp_weight_from_dict(tgt_geo,tgt_bs,tgt_tgt,src_tgt,weight_dict)
                    except NameError as e:
                        print(e)
            except IndexError as e:
                print('{} does not have blendshape'.format(tgt_geo))
        else:
            error_objs = [obj for obj in (tgt_geo,src_geo) if not cmds.objExists(obj)]
            print('{} does not exists'.format(error_objs))

def get_exact_type_obj_in_grp(grp,node_type,shape=True):
    
    nodes = cmds.listRelatives(grp,ad=True,type=node_type,pa=True)
    
    if nodes and cmds.objectType(nodes[0],isa='shape') and not shape:
        # cmds.listRelatives can take list as argment so we can get all parent of the list like below
        nodes = list({geo for geo in cmds.listRelatives(nodes,p=True,pa=True)})
    
    return nodes


def get_all_top_nodes():
    return cmds.ls(assemblies=True)


def get_namespace_from_ref_node(ref):
    try:
        return cmds.referenceQuery(ref,namespace=True)
    except RuntimeError:
        cmds.file(lr=ref)
        return cmds.referenceQuery(ref,namespace=True)


def get_top_nodes_of_the_namespace(ns):
    return cmds.ls('{}:*'.format(ns),assemblies=True)


def get_all_ref_node():
    return cmds.ls(type='reference')


def replace_references(refs,folder_format,file_format):
    for ref in refs:
        file = cmds.referenceQuery(ref,f=True)
        new_folder = folder_format(file)
        new_basename = file_format(file)
        new_file = os.path.join(new_folder,new_basename)
        if os.path.exists(new_file):
            cmds.file(os.path.join(new_folder,new_basename), loadReference=ref)
        else:
            print('{} does not exists'.format(new_file))
            
def make_overscan_camera(camera):
    os_cam = cmds.duplicate(camera,n='OS_{}'.format(camera))[0]
    mult_node = cmds.createNode('multiplyDivide',n=('cam_OS_mult'))
    cmds.setAttr('{}.operation'.format(mult_node),2)
    cmds.setAttr('{}.input2X'.format(mult_node),1.1)
    
    
    cam_shape = cmds.listRelatives(camera,s=True)[0]

    cam_shape = cmds.listRelatives(camera,s=True)[0]
    os_cam_shape = cmds.listRelatives(os_cam,s=True)[0]


    # constraint leads to trouble when set camera renderable,so use connection
    cmds.connectAttr('{}.translate'.format(camera),'{}.translate'.format(os_cam))
    cmds.connectAttr('{}.rotate'.format(camera),'{}.rotate'.format(os_cam))

    for shape_attr in CAM_SHAPE_ATTR:
        if not shape_attr == 'postScale':
            cmds.setAttr('{}.{}'.format(os_cam_shape,shape_attr),k=True,l=False)
            cmds.connectAttr('{}.{}'.format(cam_shape,shape_attr),'{}.{}'.format(os_cam_shape,shape_attr))
        else:
            cmds.setAttr('{}.{}'.format(os_cam_shape,shape_attr),k=True,l=False)
            cmds.connectAttr('{}.{}'.format(cam_shape,shape_attr),'{}.input1X'.format(mult_node))
            cmds.connectAttr('{}.outputX'.format(mult_node),'{}.{}'.format(os_cam_shape,shape_attr))

EXP_DATA = [
        {"name":"A","code":"aa","parts":["mouth"]},
        {"name":"I","code":"ii","parts":["mouth"]},
        {"name":"U","code":"uu","parts":["mouth"]},
        {"name":"E","code":"ee","parts":["mouth"]},
        {"name":"O","code":"oo","parts":["mouth"]},
        {"name":"BlinkA","code":"blinkA","parts":["eyes","mouth"]},
        {"name":"BlinkS","code":"blinkS","parts":["eyes","mouth"]},
        {"name":"Smile","code":"smile","parts":["eyes","mouth"]},
        {"name":"Wow","code":"wow","parts":["eyes","mouth"]},
        {"name":"Boke","code":"boke","parts":["eyes","mouth"]},
        {"name":"Angry","code":"angry","parts":["eyes","mouth"]},
        {"name":"Blink","code":"blink","parts":["eyes","mouth"]},
        {"name":"Con","code":"con","parts":["eyes","mouth"]},
        {"name":"Shy","code":"shy","parts":["eyes","mouth"]},
        {"name":"Huh","code":"huh","parts":["eyes","mouth"]},
        {"name":"Laugh","code":"laugh","parts":["eyes","mouth"]},
        {"name":"Clench","code":"clench","parts":["eyes","mouth"]},
        {"name":"LaughF","code":"laughF","parts":["eyes","mouth"]},
        {"name":"Serious","code":"serious","parts":["eyes","mouth"]}
        
        ]

PIN_INFO = [
        {
            "tgt_geo": "C_Head_Geo",
            "objs_to_add_pin": [
                "eye_L_inCorner_ctl_npo",
                "eye_L_outCorner_ctl_npo",
                "eye_L_lowMid_ctl_npo",
                "eye_L_upMid_ctl_npo",
                "eye_L_upInMid_ctl_npo",
                "eye_L_lowInMid_ctl_npo",
                "eye_L_upOutMid_ctl_npo",
                "eye_L_lowOutMid_ctl_npo",
                "eye_outCorInt_L0_ctl_npo",
                "eye_upInInt_L0_ctl_npo",
                "eye_upOutInt_L0_ctl_npo",
                "eye_inCorInt_L0_ctl_npo",
                "eye_lowInInt_L0_ctl_npo",
                "eye_lowMidInt1_L0_ctl_npo",
                "eye_lowMidInt2_L0_ctl_npo",
                "eye_lowOutInt_L0_ctl_npo",
                "eye_R_inCorner_ctl_npo",
                "eye_R_outCorner_ctl_npo",
                "eye_R_lowMid_ctl_npo",
                "eye_R_upMid_ctl_npo",
                "eye_R_upInMid_ctl_npo",
                "eye_R_lowInMid_ctl_npo",
                "eye_R_upOutMid_ctl_npo",
                "eye_R_lowOutMid_ctl_npo",
                "eye_outCorInt_R0_ctl_npo",
                "eye_upInInt_R0_ctl_npo",
                "eye_upOutInt_R0_ctl_npo",
                "eye_inCorInt_R0_ctl_npo",
                "eye_lowInInt_R0_ctl_npo",
                "eye_lowMidInt1_R0_ctl_npo",
                "eye_lowMidInt2_R0_ctl_npo",
                "eye_lowOutInt_R0_ctl_npo",
                "lips_C_upper_ctl_npo",
                "lipsUp_C0_ctl_npo",
                "lips_L_upInner_ctl_npo",
                "lips_L_upOuter_ctl_npo",
                "lips_R_upInner_ctl_npo",
                "lips_R_upOuter_ctl_npo",
                "lips_C_lower_ctl_npo",
                "lipsDown_C0_ctl_npo",
                "lips_L_lowInner_ctl_npo",
                "lips_L_lowOuter_ctl_npo",
                "lips_R_lowInner_ctl_npo",
                "lips_R_lowOuter_ctl_npo"
            ]
        },
        {
            "tgt_geo": "C_Tp_Teeth_Geo",
            "objs_to_add_pin": [
                "mouth_C0_teethup_ctl_npo"
            ]
        },
        {
            "tgt_geo": "C_Bt_Teeth_Geo",
            "objs_to_add_pin": [
                "mouth_C0_teethlow_ctl_npo"
            ]
        },
        {
            "tgt_geo": "C_Tongue_Geo",
            "objs_to_add_pin": [
                "tongue_C0_fk3_ctl_npo",
                "tongue_C0_fk2_ctl_npo",
                "tongue_C0_fk1_ctl_npo",
                "tongue_C0_fk0_ctl_npo"
            ]
        },
                {
            "tgt_geo": "C_Eyebrows_Geo",
            "objs_to_add_pin": [
                "eyebrow_L_sec_00_ctl_npo",
                "eyebrow_L_sec_01_ctl_npo",
                "eyebrow_L_sec_02_ctl_npo",
                "eyebrow_L_sec_03_ctl_npo",
                "eyebrow_L_sec_04_ctl_npo",
                "eyebrow_L_sec_05_ctl_npo", 
                "eyebrow_L_sec_06_ctl_npo",
                "eyebrow_L_sec_07_ctl_npo",
                "eyebrow_L_sec_08_ctl_npo",
                "eyebrow_L_sec_09_ctl_npo",
                "eyebrow_R_sec_00_ctl_npo",
                "eyebrow_R_sec_01_ctl_npo",
                "eyebrow_R_sec_02_ctl_npo",
                "eyebrow_R_sec_03_ctl_npo",
                "eyebrow_R_sec_04_ctl_npo",
                "eyebrow_R_sec_05_ctl_npo",
                "eyebrow_R_sec_06_ctl_npo",
                "eyebrow_R_sec_07_ctl_npo",
                "eyebrow_R_sec_08_ctl_npo",
                "eyebrow_R_sec_09_ctl_npo"
            ]
        }
    ]

def connect_facial_exps(bsp_path,rig_geos,exp_data=EXP_DATA):
    cmds.file(bsp_path,i=True)
    exp_grps = cmds.listRelatives('Bsp_Grp')
    hook = cmds.group(n='Hook_Grp',em=True)
    cmds.setAttr('{}.visibility'.format(hook),0)
    
    
    dummys = create_proximity_pins(hook)
    dummy_grp = cmds.group(dummys,n='dummy_Grp',w=True)
    cmds.setAttr('{}.visibility'.format(dummy_grp),0)
    
    for dummy in dummys:
        cmds.skinCluster('neck_C0_head_jnt',dummy,tsb=True)
    
    for exp_grp in exp_grps:
        # we named geometry "geoName_expName" like "C_Head_Geo_smile"
        exp_code = exp_grp.split('_')[-1] 
        exp_dicts = [exp_dict for exp_dict in exp_data if exp_dict['code']==exp_code]
        if len(exp_dicts) == 1:
            exp_dict = exp_dicts[0]
        else:
            raise ValueError('there is no info or are multiple info about {} \n'.format(exp_code)
                                +'dicts is this {}'.format(exp_dicts))
        
        exp_name = exp_dict['name']
        facial_parts = generate_facial_part_names_from_dict(exp_dict)
        
        geos = ema.get_exact_type_obj_in_grp(exp_grp,'mesh',shape=False)
        
        for geo in geos:
            base_geo = '_'.join(geo.split('_')[0:-1])
            for part in facial_parts:
                if base_geo in rig_geos:
                    tgt_name = part+exp_name
                    bs_info_of_facial_exp_step = ema.connect_bldshp(base_geo,geo,weight=0,tgt_name=tgt_name)
                    hooks_attr = '{}.{}'.format(hook,tgt_name)
                    if not cmds.objExists(hooks_attr):
                        cmds.addAttr(hook,longName = tgt_name, attributeType="float", defaultValue=0, h=0, k=1, min=0, max=1)
                    dummy_tgt_attr =   '{}.{}'.format(bs_info_of_facial_exp_step['bs_node'],tgt_name)
                    
                    cmds.connectAttr(hooks_attr,dummy_tgt_attr)
                else:
                    cmds.warning('nanka error detorude {}'.format(base_geo))

                if base_geo+'_dummy' in dummys:
                    bs_info_of_dummy = ema.connect_bldshp(base_geo+'_dummy',geo,weight=0,tgt_name=tgt_name)
                    dummy_tgt_attr =   '{}.{}'.format(bs_info_of_dummy['bs_node'],tgt_name)
                    
                    cmds.connectAttr(hooks_attr,dummy_tgt_attr)
                else:
                    cmds.warning('dummy niha iranyatu {}'.format(base_geo))


    cmds.delete('Bsp_Grp')
def generate_facial_part_names_from_dict(exp_dict):
     
    facial_parts = []
    
    for parts in exp_dict['parts']:
        if 'mouth' in parts:
            facial_parts.append('mouth')
        if 'eyes' in parts:
            facial_parts.extend(['eyeL','eyeR','eyebrowL','eyebrowR'])
    
    return facial_parts

def generate_tgt_names_from_exp_dict(exp_dict):
    facial_farts = generate_facial_part_names_from_dict(exp_dict)
    tgt_names = [part+exp_dict['name'] for part in facial_farts]
    return tgt_names
      
    

def _copy_bldshp_weight_to_all_other_tgts(src_exp_name,geo,exp_data=EXP_DATA):

    tgt_exp_data = [exp_dict for exp_dict in exp_data if exp_dict['name'] != src_exp_name]
    src_exp_data = [exp_dict for exp_dict in exp_data if exp_dict['name'] == src_exp_name]
    src_exp_dict = src_exp_data[0]
    
    for exp_dict in tgt_exp_data:
        facial_parts = generate_facial_part_names_from_dict(exp_dict)
        for part in facial_parts:
            src_tgt = part+src_exp_name
            tgt_tgt = part+exp_dict['name']
            bsp = ema.get_bldshp_nodes_from_obj(geo)[0]
            ema.copy_bldshp_weight(geo,bsp,src_tgt,geo,bsp,tgt_tgt)

def copy_bldshp_weight_from_this_to_the_others(src_exp_name):
    geos = cmds.ls(sl=True)
    for geo in geos:
        _copy_bldshp_weight_to_all_other_tgts(src_exp_name,geo,exp_data=EXP_DATA)

def import_and_connect_bldshp(path):
    rig_geos = ema.get_exact_type_obj_in_grp('Geo_Grp','mesh',shape=False)
    connect_facial_exps(path,rig_geos)
    connect_ctl_to_hooks('faceUI_C0_ctl','Hook_Grp')

def create_proximity_pins(parent,proximity_pins=PIN_INFO):
    dummy_geos = []
    for pin_info in proximity_pins:

        tgt_geo = pin_info['tgt_geo']
        geometry = cmds.duplicate(tgt_geo,n=tgt_geo+'_dummy')[0]
        dummy_geos.append(geometry)
        
        prx_pin = cmds.createNode("proximityPin", n=geometry+"_pxp")
        cmds.setAttr(prx_pin+".coordMode", 1)
        cmds.setAttr(prx_pin+".normalAxis", 0)
        cmds.setAttr(prx_pin+".tangentAxis", 1)
        cmds.setAttr(prx_pin+".offsetTranslation", 1)
        cmds.setAttr(prx_pin+".offsetOrientation", 1)
        cmds.connectAttr("{}ShapeOrig.outMesh".format(geometry),"{}.originalGeometry".format(prx_pin))
        cmds.connectAttr("{}Shape.worldMesh[0]".format(geometry),"{}.deformedGeometry".format(prx_pin))
        
        objs_to_add_pin = pin_info["objs_to_add_pin"]
        index = 0
        for npo in objs_to_add_pin:
            
            if cmds.objExists(npo):            
                loc_as_pin = cmds.spaceLocator(n=npo+"_pip")[0]
                npo_actual_name = ema.remove_overlap_from_parent(npo,'world_ctl')
                
                world_scale = cmds.xform(npo_actual_name,ws=1,q=1,s=1)
                cmds.xform(loc_as_pin,ws=1,s=world_scale)
                ema.align_objs_to_parent(npo_actual_name,[loc_as_pin])
                cmds.parent(loc_as_pin, parent)
                


                cmds.setAttr(str(npo_actual_name)+".inheritsTransform", 0)
                cmds.setAttr(str(npo_actual_name)+".t",0,0,0)
                cmds.setAttr(str(npo_actual_name)+".r",0,0,0)
                cmds.setAttr(str(npo_actual_name)+".s",1,1,1)


                cmds.connectAttr(str(loc_as_pin)+".matrix",prx_pin+".inputMatrix["+str(index)+"]")
                cmds.connectAttr(prx_pin+".outputMatrix["+str(index)+"]",str(npo_actual_name)+".offsetParentMatrix")
                index +=1
    return dummy_geos

def export_bldshp_weights(objs,path):
    
    geo_and_tgts_list = []
    
    for obj in objs:
        try:
            bs_node = ema.get_bldshp_nodes_from_obj(obj)[0]
            tgts = ema.get_all_tgt_names_from_bldshp(bs_node)
            geo_and_tgts_list.append((obj,tgts))
        except IndexError as e:
            print(e)


    
    ema.export_bldshp_weights_as_json(geo_and_tgts_list,path)

def copy_weights_to_another(src_geo,tgt_geo):
    src_bs_node = ema.get_bldshp_nodes_from_obj(src_geo)[0]
    tgts = ema.get_all_tgt_names_from_bldshp(src_bs_node)
    tgt_bs_node = ema.get_bldshp_nodes_from_obj(tgt_geo)[0]
    if src_bs_node:
        for tgt in tgts:
            ema.copy_bldshp_weight(src_geo,src_bs_node,tgt,tgt_geo,tgt_bs_node,tgt)
    
def copy_weights_to_dummys(dummys,dummy_suffix,base_suffix=''):
    for dummy in dummys:
        copy_weights_to_another(dummy.replace(dummy_suffix,base_suffix),dummy)


def rebuild_blendshape(bsp_path,weight_path):
    import_and_connect_bldshp(bsp_path)
    ema.import_same_bldshp_weight_from_json(weight_path)

    dummys = ema.get_exact_type_obj_in_grp('dummy_Grp','mesh',shape=False)
    copy_weights_to_dummys(dummys,'_dummy')
    
    connect_step_to_the_other('mouthSlider_setup','dummy')
    connect_step_to_the_other('eyebrows_setup','dummy',omit_geos=['C_Head_Geo'])
    
    return
    
    
    
def connect_step_to_the_other(src_suf,tgt_suf,omit_geos=None):
    omit_geos = omit_geos or []
    
    src_geos = cmds.ls('*_{}'.format(src_suf),type='transform')
    if not src_geos:
        print('there are no objs with suffix {}'.format(src_suf))
    src_geos = [geo for geo in src_geos if cmds.listRelatives(geo,s=True) and geo.replace('_{}'.format(src_suf),'') not in omit_geos]
    print('src_geos',src_geos)
    for src_geo in src_geos:
        tgt_geo = src_geo.replace(src_suf,tgt_suf)
        if cmds.objExists(tgt_geo):
            ema.connect_bldshp(tgt_geo,src_geo)

def connect_ctl_to_hooks(facial_ctl,hook):
    
    attrs = cmds.listAttr(hook)
    exps = [attr for attr in attrs if attr.startswith('eye') or attr.startswith('mouth')]
    for exp in exps:
        cmds.addAttr(facial_ctl,longName = exp, attributeType="float", defaultValue=0, h=0, k=1, min=0, max=1)
        cmds.connectAttr('{}.{}'.format(facial_ctl,exp),'{}.{}'.format(hook,exp))

def add_hash_to_matrix_and_ik_nodes():

    now = datetime.datetime.now()
    mat_nodes = cmds.ls('*Matrix*')
    ik_crvs = cmds.ls('*rollRef_crv','*RollRef_crv')

    hash = hashlib.md5(str(now).encode()).hexdigest()

    crypto = hash[now.second%10]+hash[int(now.microsecond/243%10)]+hash[now.microsecond/333%10]

    for mat_node in mat_nodes:
        cmds.rename(mat_node,mat_node.replace('Matrix',crypto+'_Mat'))
    for ik_crv in ik_crvs:

        crv = cmds.rename(ik_crv,ik_crv.replace('Ref_crv',crypto+'_Ref_crv'))
        shapes = cmds.listRelatives(crv,s=True)
        for shape in shapes:
            cmds.rename(shape,shape.replace('Ref_crv',crypto+'_Ref_crv'))