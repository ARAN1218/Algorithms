def multi_start_local_search(data, max_weight, start_point=3):
    # 近傍解を求める
    def getNeighbors(solution):
        neighbors = []
        for i in range(len(solution)):
                neighbor = solution.copy()
                neighbor[i] = 1 if neighbor[i]==0 else 0
                neighbors.append(neighbor)
        return neighbors
    
    
    finalbestSolution, finalbestValue = 0, 0
    for cnt in range(start_point):
        random.seed(cnt)
        bestSolution = [random.randint(0,1) for i in range(len(data))]
        bestValue = 0
        print(f"探索初期解：{bestSolution}")
        while True:
            update = False
            currentNeighbors = getNeighbors(bestSolution)
            for neighbor in currentNeighbors:
                neighborWeight = sum([item[0] for i,item in enumerate(data) if neighbor[i] == 1])
                neighborValue = sum([item[1] for i,item in enumerate(data) if neighbor[i] == 1])
                if neighborWeight <= max_weight and bestValue < neighborValue:
                    bestSolution = neighbor.copy()
                    bestValue = neighborValue
                    update = True

            if not update: break
    
        print(f"探索解：{bestSolution}, 探索価値：{bestValue}")
        if finalbestValue < bestValue:
            finalbestSolution = bestSolution.copy()
            finalbestValue = bestValue
            
    print()
    print(f"探索最適解：{finalbestSolution}, 探索最大価値：{finalbestValue}")
    return finalbestSolution, finalbestValue

  
# テスト
import random
# 品物i：(重さw, 価値v)
data = [(10,10), (20,20), (30,30), (40,10)]
#data = [(10,10), (20,20), (30,30), (40,100)]
max_weight = 50

print(data)
multi_start_local_search(data, max_weight, start_point=3)
