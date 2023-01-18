def insert_sort(data):
    """挿入ソート
    左から順にデータを適切な位置に交換していくアルゴリズム
    """
    for i in range(len(data)-1):
        for j in range(i,len(data)): # 最小値を見つけ次第すぐに交換する
            if data[i] > data[j]: data[i], data[j] = data[j], data[i]
        
    return data

  
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(insert_sort(data))
print(sorted(data))
