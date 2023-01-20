def pigeonhole_sort(data, left, right):
    size = right - left + 1 # データ内の最小値・最大値がなければ、このソートは使えない
    pigeonholes = [0] * size # 度数分布のリストをゼロで初期化
  
    for x in data:
        pigeonholes[x - left] += 1 # 出現回数の計算

    i = 0
    for count in range(size):
        while pigeonholes[count] > 0:
            pigeonholes[count] -= 1
            data[i] = count + left # 最小値+保管座標で値を特定
            i += 1
            
    return data
  
  
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
min_value = min(data)
max_value = max(data)
print(data)
print(pigeonhole_sort(data, min_value, max_value))
print(sorted(data))
