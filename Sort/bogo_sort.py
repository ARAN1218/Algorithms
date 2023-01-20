def bogo_sort(data):
    import random
    count = 0
    
    while True:
        random.shuffle(data) # ソート
        count += 1
        print("count:",count)

        flag = True
        for i in range(len(data)-1): # 確認
            if data[i] > data[i+1]:
                flag = False
                
        if flag: break
    
    return data # 揃ったら出力

  
# テスト
import random
data = [random.randint(0,10) for i in range(8)]
print(data)
print(bogo_sort(data))
print(sorted(data))
