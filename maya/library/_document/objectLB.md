# objectLB

[玄人向け(professional)](/maya/library/_document/_professional/objectLB.md)

## クラス一覧

[SelfNode(object)](#selfnode)

[SelfDagNode(SelfNode)](#selfdagnode)

[SelfConnectNode(SelfDagNode)](#selfconnectnode)

[SelfMatrixNode(SelfDagNode)](#selfmatrixnode)

[SelfLocationNode(SelfMatrixNode)](#selflocationnode)

[SelfAnimNode(SelfMatrixNode)](#selfanimnode)

[SelfWeightJoint(SelfConnectNode)](#selfweightjoint)

[SelfPolygon(SelfMatrixNode)](#selfpolygon)

[SelfSurface(SelfMatrixNode)](#selfsurface)

[SelfCreateNode(object)](#selfcreatenode)

<a id="selfnode"></a>
# class SelfNode

Inheritance : object

Summary : 自立ノードの原点
## Setting Function
def [\_\_init\_\_()](#__init__)

def [setNode()](#setnode)

def [getNode()](#getnode)

def [getNodeType()](#getnodetype)

def [setAttr()](#setattr)

def [getAttr()](#getattr)

def [setValue()](#setvalue)

def [getValue()](#getvalue)

## Public Function

def [editAttr()](#editattr)

def [queryAttr()](#queryattr)

===================

<a id="__init__"></a>
### def \_\_init\_\_()

Parameters : str(node name)

Returns : None

Documents : 自身が何のノードなのかを入れる必要がある

<a id="setnode"></a>
### def setNode()

Parameters : str(node name)

Returns : MObject

Documents : 自身のノードを変更する関数

<a id="getnode"></a>
### def getNode()

Parameters : fullPath=bool

Returns : str(node name)

Documents : 自身のノード名を返す関数

<a id="getnodetype"></a>
### def getNodeType()

Parameters : None

Returns : str(node type)

Documents : 自身のノードタイプを返す関数

<a id="setattr"></a>
### def setAttr()

Parameters : str(attribute name)

Returns : str(attribute name)

Documents : 自身が何のアトリビュートを所持しているかを決める関数

<a id="getattr"></a>
### def getAttr()

Parameters : None

Returns : str(attribute name)

Documents : 自身が何のアトリビュートを所持しているかを返す関数

<a id="setvalue"></a>
### def setValue()

Parameters : single variable

Returns : single variable

Documents : 自身が何の値を所持しているかを決める関数

<a id="getvalue"></a>
### def getValue()

Parameters : None

Returns : single variable

Documents : 自身が何の値を所持しているかを返す関数

<a id="editattr"></a>
### def editAttr()

Parameters : attr_str=str(attribute name),value=single variable

Returns : None

Documents : 設定した値を使用して設定したアトリビュートを変更する関数

<a id="queryattr"></a>
### def queryAttr()

Parameters : attr_str=str(attribute name),valueType_str=str(single variable name)

Returns : single variable

Documents : 設定したアトリビュートの値を返す関数