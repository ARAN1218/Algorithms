def shaker_sort(data):
    start = 0
    end = len(data)-1
    
    while start <= end:
        flag = True
        
        for i in range(start, end): # 左から右
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                flag = False
                
        end -= 1
        
        for i in range(end, start, -1): # 右から左
            if data[i-1] > data[i]:
                data[i], data[i-1] = data[i-1], data[i]
                flag = False

        start += 1
        
        if flag: return data
    
    
# テスト
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(shaker_sort(data))
print(sorted(data))
