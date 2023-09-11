# baseLB
- [ ] 編集中
- [x] 編集済み

[玄人向け(professional)](./_professional/baseLB.md)

## クラス一覧
class : [SelfOrigin(object)](#class-selforigin-page)

## 関数一覧
None

## 変数一覧
None

---

# class SelfOrigin Page
>Inheritance :  
object

>import :  
None

>Summary :  
データを取得してアクションをするの指示が入っているクラス

## Setting Function
def [setDataDict()](#selforiginsetdatadict)  
def [getDataDict()](#selforigingetdatadict)  
def [setDataChoices()](#selforiginsetdatachoices)  
def [addDataChoices()](#selforiginadddatachoices)  
def [getDataChoices()](#selforigingetdatachoices)  
def [setDoIts()](#selforiginsetdoIts)  
def [addDoIts()](#selforiginadddoits)  
def [getDoIts()](#selforigingetdoits)  
## Public Function
def [writeData()](#selforiginwritedata)  
def [readData()](#selforiginreaddata)  
def [doIt()](#selforigindoit)  

---
# class SelfOrigin
## Setting Function
### SelfOrigin.setDataDict()
>Signature :  
setDataDict(variable)

>Parameters :  
variable - dict

>Returns :  
dict

>Description :  
setting関数たちに組み込むためのdictを読み込む関数

### SelfOrigin.getDataDict()
>Signature :  
getDataDict()

>Parameters :  
None

>Returns :  
dict

>Description :  
setting関数に設定するdictを返す関数

### SelfOrigin.setDataChoices()
>Signature :  
setDataChoices(variables)

>Parameters :  
variables - sequence of string

>Returns :  
sequence of string

>Description :  
writeDict()を実行した際に書き出せるように設定する関数  
writeDict()に書き出したいsetting関数のset,getを除いた文字列を入れる必要がある  
例: setNode(),getNode()があった場合setDataChoices(["Node"])となる  

### SelfOrigin.addDataChoices()
>Signature :  
addDataChoices(variables)

>Parameters :  
variables - sequence of string

>Returns :  
sequence of string

>Description :  
writeDict()を実行した際に書き出せるように設定を追加する関数  
writeDict()に書き出したいsetting関数のset,getを除いた文字列を入れる必要がある  
例: setNode(),getNode()があった場合addDataChoices(["Node"])となる  

### SelfOrigin.getDataChoices()
>Signature :  
getDataChoices()

>Parameters :  
None

>Returns :  
sequence of string

>Description :  
設定した書き出す予定のシーケンス文字列を返す関数

### SelfOrigin.setDoIts()
>Signature :  
setDoIts(variables)

>Parameters :  
variables - sequence of string

>Returns :  
sequence of string

>Description :  
doIt()を実行した際に実行してほしいpublic関数名を設定する関数  
例: read(),create()があった場合setDoIts(["read","create"])となる

### SelfOrigin.addDoIts()
>Signature :  
addDoIts(variables)

>Parameters :  
variables - sequence of string

>Returns :  
sequence of string

>Description :  
doIt()を実行した際に実行してほしいpublic関数名を設定に追加する関数  
例: read(),create()があった場合addDoIts(["read","create"])となる

### SelfOrigin.getDoIts()
>Signature :  
getDoIts()

>Parameters :  
None

>Returns :  
sequence of string

>Description :  
設定したpublic関数名のlistを返す関数

## Public Function
### SelfOrigin.writeData()
>Signature :  
[setDataChoices()](#selforiginsetdatachoices)  
writeData() or writeData(dataChoices)

>Parameters :  
dataChoices - sequence of string

>Returns :  
dict

>Description :  
dataChoicesで設定したsetting関数をdictで返す関数

### SelfOrigin.readData()
>Signature :  
[setDataDict()](#selforiginsetreaddict)  
readData() or readData(settingData)

>Parameters :  
settingData - dict

>Returns :  
None

>Description :  
dictを使ってsetting関数たちに読み込ませる関数

### SelfOrigin.doIt()
>Signature :  
[setDoIts](#selforiginsetdoits)  
doIt() or doIt(doIts)

>Parameters :  
doIts - sequence of string

>Returns :  
None

>Description :  
doItsで設定したpublic関数を順番に実行する関数

---

# Functions
None

---

# Variables
None

---
[back](../README.md) [Top](#baselb)