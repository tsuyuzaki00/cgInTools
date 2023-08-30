# jsonLB
- [ ] 編集中
- [x] 編集済み

[玄人向け(professional)](./_professional/jsonLB.md)

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
json,os

>Summary :  
Jsonファイルを読み込み書き出しするクラス

## Setting Function
def [setDirectory()](#jsonsetdirectory)  
def [getDirectory()](#jsongetdirectory)  
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
[Json](#class-json-page)

>Summary :  
複数のJsonファイルを読み込み書き出しするクラス

## Setting Function
def [setDirectory()](#jsonpacksetdirectory)  
def [getDirectory()](#jsonpackgetdirectory)  
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
## Setting Function
### Json.setDirectory()
>Signature :  
setDirectory(variable)

>Parameters :  
variable - string

>Returns :  
string(directory)

>Description :  
フォルダ階層の文字列を設定する関数
### Json.getDirectory()
>Signature :  
getDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定したフォルダ階層の文字列を返す関数

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
[setDirectory(variable)](#jsonsetdirectory)  
[setFile(variable)](#jsonsetfile)  
[setExtension(variable)](#jsonsetextension)  
read() or read(directory=None,file=None,extension=None)

>Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)  

>Returns :  
dict

>Description :  
Jsonファイルを読み込む関数

### Json.write()
>Signature :  
[setDirectory(variable)](#jsonsetdirectory)    
[setFile(variable)](#jsonsetfile)  
[setExtension(variable)](#jsonsetextension)  
[setWriteDict(variable)](#jsonsetwritedict)  
write() or write(directory=None,file=None,extension=None,write=None)

>Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)  
write - dict  

>Returns :  
None

>Description :  
Jsonファイルを書き出す関数

--- 
# class JsonPack
## Setting Function
### JsonPack.setDirectory()
>Signature :  
setDirectory(variable)

>Parameters :  
variable - string

>Returns :  
string(directory)

>Description :  
フォルダ階層の文字列を設定する関数
### JsonPack.getDirectory()
>Signature :  
getDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定したフォルダ階層の文字列を返す関数

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
[setDirectory(variable)](#jsonpacksetdirectory)  
[setFile(variable)](#jsonpacksetfile)  
[setExtension(variable)](#jsonpacksetextension)  
readPack() or readPack(directory=None,file=None,extension=None)

>Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)  

>Returns :  
None

>Description :  
jsonPackを読み込む関数

### JsonPack.writePack()
>Signature :  
[setDirectory(variable)](#jsonpacksetdirectory)  
[setFile(variable)](#jsonpacksetfile)  
[setExtension(variable)](#jsonpacksetextension)  
[setJsonObjects(variable)](#jsonpacksetjsonobjects)
writePack() or writePack(directory=None,file=None,extension=None,writePack=None)

>Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)

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
拡張子をjsonで固定してjsonファイルを書き込む関数

---

# Variables