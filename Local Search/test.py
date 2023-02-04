import random
import math

# greedy_search テスト
SIZE = 5
MAP_SIZE = 100
data = [[random.randint(0,MAP_SIZE) for i in range(2)] for j in range(SIZE)]
data = [[((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5 for i in data] for j in data]

greedy_search(data, currentSolution=[0,1,2,3,4])


# multi_start_local_search テスト
SIZE = 5
MAP_SIZE = 100
data = [[random.randint(0,MAP_SIZE) for i in range(2)] for j in range(SIZE)]
data = [[((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5 for i in data] for j in data]

multi_start_local_search(data, start_point=10)


# simulated_annealing テスト
SIZE = 5
MAP_SIZE = 100
data = [[random.randint(0,MAP_SIZE) for i in range(2)] for j in range(SIZE)]
data = [[((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5 for i in data] for j in data]

simulated_annealing(data, currentSolution=[], steps=100, proba=0.5, c=0.9)


# tabu_search テスト
SIZE = 5
MAP_SIZE = 100
data = [[random.randint(0,MAP_SIZE) for i in range(2)] for j in range(SIZE)]
data = [[((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5 for i in data] for j in data]

tabu_search(data, currentSolution=[], steps=100, tabu_list_size=7)


# genetic_algorithm テスト
SIZE = 5
MAP_SIZE = 100
data = [[random.randint(0,MAP_SIZE) for i in range(2)] for j in range(SIZE)]
data = [[((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5 for i in data] for j in data]

genetic_algorithm(data, max_generation=10, solution_cnt=10)
