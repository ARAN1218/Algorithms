# Algorithms
数理最適化に関するアルゴリズムをPythonで一から実装します。  
また、PythonのTkinterライブラリを用いてアルゴリズム可視化アプリを作成します。

## Reference
### Sort
- Selection sort (選択ソート)
- Insertion sort (挿入ソート)
- Bubble sort (バブルソート)
- Shaker sort (シェーカーソート)
- Quick sort (クイックソート)
- Merge sort (マージソート)
- Heap sort (ヒープソート)
- Counting sort (分布数えソート)
- Pigeonhole sort (鳩の巣ソート)
- Radix sort(LSD)
- Bogo sort (ボゴソート)


### Global Search
- Linear search (線形探索)
- Binary search (二分探索)
- Breadth first search (幅優先探索)
- Depth first search (深さ優先探索)
- Branch-and-bound method (分枝限定法)
- Dynamic programming (動的計画法)


### Local Search
- Greedy search (貪欲探索)
- Multi-start local search (多開始局所探索)
- Simulated annealing (シミュレーテッドアニーリング(焼きなまし法))
- Tabu search (タブーサーチ)
- Genetic algorithms (遺伝的アルゴリズム)


## アルゴリズム可視化アプリ(仮称：Algos App)について
アルゴリズムの可視化を行うアプリで、各種アルゴリズムの勉強やリラックスに利用することができるアプリ。

このアプリはホーム画面から選べる以下の３つの機能で構成される。
1. Sort
  - ランダムな長さの棒を各種アルゴリズムでソートする様子を可視化する。

2. Global Search
  - 迷路を穴掘り法によってランダムに構築し、スタートからゴールまでの最短ルートを探索する様子を可視化する。

3. Heuristics
  - 最適解が円形になる巡回セールスマン問題に対し、一定時間メタヒューリスティクスで探索する様子を可視化する。
  - 必ず線が円形に結ばれるとは限らないため、リラックス効果は薄いかも


※GithubのReleases機能からダウンロードしたexeファイルは開発元が不明だと言われて開けない可能性がある。以下の手順でwindows・macから開くことが可能になる。  

windows： https://www.memorou.com/2016/05/exe.html  
mac： https://support.apple.com/ja-jp/guide/mac-help/mh40616/mac


