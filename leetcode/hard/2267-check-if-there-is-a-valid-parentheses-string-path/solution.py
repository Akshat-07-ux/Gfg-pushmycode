class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(' or ( m + n - 1) % 2 != 0:
            return False

        namo = {}

        def df1(r, c, bal):
            if r == m or c == n:
                return False

            bal += 1 if grid[r][c] == '(' else -1

            if bal < 0:
                return False

            if r == m - 1 and c == n - 1:
                return bal == 0

            state = (r, c, bal)
            if state in namo:
                return namo[state]

            namo[state] = df1(r + 1, c, bal) or df1(r, c + 1, bal)

            return namo[state]

        return df1(0, 0, 0)