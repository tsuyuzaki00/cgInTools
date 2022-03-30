import pymel.core as pm

lists = ['L_eyebrowUp',
        'R_eyebrowUp',
        'L_eyebrowDown',
        'R_eyebrowDown',
        'L_eyeOpen',
        'R_eyeOpen',
        'L_eyelashUp',
        'R_eyelashUp',
        'L_eyelashDown',
        'R_eyelashDown',
        'L_eyeBlink',
        'R_eyeBlink',
        'C_mouthOo',
        'C_mouthUp',
        'L_mouthUp',
        'R_mouthUp',
        'C_mouthBite',
        'L_mouthBite',
        'R_mouthBite',
        'C_angryMouth',
        'L_angryMouth',
        'R_angryMouth',
        'C_sadMouth',
        'L_sadMouth',
        'R_sadMouth']

sel = pm.selected()[0]

for i in lists:
    pm.addAttr(ln = i, k = True, at = 'float', min = 0, max = 1)
    pm.connectAttr(sel + '.' + i , 'facialBlenShape.' + i)