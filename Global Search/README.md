# Global Search
全探索アルゴリズムをPythonで実装します。

## References
### Linear search(線形探索)
dataの左から一つずつtargetと照合し、同じ要素であればその位置を返すアルゴリズム

### Binary search(二分探索)
予めソートしたdataを二分割していき、targetがその中点より大きければ右、小さければ左を探索していくアルゴリズム

### Depth first search(深さ優先探索)
木構造のデータ探索を行うアルゴリズムの一種
- 最後（最も最近）に追加された候補を優先的に探索するLIFO（Last-In First-Out）方式で次に進むノードを決定する。
- 探索候補ノードの記録にはスタック（stack）というデータ構造が適している。

### Breadth first search(幅優先探索)
木構造のデータ探索を行うアルゴリズムの一種
- 最初（最も過去）に追加された候補を優先的に探索するFIFO（First-In First-Out）方式で次に進むノードを決定する。
- 探索候補ノードの記録にキュー（queue）というデータ構造が適している。

### Branch-and-bound method(分枝限定法)


### Dynamic programming(動的計画法)
