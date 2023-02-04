def simulated_annealing(data, currentSolution=[], steps=100, proba=0.1, c=0.9):
    # TSPの解のクラス
    class Solution:
        def __init__(self, solution):
            self.solution = solution
            self.dist = sum([data[solution[s]][solution[s+1]] for s in range(len(solution)-1)]) + data[solution[0]][solution[-1]]

        def copy(self):
            return Solution(self.solution)
    
    # 近傍解を求める
    def getNeighbors(solution):
        neighbors = []
        for i in range(len(solution)):
            for j in range(i, len(solution)):
                neighbor = solution.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbor = Solution(neighbor)
                neighbors.append(neighbor)
        return neighbors
    
    # 探索開始
    step = 0
    bestSolution = Solution(currentSolution) if currentSolution else Solution([i for i in range(len(data))])
    cneighbor = bestSolution.copy()
    while step <= steps:
        currentNeighbors = getNeighbors(cneighbor.solution)
        cneighbor = currentNeighbors[0]
        for neighbor in currentNeighbors:
            if cneighbor.dist > neighbor.dist:
                cneighbor = neighbor
                #print(f"ようこそ:{neighbor.solution}:{neighbor.dist}:{1/(1+np.exp((bestSolution.dist-neighbor.dist)/0.05/(bestSolution.dist-neighbor.dist+100)**2))}:{proba}")
            elif 1/(1+math.exp((bestSolution.dist-neighbor.dist+100)/0.05/(bestSolution.dist-neighbor.dist+100)**2)) < proba:
                cneighbor = neighbor
                #print(f"確率が作動！:{neighbor.solution}:{neighbor.dist}:{1/(1+math.exp((bestSolution.dist-neighbor.dist)/0.05/(bestSolution.dist-neighbor.dist+100)**2))}:{proba}")
                proba *= c # probaを冷却する
                
            if bestSolution.dist > cneighbor.dist:
                bestSolution = cneighbor
                #print("改善なう")
                step = 0
        
        step += 1
    
    return bestSolution.solution, bestSolution.dist
            
