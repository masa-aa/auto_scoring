# Auto Scoring
フォルダに存在する 012_1116345678_masa_aa_Q1.c のようなC言語のコードをコンパイルし，実行してtxtファイルと比較する．  
    
## 全体の流れ
(1) .cのファイル名を012_1116345678_masa_aa_Q1.c → 1116345678_Q1.c に変更する．  
(2) Cのコードをコンパイルし1116345678.exeを生成する．  
(3) 1116345678.exeを実行し，結果を保存し，1116345678.exe を削除する．  
(4) .txt も同様に名前を変更し，(3)の結果と比較し，出力を保存する．  
  
## 環境について
Windows環境では問題なく動作することを確認したが，Linux，Macなどでは試してないためコマンドを直打ちしてる関係上動くかわからない．  
Linuxには対応する予定．

# 注意点など
## (1) rename
ファイル名を破壊的に変更する．

## (2) compile
以下明日書く
```cpp
int main() {
    SortedList<int> a = {1, 2, 1, 1, 4, 2};  
    cout << a[3] << endl; // 2  
    a.print(); // [1, 1, 1, 2, 2, 4]  
}
```
### コンストラクタ
```cpp
(1) SortedList<S> sl()
(2) SortedList<S> sl(vector<T> v)
(3) SortedList<S> sl(initializer_list<T> v)
``` 
* 比較可能な型 `T`
を定義する必要がある．

##### 計算量
$N$ を`v`の大きさとすると，$O(N\log(N))$ である．

### add
```cpp
void sl.add(T x)
```
`sl`に`x`を追加する．
##### 計算量
$O(\log(N))$ である．

### remove
```cpp
void sl.remove(T x)
```
`sl`から`x`を1つ削除する．
##### 制約
`sl`に`x`が存在する必要がある．存在しないと`x`より大きい最小の値を削除する．
##### 計算量
$O(\log(N))$ である．

### remove_if
```cpp
void sl.remove_if(T x)
```
`sl`に`x`が存在すれば，`sl`から`x`を1つ削除する．

##### 計算量
$O(\log(N))$ である．

### pop
```cpp
T sl.pop()
T sl.pop(int k)
```
`sl`の`k`番目を削除し取得する．`k`を指定しない時，一番大きい要素を1つ削除し取得する．

##### 計算量
$O(\log(N))$ である．

### bisect_left
```cpp
int sl.bisect_left(T x)
```
`x`以上で最小の数が何番目かを返す．つまり`x`未満の数が何個あるかわかる．

