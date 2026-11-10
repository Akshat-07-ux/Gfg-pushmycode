class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            c = costs[i - 1]
            for j in range(max(0, i - 3), i):
                dp[i] = min(dp[i], dp[j] + c + (i - j) ** 2)

        return dp[n]