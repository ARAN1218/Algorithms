def genetic_algorithm(data, max_generation=10, solution_cnt=10):
    # TSPの解のクラス
    class Solution:
        def __init__(self, solution):
            self.solution = solution
            self.dist = sum([data[solution[s]][solution[s+1]] for s in range(len(solution)-1)]) + data[solution[0]][solution[-1]]

        def copy(self):
            return Solution(self.solution)

    # 選択(ルーレット方式)
    def select_roulette(solutions):
        selected = []
        total_dist = sum([1/solution.dist for solution in solutions]) # 小さい方がいいので、逆数を取る
        norm_weights = [(1/solution.dist) / total_dist for solution in solutions]
        selected = random.choices(solutions, k=len(solutions), weights=norm_weights)
        print(f"選択(ルーレット方式)：{[s.solution for s in selected]}")
        return selected
    
    # 選択(トーナメント方式)
    def select_tournament(solutions):
        selected = []
        for i in range(len(generation)):
            tournament = random.choices(generation, 3, replace=False)
            max_genom = max(tournament, key=Individual.get_fitness).genom.copy()
            selected.append(Individual(max_genom))
        return selected
    
    # 選択(エリート方式)
    def select_elite(solutions):
        selected = []
        return selected
    
    # 交叉(2点交叉)
    # ある2点を選び、その間の配列を模倣するように現在の解を並び替える
    def crossover(solutions):
        selected = solutions.copy()
        children = []
        if solution_cnt % 2:
            selected.append(selected[0])
        for child1, child2 in zip(selected[::2], selected[1::2]):
            # 一定の確率で交叉を適用
            if random.randint(0,100) < 10: # 10%の確率で交叉する
                child1, child2 = cross_two_point_copy(child1, child2)
            children.append(child1)
            children.append(child2)
        children = children[:solution_cnt]
        print(f"交叉(2点交叉)：{[s.solution for s in children]}")
        return children
    
    def cross_two_point_copy(child1, child2):
        c_children = [child1, child2]
        for c_ind in range(len(c_children)):
            ind1, ind2 = random.randint(0,len(data)-1), random.randint(0,len(data)-1)
            ind1, ind2 = (ind2, ind1) if ind1 > ind2 else (ind1, ind2) # ind1, ind2の大きさ順にする
            for ind in range(ind1, ind2+1):
                r_value = c_children[1-c_ind].solution[ind]
                c_children[c_ind].solution[ind], c_children[c_ind].solution[c_children[c_ind].solution.index(r_value)] = c_children[c_ind].solution[c_children[c_ind].solution.index(r_value)], c_children[c_ind].solution[ind]
                
        return c_children[0].copy(), c_children[1].copy()
        
    
    # 突然変異
    def mutate(solutions):
        for i in range(len(solutions)):
            if random.randint(0,100) < 5: # 5%の確率で突然変異する
                print(f"突然変異発生！：{[s.solution for s in solutions]}", end="")
                ind1 = random.randint(0,len(data)-1)
                ind2 = random.randint(0,len(data)-1)
                solutions[i].solution[ind1], solutions[i].solution[ind2] = solutions[i].solution[ind2], solutions[i].solution[ind1]
                solutions[i] = solutions[i].copy()
                print(f"{[s.solution for s in solutions]}")
                
        return solutions
    
    # 初期解をsolution_cnt個だけ作成する
    solutions = [random.sample([i for i in range(len(data))], len(data)) for s in range(solution_cnt)]
    solutions = [Solution(solution) for solution in solutions]
    # 選択→交叉→突然変異の順に処理していく
    for generation in range(max_generation):
        print("サイクル")
        # 選択
        solutions = select_roulette(solutions)
        # 交叉
        solutions = crossover(solutions)
        # 突然変異
        solutions = mutate(solutions)
        
    # 最適解を選ぶ
    finalValues = [solution.dist for solution in solutions]
    bestindex = finalValues.index(min(finalValues))
    return solutions[bestindex].solution, solutions[bestindex].dist
    
