import sys

sys.setrecursionlimit(200000)

class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        
        dp = [[-1] * m for _ in range(n)]
        
        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
                
            max_len = 1
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
                    
            dp[r][c] = max_len
            return dp[r][c]
            
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
                
        return ans
