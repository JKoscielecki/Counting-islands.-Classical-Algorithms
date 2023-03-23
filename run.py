from island_counter import IslandCounter

M = 5
N = 5
matrix = [[1, 1, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 1, 1]]


counter = IslandCounter(M, N, matrix)
print(counter.count_islands())
