# Title

### attributeLB < setBaseLB

## class <span style="color:0066DD">ClassName</span>

## self Values:

### self._object

def [setObject()](#setobject)

def [getObject()](#getobject)

## Public function

## Private Function

## Multi Function

## Single Function

===================

<a id="setobject"></a>
### def setObject()

Parameters : object

Returns : object

<a id="getobject"></a>
### def getObject()

Parameters :

Returns : object

ch bool constructionHistory
n string name
    
mrt bool Match render tessellation
    
pt int
0:"Triangles"
1:"Quads"

f int
0:"Count"
1:"Standard fit"
2:"General"
3:"Control point"
    
mnd bool Match Normal Dir
ntr bool Normalize Trimmed UVRange

ut int [General] U Type
1:Per surf # of iso params in 3D
2:Per surf # of iso params
3:Per span # of iso params
un int [General] Number U
    
vt int [General] V Type
1:Per surf # of iso params in 3D
2:Per surf # of iso params
3:Per span # of iso params
vn int [General] Number V
    
uch bool [General] Use chord height
cht float [General] Chord height
ucr bool [General] Use chord height ratio
chr float [General][Standard fit] Chord height ratio
es bool [General] Edge swap
    
ft float [Standard fit] Fractional tolerance
mel float [Standard fit] Minimal edge length
d float [Standard fit] 3D delta
    
pc int [Count] Count

? uss bool
--example--
cmds.nurbsToPoly(self.obj,
    ch=self.constructionHistory,
    n=self.name,
    mrt=self.matchRender,
    f=self.format,
    pt=self.polyType,
    mnd=self.matchNormalDir,
    ntr=self.normalizeTrimmedUVRange,
    ut=self.uType,
    un=self.uNumber,
    vt=self.vType,
    vn=self.vNumber,
    uch=self.useChordHeigh,
    cht=self.chordHeight,
    ucr=self.useChordHeighRatio,
    chr=self.chordHeighRatio,
    es=self.edgeSwap,
    ft=self.fraction,
    mel=self.minEdgeLen,
    d=self.delta3D,
    pc=self.count,
    uss=True)