def greedy_search(data, currentSolution=[]):
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
    bestSolution = Solution(currentSolution) if currentSolution else Solution([i for i in range(len(data))])
    while True:
        update = False
        currentNeighbors = getNeighbors(bestSolution.solution)
        for neighbor in currentNeighbors:
            if bestSolution.dist > neighbor.dist:
                bestSolution = neighbor
                update = True
                
        if not update: return bestSolution.solution, bestSolution.dist
