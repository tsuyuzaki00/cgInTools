# \_template
- [x] 編集中
- [ ] 編集済み

[一般向け(person)](../_template.md)

## クラス一覧
class [Class001(object)](#class-class001-page)   
class [Class002(object)](#class-class002-page)  
class [Class003(object)](#class-class003-page)  

## 関数一覧
def [functionOnly()](#def-functiononly)  

## 変数一覧
None

---

# class Class001 Page
>Inheritance :  
継承しているものを書く無い場合はobjectと書く

>import :  
インポートで使用している専用ライブラリのみ書く  
[\_template](_template.md)

>Summary :  
Class001のざっくりした内容を書く

## Special Function
def [\_\_init\_\_()](#class001__init__)

## Single Function
def [single_mode_func()](#class001single_mode_func)  

## Multi Function
def [\_multi_mode_func()](#class001_multi_mode_func)  

## Inheritance Function
def [\_inheritance_mode_func()](#class001_inheritance_mode_func)  

## Private Function
def [\_\_private_mode_func()](#class001__private_mode_func)  

## Setting Function
def [setSetting()](#class001setsetting)  
def [addSetting()](#class001addsetting)  
def [currentSetting()](#class001currentsetting)  
def [getSetting()](#class001getsetting)  

## Public Function
def [public()](#class001public) 

---

# class Class002 Page
>Inheritance :  
継承しているものを書く無い場合はobjectと書く

>import :  
インポートで使用している専用ライブラリのみ書く  
[\_template](_template.md)

>Summary :  
Class002のざっくりした内容を書く  

## Special Function
def [\_\_init\_\_()](#class002__init__)
## Single Function
def [single_mode_func()](#class002single_mode_func)  

## Multi Function
def [\_multi_mode_func()](#class002_multi_mode_func)  

## Inheritance Function
def [\_inheritance_mode_func()](#class002_inheritance_mode_func)  

## Private Function
def [\_\_private_mode_func()](#class002__private_mode_func)  

## Setting Function
def [setSetting()](#class002setsetting)  
def [addSetting()](#class002addsetting)  
def [currentSetting()](#class002currentsetting)  
def [getSetting()](#class002getsetting)  

## Public Function
def [public()](#class002public)  

---
# class Class003 Page
>Inheritance :  
object

>import :  
None

>Summary :  
とくになし

## Special Function
None
## Single Function
None

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function
None

## Public Function
None

---

# class Class001
## Special Function
### Class001.\_\_init\_\_()
>Signature :  
instance=Class001()  
\_localVariable_value=None  

>Parameters :  
None

>Returns :  
None

>Description :  
\_localVariable_value - 変数の説明を書く  
## Single Function
### Class001.single_mode_func()
>Signature :  
single_mode_func()

>Parameters :  
None

>Returns :  
None

>Description :  
単独でも使用できる関数
## Multi Function
### Class001.\_multi_mode_func()
>Signature :  
\_multi_mode_func()

>Parameters :  
None

>Returns :  
None

>Description :  
single_mode_func()関数が内部にある関数

## Inheritance Function
### Class001.\_inheritance_mode_func()
>Signature :  
\_inheritance_mode_func()

>Parameters :  
None

>Returns :  
None

>Description :  
継承や合成(委譲)した関数が内部にある関数

## Private Function
### Class001.\_\_private_mode_func()
>Signature :  
\_\_private_mode_func()

>Parameters :  
None

>Returns :  
None  

>Description :  
継承や合成(委譲)した際に使用されないようにする関数

## Setting Function
### Class001.setSetting()
>Signature :  
setSetting(variable)

>Parameters :  
variable - value  

>Returns :  
value

>Description :  
クラス内変数に設定する関数

### Class001.addSetting()
>Signature :  
addSetting(variables)

>Parameters :  
variables - list  

>Returns :  
list

>Description :  
クラス内変数に追加する関数  
シーケンスを渡す事が多い

### Class001.currentSetting()
>Signature :  
currentSetting()

>Parameters :  
None

>Returns :  
value

>Description :  
取得してクラン内変数に設定する関数  
パラメータには何も入れない

### Class001.getSetting()
>Signature :  
getSetting()

>Parameters :  
None

>Returns :  
value

>Description :  
クラス内変数に設定している変数を返す関数  
パラメータには何も入れない

## Public Function
### Class001.public()
>Signature :  
setSetting()  
public() or public(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

---

# class Class002
## Special Function
### Class002.\_\_init\_\_()
>Signature :  
instance=Class002()  
\_localVariable_value=None  

>Parameters :  
None

>Returns :  
None

>Description :  
\_localVariable_value - 変数の説明を書く  
## Single Function
### Class002.single_mode_func()
>Signature :  
single_mode_func()  

>Parameters :  
None

>Returns :  
None

>Description :  
単独でも使用できる関数

## Multi Function
### Class002.\_multi_mode_func()
>Signature :  
\_multi_mode_func()

>Parameters :  
None

>Returns :  
None

>Description :  
single_mode_func()関数が内部にある関数

## Inheritance Function
### Class002.\_inheritance_mode_func()
>Signature :  
\_inheritance_mode_func()

>Parameters :  
None

>Returns :  
None

>Description :  
継承や合成(委譲)した関数が内部にある関数

## Private Function
### Class002.\_\_private_mode_func()
>Signature :  
\_\_private_mode_func()

>Parameters :  
None

>Returns :  
None  

>Description :  
継承や合成(委譲)した際に使用されないようにする関数

## Setting Function
### Class002.setSetting()
>Signature :  
setSetting(variable)

>Parameters :  
variable - value  

>Returns :  
value

>Description :  
クラス内変数に設定する関数

### Class002.addSetting()
>Signature :  
addSetting(variables)

>Parameters :  
variables - list  

>Returns :  
list

>Description :  
クラス内変数に追加する関数  
シーケンスを渡す事が多い

### Class002.currentSetting()
>Signature :  
currentSetting()

>Parameters :  
None

>Returns :  
value

>Description :  
取得してクラン内変数に設定する関数  
パラメータには何も入れない

### Class002.getSetting()
>Signature :  
getSetting()

>Parameters :  
None

>Returns :  
value

>Description :  
クラス内変数に設定している変数を返す関数  
パラメータには何も入れない

## Public Function
### Class002.public()
>Signature :  
setSetting()  
public() or public(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

---

# Functions
### def functionOnly()
>Signature :  
functionOnly()

>Parameters :  
None

>Returns :  
None

>Description :  
関数...以上

---

# Variables
None

---

[back](../README.md) [Top](#_template)