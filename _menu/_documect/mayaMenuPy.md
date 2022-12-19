# mayaMenu.py

### 継承なし

<a id="classMenu"></a>
## Class Menu Functions

def [__ init __()](#__init__)

### Public Function
def [run()](#run)

### Multi Function
def [_settingsMenu_create_func()](#_settingsMenu_create)

def [_multiItem_create_func()](#_multiItem_create)

def [_singleItem_create_func()](#_singleItem_create)     

### Single Function
def [setItem_create_func()](#setItem_create)

def [setUpJson_quary_dict()](#setUpJson_quary)

## Direct Functions
def [setUp()](#setUp)

<a id="__init__"></a>
### def __ init __()

Parameters:None

self._path=string

self._file=string

Returns:None

Description:ファイルパスとJsonファイルを設定している

Loading Function or Class:None

<a id="run"></a>
### def run()

Parameters:None

Returns:None

Description:Mayaメニューバーに設定した内容を実行するための関数

初期設定は済んでいるためインスタンス化を行い実行すれば使用可能

Loading Function or Class:None

[_settingsMenu_create_func()](#_settingsMenu_create)

<a id="_settingsMenu_create"></a>
### def _settingsMenu_create_func()

Parameters:

menuTitle_str=string,

orderMenu_lists=["single"or"multi",dictKeyName],

menus_dict={KeyName:lists[[string,relativePath_string,fileName_string,function_string,imageFile_string]...]}

Returns:None

Description: アイテムを並列に並べるか入れ子構造にするか決める関数

1.menuTitle_str メニューバーに表示する文字列

2.orderMenu_lists [...,dictKeyName]を

single(アイテムを整列構造にするか)

multi(アイテムを入れ子構造にするか)

にするかを決めるリスト

3.menus_dict 実行させるためのアイテムをまとめた辞書

Loading Function or Class:

[_multiItem_create_func()](#_multiItem_create)

[_singleItem_create_func()](#_singleItem_create)   

<a id="_multiItem_create"></a>
### def _multiItem_create_func()

Parameters:

titleName=string,

multiItem_lists=[[string,relativePath_string,fileName_string,function_string,imageFile_string]...]

Returns:None

Description:アイテムをタイトルの入れ子にする関数

1.titleName タイトル名

2.multiItem_lists アイテムリスト

Loading Function or Class:

[setItem_create_func()](#setItem_create)

<a id="_singleItem_create"></a>
### def _singleItem_create_func()

Parameters:

titleName=string,

singleItem_lists=[[string,relativePath_string,fileName_string,function_string,imageFile_string]...]

Returns:None

Description:アイテムをタイトルの下に並べる関数

1.titleName タイトル名

2.singleItem_lists アイテムリスト

Loading Function or Class:

[setItem_create_func()](#setItem_create)

<a id="setItem_create"></a>
### def _setItem_create_func()

Parameters:

title=string

relativePath=string

fileName=string

function=string

image=string

Returns:None

Description:アイテムを作成する関数

1.title アイテム名 例:"Oomozi Hazimari"

2.relativePath 相対パス名 例:"cgInTools.maya.execute"

3.fileName pythonファイル名 例:"sample.py"

4.function 呼び出す関数名 例:"main()"

5.icon アイテム左側の画像 /iconsフォルダーに入れる必要あり 例:"sample.png"

Loading Function or Class:None

<a id="setUpJson_quary"></a>
### def setUpJson_quary_dict()

Parameters:

path=string

file=string

Returns:dict

Description:ファイルパスとjsonファイルを指定し呼び出す関数

1.path ファイルパス名

2.file jsonファイル名 例:mayaMenu *拡張子はなし

Loading Function or Class:None

<a id="setUp"></a>
### def setUp()

Parameters:None

Returns:None

Description:外部からインポートした際にメニューバー作成を実行できるようにした関数

Loading Function or Class:None

[Menu](#classMenu)

[run()](#run)