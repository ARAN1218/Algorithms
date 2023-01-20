def quick_sort(data):
    # 基準点を決める(今回の例ではデータの真ん中にある点)
    left, right, middle = [], [], []
    pivot = data[len(data)//2]
    
    # 基準点より小さいものはleft、大きいものはright、同じものはmiddleに入れていく
    for i in range(len(data)):
        if data[i] < pivot: # 基準点より小さい
            left.append(data[i])
        elif pivot < data[i]: # 基準点より大きい
            right.append(data[i])
        else:
            middle.append(data[i])
            
    # left, rightはそれぞれquick_sortを再帰し、それぞれで揃えたものを用意する
    if left:
        left = quick_sort(left)
    if right:
        right = quick_sort(right)

    return left + middle + right

  
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(quick_sort(data))
print(sorted(data))
