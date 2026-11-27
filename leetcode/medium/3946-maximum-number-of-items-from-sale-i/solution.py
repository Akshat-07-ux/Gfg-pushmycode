class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)
        min_price = min(p for _, p in items)

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            fi, pi = items[i]
            if pi > budget:
                continue
            gain = 1 + sum(1 for j in range(n) if j != i and items[j][0] % fi == 0)
            for c in range(budget, pi - 1, -1):
                if dp[c - pi] != -1 and dp[c - pi] + gain > dp[c]:
                    dp[c] = dp[c - pi] + gain

        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                ans = max(ans, dp[c] + (budget - c) // min_price)

        return ans