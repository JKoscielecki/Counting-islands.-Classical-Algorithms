class IslandCounter:
    def __init__(self, M, N, matrix):
        self.M = M
        self.N = N
        self.matrix = matrix
        self.visited = [[False for _ in range(N)] for _ in range(M)]
        self.island_count = 0

    def dfs(self, row, col):
        if row < 0 or row >= self.M or col < 0 or col >= self.N or self.visited[row][col] or self.matrix[row][col] == 0:
            return

        self.visited[row][col] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            self.dfs(row + dr, col + dc)


    def count_islands(self):
        for row in range(self.M):
            for col in range(self.N):
                if self.matrix[row][col] == 1 and not self.visited[row][col]:
                    self.dfs(row, col)
                    self.island_count += 1

        return self.island_count
