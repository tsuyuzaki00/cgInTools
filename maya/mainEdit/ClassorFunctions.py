import pymel.core as pm

objs = pm.selected()

def select_center_pivot(objs):
    box1 = pm.xform(objs, query=True, boundingBox=True, ws=True)
    box1 = (((box1[0]+box1[3])/2),((box1[1]+box1[4])/2),((box1[2]+box1[5])/2))
    return box1

#self.proxyAttr(sel = UIAttr["UI"], name = UIAttr["attr"], source = UIAttr["option"])
def proxyAttr(get_ctrl_name,attr_name,create_ctrl_name):
    pm.select(get_ctrl_name)
    pm.addAttr(longName = attr_name, attributeType = "bool", defaultValue=0, k=False, proxy = create_ctrl_name + "." + attr_name)
    pm.setAttr(get_ctrl_name + "." + attr_name, cb=True)
    
class SetDrivenKey():
    def __init__(self,driver_obj,driven_obj,driver_attr,driven_attr,driver_value,driven_value,ctrl_obj=None):
        self.driver_obj = driver_obj
        self.driven_obj = driven_obj
        self.driver_attr = driver_attr
        self.driven_attr = driven_attr
        self.driver_value = driver_value
        self.driven_value = driven_value
        self.ctrl_obj = ctrl_obj

    def run(self):
        if self.ctrl_obj == None:
            self.normal_driven_key()
        else:
            self.ctrl_driven_key()

    def normal_driven_key(self):
        pm.setAttr(self.driver_obj + '.' + self.driver_attr, self.driver_value)
        pm.setAttr(self.driven_obj + '.' + self.driven_attr, self.driven_value)

        pm.setDrivenKeyframe(self.driven_obj + '.' + self.driven_attr, cd = self.driver_obj + '.' + self.driver_attr)

        pm.setAttr(self.driver_obj + '.' + self.driver_attr, 0)
        pm.setAttr(self.driven_obj + '.' + self.driven_attr, 0)

    def ctrl_driven_key(self):
        pm.setAttr(self.ctrl_obj + '.' + self.driver_attr, self.driver_value)
        pm.setAttr(self.driven_obj + '.' + self.driven_attr, self.driven_value)

        pm.setDrivenKeyframe(self.driven_obj + '.' + self.driven_attr, cd = self.driver_obj + '.' + self.driver_attr)

        pm.setAttr(self.ctrl_obj + '.' + self.driver_attr, 0)
        pm.setAttr(self.driven_obj + '.' + self.driven_attr, 0)

set_driven_list = [
    ["nurbsCircle1","C_model_geo_scene_01","rotateZ","translateX",-45,10,"nurbsCircle2"],
    ["nurbsCircle1","C_model_geo_scene_01","rotateZ","translateX",0,0,"nurbsCircle2"],
    ]

proxy_list = [
    ["spineUI_C0_ctl","neckIKCtl","options_C0_ctl"],
    ]

def proxyAttrRun():
    for pxy in proxy_list:
        proxyAttr(get_ctrl_name=pxy[0],attr_name=pxy[1],create_ctrl_name=pxy[2])

def drivenRun():
    for sdl in set_driven_list:
        sdk = SetDrivenKey(driver_obj=sdl[0],driven_obj=sdl[1],driver_attr=sdl[2],driven_attr=sdl[3],driver_value=sdl[4],driven_value=sdl[5],ctrl_obj=sdl[6])
        sdk.run()

proxyAttrRun()

#add_layer(layer_name="",add_obj=[]or"")
def add_layer(layer_name,add_obj):
    if pm.objExists(layer_name):
        pm.editDisplayLayerMembers(layer_name, add_obj, nr = True)
        pm.setAttr(layer_name + ".displayType", 2)
    else:
        layer = pm.createDisplayLayer(n = layer_name)
        pm.editDisplayLayerMembers(layer, add_obj, nr = True)
        pm.setAttr(layer + ".displayType", 2)

#add_null(null_name="",add_obj=[]or"")
def add_null(null_name,add_obj):
    new_grp = pm.createNode( 'transform', n = null_name )
    pm.parent(add_obj,new_grp)

#
def camera_mask_color(cam,color=(0,0,0),opacity=1.0):
    pm.setAttr(cam + ".displayResolution", 1)
    pm.setAttr(cam + ".displayGateMask", 1)
    pm.setAttr(cam + ".displayGateMaskOpacity", opacity)
    pm.setAttr(cam + ".displayGateMaskColor", color, type = "double3")

#
def trans_rot_lock(obj,lock=True):
    pm.setAttr(obj + ".translateX", l = lock)
    pm.setAttr(obj + ".translateY", l = lock)
    pm.setAttr(obj + ".translateZ", l = lock)
    pm.setAttr(obj + ".rotateX", l = lock)
    pm.setAttr(obj + ".rotateY", l = lock)
    pm.setAttr(obj + ".rotateZ", l = lock)

#
def get_target_trnsRot(target,source,parent_back):
    pm.parent(source,target)
    pm.setAttr(source + ".translateX", 0)
    pm.setAttr(source + ".translateY", 0)
    pm.setAttr(source + ".translateZ", 0)
    pm.setAttr(source + ".rotateX", 0)
    pm.setAttr(source + ".rotateY", 0)
    pm.setAttr(source + ".rotateZ", 0)
    pm.parent(source,parent_back)


"left_, _left, Left_, _Left, lt_, _lt, Lt_, _Lt, lft_, _lft, Lft_, _Lft, Lf_, _Lf, lf_, _lf, l_, _l, L_, _L"
"right_, _right, Right_, _Right, rt_, _rt, Rt_, _Rt, rgt_, _rgt, Rgt_, _Rgt, Rg_, _Rg, rg_, _rg, r_, _r, R_, _R"