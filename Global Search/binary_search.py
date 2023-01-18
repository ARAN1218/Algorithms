def binary_search(data, target):
    """二分探索
    予めソートしたdataを二分割していき、targetがその中点より大きければ右、小さければ左を探索していくアルゴリズム
    """
    
    data = sorted(data)
    start = 0
    end = len(data)-1
    while start <= end:
        mid_point = (start + end) // 2

        if data[mid_point] == target: # 見つかった時
            return mid_point
        elif data[mid_point] < target: # 中央値より大きい時
            start = mid_point+1
        else: # 中央値より小さい時
            end = mid_point-1
        
    return -1 # 見つからなかった時
            
    
# テスト
import random
data = [i for i in range(10)]
random.shuffle(data)
target = 1

print(data)
print(binary_search(data, target))
data = sorted(data)
print(data)
print(data[binary_search(sorted(data), target)])
