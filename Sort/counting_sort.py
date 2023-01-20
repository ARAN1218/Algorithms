def counting_sort(data, max_value):
    size = max_value + 1 # データ内の最小値・最大値がなければ、このソートは使えない
    count = [0] * size # 度数分布のリストをゼロで初期化
    for a in data:
        count[a] += 1 # 出現回数の計算
    i = 0
    for a in range(size): # 値の最大値まで繰り返す
        for c in range(count[a]): # 値の出現回数だけ繰り返して元のリストに値をコピーする
            data[i] = a
            i += 1
    return data

  
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
max_value = max(data)
print(data)
print(counting_sort(data, max_value))
print(sorted(data))
