"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water

Count the number of islands.
"""


class NumIsland:
    def __init__(self, grid):
        self.grid = grid

    def count_island(self):
        if not self.grid:
            return 0
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.dfs(i, j, "start")
                    count += 1
        return count

    def dfs(self, i, j, text):
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] != 1:
            return
        self.grid[i][j] = 0
        self.dfs(i + 1, j, "going down")
        self.dfs(i - 1, j, "going up")
        self.dfs(i, j + 1, "going right")
        self.dfs(i, j - 1, "going left")


island = [
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, 1],
]

print(NumIsland(island).count_island())
