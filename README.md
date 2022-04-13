# Auto Scoring
フォルダに存在する 012_1116345678_masa_aa_Q1.c のようなC言語のコードをコンパイルし，実行してtxtファイルと比較する．  

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

