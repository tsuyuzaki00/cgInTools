# pathLB
- [ ] 編集中
- [x] 編集済み

[一般向け(person)](../pathLB.md)

## クラス一覧
class [Path(object)](#class-path-page)   

## 関数一覧
None

## 変数一覧
None

---

# class Path Page
>Inheritance :  
object

>import :    
os,shutil

>Summary :  
directory,folder,file,path  
フォルダ階層、フォルダー、ファイル、フォルダ階層とファイルを合わせたものをパス  
を所持ているオブジェクト  

## Special Function
def [\_\_init\_\_()](#path__init__)  
def [\_\_str\_\_()](#path__str__)  
def [\_\_rshift\_\_()](#path__rshift)  
def [\_\_irshift\_\_()](#path__irshift)  
def [\_\_lshift\_\_()](#path__lshift)  
def [\_\_ilshift\_\_()](#path__ilshift)  

## Single Function
def [mergeDirectory_create_dir()](#pathmergedirectory_create_dir)  
def [mergePath_create_path()](#pathmergepath_create_path)

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function
def [setAbsoluteDirectory()](#pathsetabsolutedirectory)  
def [getAbsoluteDirectory()](#pathgetabsolutedirectory)  
def [setRelativeDirectory()](#pathsetrelativedirectory)  
def [addRelativeDirectory()](#pathaddrelativedirectory)  
def [getRelativeDirectory()](#pathgetrelativedirectory)  
def [setFile()](#pathsetfile)  
def [getFile()](#pathgetfile)  
def [setExtension()](#pathsetextension)  
def [getExtension()](#pathgetextension)  
def [setTargetPath()](#pathsettargetpath)  
def [getTargetPath()](#pathgettargetpath)  
def [setSourcePath()](#pathgetsourcepath)  
def [getSourcePath()](#pathgetsourcepath)  

## Public Function
def [queryDirectory()](#pathquerydirectory)  
def [queryAbsolutePath()](#pathqueryabsolutepath)  
def [queryRelativePath()](#pathqueryrelativepath)  
def [querySequencePath()](#pathquerysequencepath)  
def [createFileExt()](#pathcreatefileext)  
def [deleteFileExt()](#pathdeletefileext)  
def [createDirectory()](#pathcreatedirectory)  
def [targetPathMove()](#pathtargetpathmove)  
def [targetPathCopy()](#pathtargetpathcopy)  
def [sourcePathMove()](#pathsourcepathmove)  
def [sourcePathCopy()](#pathsourcepathcopy)  

---
# class Path
## Special Function
### Path.\_\_init\_\_()
>Signature :  
instance=Path()  
\_absolute\_dir=None  
\_relative\_dir=None  
\_file\_str=None  
\_extension\_ext=None  
\_target\_Path=None
\_source\_Path=None

>Parameters :  
None

>Returns :  
None

>Description :  
\_absolute\_dir - 絶対ディレクトリを保持する変数  
\_relative\_dir - 相対ディレクトリを保持する変数  
\_file\_str - ファイル名を保持する変数  
\_extension\_ext - 拡張子名を保持する変数  
\_target\_Path - 支持するためのオブジェクト
\_source\_Path - 受け取るためのオブジェクト

### Path.\_\_str\_\_()
>Signature :  
instance=Path()  
instance.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance.[setFile()](#pathsetfile)  
instance.[setExtension()](#pathsetextension)  
print(instance) or str(instance)  

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイルパスを返す

### Path.\_\_rshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 >> instance2

>Parameters :  
None

>Returns :  
None

>Description :  
instance1からinstance2に移動する

### Path.\_\_irshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 >>= instance2

>Parameters :  
None

>Returns :  
None

>Description :  
instance1からinstance2にコピーする

### Path.\_\_lshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 << instance2

>Parameters :  
None

>Returns :  
None

>Description :  
instance2からinstance1に移動する

### Path.\_\_ilshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 <<= instance2

>Parameters :  
None  

>Returns :  
None  

>Description :  
instance2からinstance1にコピーする  

## Single Function
### Path.mergeDirectory_create_dir()
>Signature :  
mergeDirectory_create_dir(upperDirectory_dir,lowerDirectory_dir)  

>Parameters :  
upperDirectory_dir - string(directory)  
lowerDirectory_dir - string(directory)  

>Returns :  
string(directory)  

>Description :  
絶対フォルダ階層と相対フォルダ階層を結合する関数  

### Path.mergePath_create_path()
>Signature :  
mergePath_create_path(directory_dir,file_str,extension_ext)

>Parameters :  
directory_dir - string(directory)  
file_str - string  
extension_ext - string(extension)  

>Returns :  
string(path)  

>Description :  
フォルダ階層、ファイル名、拡張子名を結合する関数  

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function
### Path.setAbsoluteDirectory()
>Signature :  
setAbsoluteDirectory(variable)  

>Parameters :  
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
絶対フォルダ階層を設定する関数  

### Path.addAbsoluteDirectory()
>Signature :  
addAbsoluteDirectory(variable)  

>Parameters :  
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
絶対フォルダ階層に階層を追加する関数  

### Path.getAbsoluteDirectory()
>Signature :  
getAbsoluteDirectory()  

>Parameters :  
None  

>Returns :  
string(directory)  

>Description :  
設定した絶対フォルダ階層を返す関数  

### Path.setRelativeDirectory()
>Signature :  
setRelativeDirectory(variable)  

>Parameters :  
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
相対フォルダ階層を設定する関数  

### Path.addRelativeDirectory()
>Signature :  
addRelativeDirectory(variable)  

>Parameters :  
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
相対フォルダ階層に階層を追加する関数  

### Path.getRelativeDirectory()
>Signature :  
getRelativeDirectory()  

>Parameters :  
None  

>Returns :  
string(directory)  

>Description :  
設定した相対フォルダ階層を返す関数

### Path.setFile()
>Signature :  
setFile(variable)

>Parameters :  
variable - string  

>Returns :  
string  

>Description :  
ファイル名を設定する関数  

### Path.getFile()
>Signature :  
getFile()  

>Parameters :  
None  

>Returns :  
string  

>Description :  
設定したファイル名を返す関数  

### Path.setExtension()
>Signature :  
setExtension(variable)

>Parameters :  
variable - string(extension)

>Returns :  
string(extension)

>Description :  
拡張子名を設定する関数  

### Path.getExtension()
>Signature :  
getExtension()  

>Parameters :  
None  

>Returns :  
string(extension)  

>Description :  
設定した拡張子名を返す関数  

### Path.setTargetPath()
>Signature :  
setTargetPath(variable)

>Parameters :  
variable - [Path](#class-path)  

>Returns :  
[Path](#class-path)  

>Description :  
影響を与えるパスオブジェクトを設定する関数  

### Path.getTargetPath()
>Signature :  
getTargetPath()  

>Parameters :  
None  

>Returns :  
[Path](#class-path)  

>Description :  
設定した影響を与えるパスオブジェクトを返す関数  

### Path.setSourcePath()
>Signature :  
setSourcePath(variable)

>Parameters :  
variable - [Path](#class-path)  

>Returns :  
[Path](#class-path)  

>Description :  
影響を受けるパスオブジェクトを設定する関数  

### Path.getSourcePath()
>Signature :  
getSourcePath()  

>Parameters :  
None  

>Returns :  
[Path](#class-path)  

>Description :  
設定した影響を受けるパスオブジェクトを返す関数  

## Public Function
### Path.queryDirectory()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
queryDirectory() or queryDirectory(absolute=None,relative=None)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  

>Returns :  
string(directory)  

>Description :  
絶対フォルダ階層と相対フォルダ階層を結合した文字列を返す関数  
### Path.queryAbsolutePath()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
queryAbsolutePath() or queryAbsolutePath(absolute=None,relative=None,file=None,ext=None)

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
string(path)  

>Description :  
絶対パスを返す関数  

### Path.queryRelativePath()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
queryRelativePath() or queryRelativePath(relative=None,file=None,ext=None)

>Parameters :  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
string(path)  

>Description :  
相対パスを返す関数  

### Path.querySequencePath()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
querySequencePath() or querySequencePath(absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
sequence of string  

>Description :  
フォルダ階層ごと、ファイル名、拡張子名とバラバラにしてlist文字列で返す関数

### Path.createFileExt()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
createFileExt() or createFileExt(absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
None  

>Description :  
新しくファイル名を作成する関数  

### Path.deleteFileExt()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
deleteFileExt() or deleteFileExt(absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
None  

>Description :  
指定したファイル名を削除する関数  

### Path.createDirectory()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
createDirectory() or createDirectory(absolute=None,relative=None)  

>Parameters :  
absolute - string(directory)  
relative - string(directory)  

>Returns :  
None  

>Description :  
同じ名前のフォルダ階層が無ければフォルダ階層を作成する関数  

### Path.createEnvironmentVariable()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
createEnvironmentVariable() or createEnvironmentVariable(directory=None,environName=None)  

>Parameters :  
directory - string(directory)  
environName - string(directory)  

>Returns :  
string(directory)  

>Description :  
環境変数を作成する関数  

### Path.targetPathMove()
>Signature :  
[setTargetPath()](#pathsettargetpath)
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
deleteFileExt() or deleteFileExt(targetPath=None,absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
targetPath - [Path](#class-path)  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
None  

>Description :  
現在所持しているPathをtargetPathに移す関数  

### Path.targetPathCopy()
>Signature :  
[setTargetPath()](#pathsettargetpath)
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
deleteFileExt() or deleteFileExt(targetPath=None,absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
targetPath - [Path](#class-path)  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
None  

>Description :  
現在所持しているPathをtargetPathにコピーする関数  

### Path.sourcePathMove()
>Signature :  
[setSourcePath()](#pathsetsourcepath)
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
deleteFileExt() or deleteFileExt(sourcePath=None,absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
sourcePath - [Path](#class-path)  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
None  

>Description :  
sourcePathを現在所持しているPathに移す関数  

### Path.sourcePathCopy()
>Signature :  
[setSourcePath()](#pathsetsourcepath)
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
[setRelativeDirectory()](#pathsetrelativedirectory)  
[setFile()](#pathsetfile)  
[setExtension()](#pathsetextension)  
deleteFileExt() or deleteFileExt(sourcePath=None,absolute=None,relative=None,file=None,ext=None)  

>Parameters :  
sourcePath - [Path](#class-path)  
absolute - string(directory)  
relative - string(directory)  
file - string  
ext - string(extension)  

>Returns :  
None  

>Description :  
sourcePathを現在所持しているPathにコピーする関数  
---
# Functions
None

---
# Variables
None

---
[back](../../README.md) [Top](#pathlb)