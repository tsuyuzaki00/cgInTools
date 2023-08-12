
### シングル変数(single variable)

single=bool or int or float or str

Document : bool型,int型,float型,str型のいずれかを示すときに使う

上記4つに全て当てはまる場合value型と定義することもある

Example : sample_bool=True 
sample_int=1 
sample_float=1.0
sample_str="text" 

### マルチ変数(multi variable)

multi=\[bool,int,float,str\],
(bool,int,float,str),
{"sample_bool":bool,"sample_int":int,"sample_float":float,"sample_str":str}

Document : list型,tuple型,dict型のいずれかを示すときに使う

list型に同じ型が並んでいる場合はfloat**s**のように略す表現もする

入れる配列が完全に固定している場合はfloat3と番号を後ろにつける表現もする

Example : sample_list=\[True,1,1.0,"text"\]
sample_tuple=(True,1,1.0,"text")
sample_dict={"checkBox":True,"radio":1,"param":1.0,"name":"window"}

sample_ints=\[2,3,5,7,11\]
sample_dicts=\[\{"name":"cube","value":1.0},{"name":"cone","value":2.5},{"name":"ball","value":5.2}\]
sample_float3=\[1.0,2.0,3.0\]

### オリジナル変数(original variable)

Document : インスタンス化した変数を示すときに使う

sample←これ=Sample()

Example : 
class Sample():
	def __init__(self):
		print("create original variable")

sample=Sample()

| フォルダ名定義 | longName | shortName |
| --- | --- | --- |
| ファルダ階層 | directory | dir |
| フォルダ名単体 | folder | folder |
| ファイル名 | file | file |
| 拡張子 | extension | ex |
| 階層+ファイル+拡張子(パス) | path | path |

| python名定義 | longName | shortName |
| --- | --- | --- |
| 実行 | execute | EX |
| ライブラリ | library | LB |
| UI実行(マネージャー) | manager | MN |
| 実行設定(オプション) | option | OP |
| ユーザーインターフェース | ui | UI |

