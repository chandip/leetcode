"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or
reflected) to equal the other
"""


class DistinctIsland:
    def __init__(self, grid):
        self.distinct_island = set()
        self.grid = grid

    def num_island(self):
        if not self.grid:
            return 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    path = []
                    self.dfs(i, j, path, "X")
                    self.distinct_island.add(''.join(path))
        return self.distinct_island

    def dfs(self, i, j, path, direction):
        path.append(direction)
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] != 1:
            return
        self.grid[i][j] = 0
        self.dfs(i + 1, j, path, "D")
        self.dfs(i - 1, j, path, "U")
        self.dfs(i, j + 1, path, "R")
        self.dfs(i, j - 1, path, "L")


island = [
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 1, 1],
]
print(DistinctIsland(island).num_island())
