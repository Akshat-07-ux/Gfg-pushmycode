class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[float('inf')] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_changes = float('inf')

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0
                        for offset in range(d):
                            l = i + offset
                            r = j - d + 1 + offset
                            while l < r:
                                if s[l] != s[r]:
                                    changes += 1
                                l += d
                                r -= d

                        min_changes = min(min_changes, changes)
                cost[i][j] = min_changes

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for p in range(j - 1, i):
                    if j == 1:
                        dp[i][j] = cost[0][i - 1]
                    else:
                        dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]