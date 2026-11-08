class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        row_c = [0] * rows
        col_c = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_c[r] += 1
                    col_c[c] += 1

        com_ser = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if row_c[r] > 1 or col_c[c] > 1:
                        com_ser += 1

        return com_ser