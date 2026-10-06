# Longest Increasing Path in Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a matrix with  **n**  rows and  **m** columns. Your task is to find the length of the longest path in with the following constraints

- The values in path strictly increasing.  For example if a path of length k has values a1, a2, a3,.... ak , then for every i from [2, k] this condition must hold ai > ai-1. 
- No cell should be revisited in the path.
- From each cell,  you can move in any of of the four directions: left, right, up, or down.
- You are not allowed to move diagonally or move outside the boundary.

 **Examples**  **:** 

```
Input: n = 3, m = 3, matrix[][] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: 5
Explanation: One such path is 1 -> 2 -> 3 -> 6 -> 9, where each number is strictly greater than the previous.

```

```
Input: n = 3, m = 3, matrix[][] = [[3, 4, 5], [6, 2, 6], [2, 2, 1]]
Output: 4
Explanation: One of the longest increasing paths is 3 -> 4 -> 5 -> 6.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T06:15:38.711Z  

```py
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

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1)