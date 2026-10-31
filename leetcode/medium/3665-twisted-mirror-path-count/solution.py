class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        MOD = 10**9 + 7

        dp = [[0] *2 for _ in range(n + 1)]
        dp[1] = [1, 1]

        for r in range(len(grid)):
            for c in range(n):
                if grid[r][c]:
                    dp[c + 1 ] = [dp[c + 1][1], dp[c][0]]
                else:
                    val = (dp[c + 1][1] + dp[c][0]) % MOD

                    dp[c + 1] = [val, val]

        return dp[-1][0]