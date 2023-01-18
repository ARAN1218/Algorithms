def linear_search(data, target):
    """線形探索
    dataの左から一つずつtargetと照合し、同じ要素であればその位置を返すアルゴリズム
    """
    
    for i in range(len(data)):
        if target == data[i]:
            return i
        
    return -1

        
# テスト
import random
data = [i for i in range(10)]
random.shuffle(data)
target = 5

print(data)
print(linear_search(data, target))
print(data[linear_search(data, target)])
