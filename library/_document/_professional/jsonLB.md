# jsonLB
- [ ] 編集中
- [x] 編集済み

[一般向け(person)](../jsonLB.md)

## クラス一覧
class [Json()](#class-json-page)  
class [JsonPack()](#class-jsonpack-page)  

## 関数一覧
def [readJson()](#def-readjson)  
def [writeJson()](#def-writejson)  

## 変数一覧
None

---
# class Json Page
>Inheritance :  
object

>import :  
[json](https://docs.python.org/ja/3/library/json.html)  
[Path](./pathLB.md)  

>Summary :  
Jsonファイルを読み込み書き出しするクラス

## Special Function
def [\_\_init\_\_()](#json__init__)

## Single Function
def [jsonPath_query_dict()](#jsonjsonpath_query_dict)  
def [jsonPath_create_func()](#jsonjsonpath_create_func)  
## Multi Function
None
## Inheritance Function
None
## Private Function
None
## Setting Function
def [setAbsoluteDirectory()](#jsonsetabsolutedirectory)  
def [getAbsoluteDirectory()](#jsongetabsolutedirectory)  
def [setRelativeDirectory()](#jsonsetrelativedirectory)  
def [getRelativeDirectory()](#jsongetrelativedirectory)  
def [setFile()](#jsonsetfile)  
def [getFile()](#jsongetfile)  
def [setExtension()](#jsonsetextension)  
def [getExtension()](#jsongetextension)  
def [setWriteDict()](#jsonsetwritedict)  
def [getWriteDict()](#jsongetwritedict)  
## Public Function
def [read()](#jsonread)  
def [write()](#jsonwrite)  

---
# class JsonPack Page
>Inheritance :  
object

>import :  
[Path](./pathLB.md)  
[Json](#class-json-page)

>Summary :  
複数のJsonファイルを読み込み書き出しするクラス

## Special Function
def [\_\_init__()]()

## Single Function
None
## Multi Function
None
## Inheritance Function
None
## Private Function
def [\_\_readPack_query_dicts()](#jsonpackreadpackquerydicts)  
def [\_\_writePack_create_func()](#jsonpackwritepackcreatefunc)  
## Setting Function
def [setAbsoluteDirectory()](#jsonpacksetabsolutedirectory)  
def [getAbsoluteDirectory()](#jsonpackgetabsolutedirectory)  
def [setRelativeDirectory()](#jsonpacksetrelativedirectory)  
def [getRelativeDirectory()](#jsonpackgetrelativedirectory)  
def [setFile()](#jsonpacksetfile)  
def [getFile()](#jsonpackgetfile)  
def [setExtension()](#jsonpacksetextension)  
def [getExtension()](#jsonpackgetextension)  
def [setJsonObjects()](#jsonpacksetjsonobjects)  
def [addJsonObjects()](#jsonpackaddjsonobjects)  
def [getJsonObjects()](#jsonpackgetjsonobjects)  
## Public Function
def [readPack()](#jsonpackreadpack)  
def [writePack()](#jsonpackwritepack)  

---
# class Json
## Special Function
### Json.\_\_init\_\_()
>Signature :  
instance=Json()  
\_json\_Path=Path()  
\_write\_dict={}  

>Parameters :  
None

>Returns :  
None

>Description :  
\_json\_Path - パスを操作するオブジェクト  
\_write\_dict - 書き出す辞書を保持する変数  
## Single Function
### Json.jsonPath_query_dict()
>Signature :  
jsonPath_query_dict(path)

>Parameters :  
path - string(path)

>Returns :  
dict

>Description :  
指定したパスからjsonファイルを読み込む関数

### Json.jsonPath_create_func()
>Signature :  
jsonPath_create_func(path,write_dict)

>Parameters :  
path - string(path)  
write_dict - dict  

>Returns :  
None

>Description :  
指定したパスにjsonファイルを書き出す関数
## Multi Function
None
## Inheritance Function
None
## Private Function
None
## Setting Function
### Json.setAbsoluteDirectory()
>Signature :  
setAbsoluteDirectory(variable)

>Parameters :  
variable - string

>Returns :  
string(directory)

>Description :  
上層フォルダ階層の文字列を設定する関数
### Json.getAbsoluteDirectory()
>Signature :  
getAbsoluteDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定した上層フォルダ階層の文字列を返す関数
### Json.setRelativeDirectory()
>Signature :  
setRelativeDirectory(variable)

>Parameters :  
variable - string

>Returns :  
string(directory)

>Description :  
下層フォルダ階層の文字列を設定する関数
### Json.getRelativeDirectory()
>Signature :  
getRelativeDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定した下層フォルダ階層の文字列を返す関数
### Json.setFile()
>Signature :  
setFile(variable)

>Parameters :  
variable - string

>Returns :  
string

>Description :  
ファイル名の文字列を設定する関数

### Json.getFile()
>Signature :  
getFile()

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイル名の文字列を返す関数

### Json.setExtension()
>Signature :  
setExtension(variable)

>Parameters :  
variable - string(extension)

>Returns :  
string(extension)

>Description :  
拡張子の文字列を設定する関数

### Json.getExtension()
>Signature :  
getExtension()

>Parameters :  
None

>Returns :  
string(extension)

>Description :  
設定した拡張子の文字列を返す関数

### Json.setWriteDict()
>Signature :  
setWriteDict(variable)

>Parameters :  
variable - dict

>Returns :  
dict

>Description :  
Jsonファイルに書き出す辞書を設定する関数

### Json.getWriteDict()
>Signature :  
 getWriteDict()

>Parameters :  
None

>Returns :  
dict

>Description :  
設定したJsonファイルに書き出す辞書を返す関数

## Public Function
### Json.read()
>Signature :  
[setAbsoluteDirectory(variable)](#jsonsetabsolutedirectory)  
[setRelativeDirectory(variable)](#jsonsetrelativedirectory)  
[setFile(variable)](#jsonsetfile)  
[setExtension(variable)](#jsonsetextension)  
read() or read(absolute=None,relative=None,file=None,extension=None)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
extension - string(extension)  

>Returns :  
dict

>Description :  
Jsonファイルを読み込む関数

### Json.write()
>Signature :  
[setAbsoluteDirectory(variable)](#jsonsetabsolutedirectory)  
[setRelativeDirectory(variable)](#jsonsetrelativedirectory)  
[setFile(variable)](#jsonsetfile)  
[setExtension(variable)](#jsonsetextension)  
[setWriteDict(variable)](#jsonsetwritedict)  
write() or write(absolute=None,relative=None,,file=None,extension=None,write=None)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
extension - string(extension)  
write - dict  

>Returns :  
None

>Description :  
Jsonファイルを書き出す関数

--- 
# class JsonPack
## Special Function
### JsonPack.\_\_init\_\_()
>Signature :  
instance=JsonPack()
\_jsonPack\_Path=Path()  
\_writePack_Jsons=[]  

>Parameters :  
None

>Returns :  
None

>Description :  
\_jsonPack\_Path=Path() - パスを操作するオブジェクト  
\_writePack_Jsons=[] - 複数のJsonオブジェクトを保持する変数  
## Single Function
None
##  Multi Function
None
## Inheritance Function
None
## Private Function
### JsonPack.\_\_readPack_query_dicts()
>Signature :  
\_\_readPack_query_dict(absolute,relative,file,extension)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
extension - string(extension)  

>Returns :  
dicts

>Description :  
JsonPackファイルを読み込む関数

### JsonPack.\_\_writePack_create_func()
>Signature :  
\_\_writePack_create_func(absolute,relative,file,extension,write_Jsons)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
extension - string(extension)  
write_Jsons - sequence of [Json](#class-json-page)  

>Returns :  
None

>Description :  
JsonPackファイルを書き出す関数
 
## Setting Function
### JsonPack.setAbsoluteDirectory()
>Signature :  
setAbsoluteDirectory(variable)

>Parameters :  
variable - string

>Returns :  
string(directory)

>Description :  
上層フォルダ階層の文字列を設定する関数
### JsonPack.getAbsoluteDirectory()
>Signature :  
getAbsoluteDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定した上層フォルダ階層の文字列を返す関数

### JsonPack.setRelativeDirectory()
>Signature :  
setRelativeDirectory(variable)

>Parameters :  
variable - string

>Returns :  
string(directory)

>Description :  
下層フォルダ階層の文字列を設定する関数

### JsonPack.getRelativeDirectory()
>Signature :  
getRelativeDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定した下層フォルダ階層の文字列を返す関数

### JsonPack.setFile()
>Signature :  
setFile(variable)

>Parameters :  
variable - string

>Returns :  
string

>Description :  
ファイル名の文字列を設定する関数

### JsonPack.getFile()
>Signature :  
getFile()

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイル名の文字列を返す関数

### JsonPack.setExtension()
>Signature :  
setExtension(variable)

>Parameters :  
variable - string(extension)

>Returns :  
string

>Description :  
拡張子の文字列を設定する関数

### JsonPack.getExtension()
>Signature :  
getExtension()

>Parameters :  
None

>Returns :  
string(extension)

>Description :  
設定した拡張子の文字列を返す関数

### JsonPack.setJsonObjects()
>Signature :  
setJsonObjects(variables)

>Parameters :  
variables - sequence of [Json](#class-json-page)

>Returns :  
sequence of [Json](#class-json-page)

>Description :  
書き出すJsonデータを設定する関数

### JsonPack.addJsonObjects()
>Signature :  
addJsonObjects(variables)

>Parameters :  
variables - sequence of [Json](#class-json-page)

>Returns :  
sequence of [Json](#class-json-page)

>Description :  
書き出すJsonデータを設定したものに追加する関数

### JsonPack.getJsonObjects()
>Signature :  
getJsonObjects()

>Parameters :  
None

>Returns :  
sequence of [Json](#class-json-page)

>Description :  
設定したJsonデータを返す関数

## Public Function
### JsonPack.readPack()
>Signature :  
[setAbsoluteDirectory(variable)](#jsonpacksetabsolutedirectory)  
[setRelativeDirectory(variable)](#jsonpacksetrelativedirectory)  
[setFile(variable)](#jsonpacksetfile)  
[setExtension(variable)](#jsonpacksetextension)  
readPack() or readPack(absolute=None,relative=None,file=None,extension=None)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
extension - string(extension)  

>Returns :  
None

>Description :  
jsonPackを読み込む関数

### JsonPack.writePack()
>Signature :  
[setAbsoluteDirectory(variable)](#jsonpacksetabsolutedirectory)  
[setRelativeDirectory(variable)](#jsonpacksetrelativedirectory)  
[setFile(variable)](#jsonpacksetfile)  
[setExtension(variable)](#jsonpacksetextension)  
[setJsonObjects(variable)](#jsonpacksetjsonobjects)
writePack() or writePack(absolute=None,relative=None,file=None,extension=None,writePack=None)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
extension - string(extension)  
writePack - sequence of [Json](#class-json-page)

>Returns :  
None

>Description :  
jsonPackを書き出す関数

---
# Functions
### def readJson()
>Signature :  
readJson(directory,file)

>Parameters :  
directory - string(directory)
file - string

>Returns :  
dict

>Description :  
拡張子をjsonで固定してファイルを読み込む関数

### def writeJson()
>Signature :  
writeJson(directory,file,write)

>Parameters :  
directory - string(directory)
file - string
write - dict

>Returns :  
None

>Description :  
拡張子をjsonで固定してjsonファイルを書き出す関数

---

# Variables
None

---
[back](../../README.md) [Top](#jsonlb)