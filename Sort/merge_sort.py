def merge_sort(data):
    # データが一つしかない時、分割不可能であるので終了
    if len(data) <= 1:
        return data
    
    # データを細かく半分ずつ分けていく(分割統治法)
    left = merge_sort(data[:len(data)//2])
    right = merge_sort(data[len(data)//2:])
    
    # (データ数が小さい方から)マージ
    # leftとrightの要素を比較して、小さい方からmergeに入れていく
    merge, l, r = [], 0, 0
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            merge.append(left[l])
            l += 1
        else:
            merge.append(right[r])
            r += 1
    
    # 比較にあぶれた余りを入れる
    if l < len(left):
        merge.extend(left[l:])
    elif r < len(right):
        merge.extend(right[r:])
            
    return merge

  
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(merge_sort(data))
print(sorted(data))
