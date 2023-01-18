def selection_sort(data):
    """選択ソート
    dataの最小値を線形探索し、それを左に埋めてくことでソートするアルゴリズム
    """
    
    for i in range(len(data)-1):
        min_index = i
        for j in range(i,len(data)):
            if data[min_index] > data[j]: # 最小値を求める
                min_index = j
        data[min_index], data[i] = data[i], data[min_index] # 最小値と交換
        
    return data



# テスト
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(selection_sort(data))
print(sorted(data))
