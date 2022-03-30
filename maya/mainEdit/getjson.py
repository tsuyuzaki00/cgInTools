import json
jsonPath = u'D:/Maya/data/json/humanIKinMgear/'

class InJson():
    def __init__(self):
        self.sels = pm.selected()
    
    def attrs(self):
        for sel in self.sels:
            pm.select(sel)
            selLists = pm.listAttr(k=True)
            return selLists
    
    def keyTimes(self):
        for sel in self.sels:
            pass
    
    def jsonGrp(self):
        keys = []
        for sel in self.sels:
            for attr in self.attrs():
                lists = {'time':1,'source':str(sel), 'attribute':attr,'value':pm.getAttr(sel + '.' + attr)}
                keys.append(lists)
        return keys
    
    def run(self):
        s = self.jsonGrp()
        with open(jsonPath + 'jointHierarchy.json', 'w') as f:
        	json.dump(s, f, indent = 4, ensure_ascii = False)

        '''
        for key in self.jsonGrp():
            pm.currentTime(key['time'])
            pm.setAttr(key['destination'] + '.' + key['attribute'], key['value'])
        '''

inJson = InJson()
inJson.run()

nameSpace = "gmr_chr_mb1_pxr:"
connects = [
    {"destination":nameSpace + "body_C0_ctl", "source":"spine_C0_0_jnt"},
    {"destination":nameSpace + "leg_L0_fk0_ctl", "source":"leg_L0_0_jnt"},
	{"destination":nameSpace + "leg_L0_fk1_ctl", "source":"leg_L0_4_jnt"},
	{"destination":nameSpace + "leg_L0_fk2_ctl", "source":"leg_L0_end_jnt"},
	{"destination":nameSpace + "foot_L0_fk0_ctl", "source":"foot_L0_1_jnt"},
	{"destination":nameSpace + "leg_R0_fk0_ctl", "source":"leg_R0_0_jnt"},
	{"destination":nameSpace + "leg_R0_fk1_ctl", "source":"leg_R0_4_jnt"},
	{"destination":nameSpace + "leg_R0_fk2_ctl", "source":"leg_R0_end_jnt"},
	{"destination":nameSpace + "foot_R0_fk0_ctl", "source":"foot_R0_1_jnt"},
	{"destination":nameSpace + "spine_C0_fk0_ctl", "source":"spine_C0_1_jnt"},
	{"destination":nameSpace + "spine_C0_fk1_ctl", "source":"spine_C0_2_jnt"},
	{"destination":nameSpace + "spine_C0_fk2_ctl", "source":"spine_C0_3_jnt"},
	{"destination":nameSpace + "shoulder_L0_ctl", "source":"shoulder_L0_shoulder_jnt"},
	{"destination":nameSpace + "arm_L0_fk0_ctl", "source":"arm_L0_0_jnt"},
	{"destination":nameSpace + "arm_L0_fk1_ctl", "source":"arm_L0_4_jnt"},
	{"destination":nameSpace + "arm_L0_fk2_ctl", "source":"arm_L0_end_jnt"},
	{"destination":nameSpace + "shoulder_R0_ctl", "source":"shoulder_R0_shoulder_jnt"},
	{"destination":nameSpace + "arm_R0_fk0_ctl", "source":"arm_R0_0_jnt"},
	{"destination":nameSpace + "arm_R0_fk1_ctl", "source":"arm_R0_4_jnt"},
	{"destination":nameSpace + "arm_R0_fk2_ctl", "source":"arm_R0_end_jnt"},
	{"destination":nameSpace + "neck_C0_fk0_ctl", "source":"neck_C0_0_jnt"},
	{"destination":nameSpace + "neck_C0_head_ctl", "source":"neck_C0_head_jnt"},
    ]
keyCount = 1830
start = 100

for connect in connects:
    for key in range(keyCount):
        pm.currentTime(key)
        pm.setAttr(connect["destination"] + '.' + "rotateX", pm.getAttr(connect["source"] + "." + "rotateX"))
        pm.setAttr(connect["destination"] + '.' + "rotateY", pm.getAttr(connect["source"] + "." + "rotateY"))
        pm.setAttr(connect["destination"] + '.' + "rotateZ", pm.getAttr(connect["source"] + "." + "rotateZ"))