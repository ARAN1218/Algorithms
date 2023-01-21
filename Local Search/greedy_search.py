def greedy_search(data, max_weight, currentSolution=[]):
    # 近傍解を求める
    def getNeighbors(solution):
        neighbors = []
        for i in range(len(solution)):
                neighbor = solution.copy()
                neighbor[i] = 1 if neighbor[i]==0 else 0
                neighbors.append(neighbor)
        return neighbors
    
    bestSolution = currentSolution if currentSolution else [0 for i in range(len(data))]
    bestValue = 0
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
                
        if not update: return bestSolution,bestValue

        
# テスト
import random
# 品物i：(重さw, 価値v)
data = [(10,10), (20,20), (30,30), (40,10)]
#data = [(10,10), (20,20), (30,30), (40,100)]
max_weight = 50

print(data)
greedy_search(data, max_weight, currentSolution=[0,0,0,0])
