def bubble_sort(data):
    flag = True
    while flag:
        flag = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                flag = True
    
    return data

  
# ใในใ
import random
data = [random.randint(0,10) for i in range(10)]
print(data)
print(bubble_sort(data))
print(sorted(data))
