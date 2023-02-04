def tabu_search(data, currentSolution=[], steps=100, tabu_list_size=7):
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
                if neighbor.solution not in tabu_list:
                    neighbors.append(neighbor)
        return neighbors
    
    # タブーリストに追加する関数
    def tabu_list_append(solution):
        if len(tabu_list) == tabu_list_size: # タブーリストが満タン
            tabu_list.pop(0)
            tabu_list.append(solution)
        else:
            tabu_list.append(solution)
    
    # 探索開始
    step = 0
    tabu_list = []
    bestSolution = Solution(currentSolution) if currentSolution else Solution([i for i in range(len(data))])
    cneighbor = bestSolution.copy()
    while step < steps:
        currentNeighbors = getNeighbors(cneighbor.solution)
        cneighbor = currentNeighbors[0]
        for neighbor in currentNeighbors:
            if cneighbor.dist > neighbor.dist and neighbor.solution not in tabu_list:
                cneighbor = neighbor
                tabu_list_append(cneighbor.solution)
        
        if bestSolution.dist > cneighbor.dist:
            bestSolution = cneighbor
            step = 0
            
        step += 1
            
    return bestSolution.solution, bestSolution.dist
