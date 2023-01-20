def heap_sort(data):
    # array[n]をヒープ構成部(0～n-1)の最適な位置へ移動
    def upheap(array, n):
        while n != 0: # 最大値になったらやめる
            parent = int((n - 1) / 2)
            if array[n] > array[parent]: # 親より大きな値の場合スワップ
                array[n], array[parent] = array[parent], array[n]
                n = parent # 交換後のインデックスを保持
            else:
                break

    # ルート[0]をヒープ(0～n)の最適な位置へ移動
    def downheap(array, n):
        if n == 0: return
        parent = 0
        while True:
            child = 2 * parent + 1 # array[n]の子要素
            if child > n: break
            
            if (child < n) and array[child] < array[child + 1]:
                child += 1
            if array[parent] < array[child]: # 子要素より小さい場合スワップ
                array[child], array[parent] = array[parent], array[child]
                parent = child # 交換後のインデックスを保持
            else:
                break
    
    # ヒープソート開始
    i = 0
    while(i < len(data)):
        # ヒープを構成
        upheap(data, i)
        i += 1

    while(i > 1):
        # ヒープから最大値を取り出し、一番後ろの要素と交換する
        i -= 1
        data[i], data[0] = data[0], data[i]

        # ヒープの再構成
        downheap(data, i-1)

    return data

  
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(heap_sort(data))
print(sorted(data))
