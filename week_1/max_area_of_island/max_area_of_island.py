from typing import List


class Solution:
    max_island = int()
    grid_seen = list(list())

    def _maxAreaHelper(self, grid: List[List[int]], row: int, col: int) -> int:
        if grid[row][col] == 0:
            return 0
        if self.grid_seen[row][col]:
            return 0
        self.grid_seen[row][col] = True
        up = left = down = right = 0
        up = self._maxAreaHelper(grid, row - 1, col) if row - 1 >= 0 else 0
        left = self._maxAreaHelper(grid, row, col - 1) if (col - 1) >= 0 else 0
        down = self._maxAreaHelper(grid, row + 1, col) if (row + 1) < len(grid) else 0
        right = self._maxAreaHelper(grid, row, col + 1) if (col + 1) < len(grid[row]) else 0
        return 1 + up + left + down + right

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid_seen = [[False] * len(grid[0]) for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if self.grid_seen[row][col]:
                    continue
                if grid[row][col]:
                    area = self._maxAreaHelper(grid, row, col)
                    if area > self.max_island:
                        self.max_island = area
                else:
                    self.grid_seen[row][col] = True
        return self.max_island
