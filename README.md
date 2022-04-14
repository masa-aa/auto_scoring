# Auto Scoring
フォルダに存在する 012_1116345678_masa_aa_Q1.c のようなC言語のコードをコンパイルし，実行してtxtファイルと比較する．  
    
## 全体の流れ
(1) .cのファイル名を012_1116345678_masa_aa_Q1.c → 1116345678_Q1.c に変更する．  
(2) Cのコードをコンパイルし1116345678.exeを生成する．  
(3) 1116345678.exeを実行し，結果を保存し，1116345678.exe を削除する．  
(4) .txt も同様に名前を変更し，(3)の結果と比較し，出力を保存する．  

```python:main.py
from auto_scoring import all_execution, equal

# 実行まで
outputs = all_execution(folder="sample_c", arg="2 2", save="sample.txt")
# 比較
equal(folder="sample_txt", outputs=outputs, save="sample_equal.txt")

```
## 環境について
Windows環境では問題なく動作することを確認したが，Linux，Macなどでは試してないためコマンドを直打ちしてる関係上動くかわからない．  
Linuxには対応する予定．

## コード配置
カレントディレクトリに以下を配置する． 
* `auto_scoring.py`
* `main.py`のような実行ファイル
* C のファイル群があるフォルダ
* txt のファイル群があるフォルダ


## 方針
正解ではないコード(である可能性があるもの)を見つけ出すことが目的であるため，不正解と判定されたコードは各自実行しなおすこと．  
逆に正解と判定されたコードは正解である可能性が限りなく高いので実行する必要がない．

# 注意点
## (1) rename
ファイル名を破壊的に変更する．  
ファイル名の区切り文字`/`と`\`を区別してるため，Windows環境ではないところではこれでバグるかも．

## (2) compile
Pythonのsubprocessを用いてCのコードをコンパイルする．  
コンパイラはgccを用いている．  
そのため，gccをインストールか，`auto_scoring.py`の`output(filename)`の以下のように変更する必要がある．
```python
# gcc 
f"gcc {filename} -o {ID}.exe"

# 例えば Visual Studio 
f"cl {filename} -o {ID}.exe"
```

## (3) execute
全体的にエラー名は適当がちである．  
無限ループは未対応なため`Ctrl + C`で止める.  
(色々試してもダメだった．timeoutの方法教えてほしい)  
Linux だと以下のように変更する必要がある.(かも)
```python
# Windows
subprocess.run(f"del {ID}.exe", shell=True)

# Linux
subprocess.run(f"rm {ID}.exe", shell=True)
```

## (4) compare
改行文字とスペースを無視して比較する．  
エラーが出てる場合はそのエラー名を出力する．  
文字コードや表記揺れの可能性があるため一致判定が`False`で返ってきても信用してはならない．


