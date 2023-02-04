def multi_start_local_search(data, start_point=3):
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
    
    
    finalbestSolution = Solution([i for i in range(len(data))])
    for cnt in range(start_point):
        random.seed(cnt)
        bestSolution = [i for i in range(len(data))]
        random.shuffle(bestSolution)
        bestSolution = Solution(bestSolution)
        print(f"探索初期解：{bestSolution.solution}")
        while True:
            update = False
            currentNeighbors = getNeighbors(bestSolution.solution)
            for neighbor in currentNeighbors:
                if bestSolution.dist > neighbor.dist:
                    bestSolution = neighbor
                    update = True

            if not update: break
    
        print(f"探索解：{bestSolution.solution}, 探索価値：{bestSolution.dist}")
        if finalbestSolution.dist > bestSolution.dist:
            finalbestSolution = bestSolution
            
    print()
    print(f"探索最適解：{finalbestSolution.solution}, 探索最大価値：{finalbestSolution.dist}")
    return finalbestSolution.solution, finalbestSolution.dist
