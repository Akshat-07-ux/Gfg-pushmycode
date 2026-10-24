# Minimum Travel Time

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an integer square matrix  **grid[][]**, where grid[i][j] represents the height of the cell (i, j).

- Initially, you are at cell (0, 0) and the value of t is 0.
- Every second, the value of t increases by 1.
- At any time t, you can move from a cell to any of its 4-directionally adjacent cells if the heights of both cells are less than or equal to t.
- Movement between valid cells is instantaneous.

Return the minimum value of t at which you can reach the cell (n - 1, n - 1).

 **Examples:** 

```
Input: grid[][] = [[0,2], [1,3]]
Output: 3
Explanation: At time t = 0, you are at cell (0, 0) and cannot move because all adjacent cells have a height greater than 0.
When t = 3, all cells on the path (0, 0) -> (1, 0) -> (1, 1) have heights at most 3, so you can reach the destination.
```

```
Input: grid[][] = [[0, 1, 2, 4], [12, 13, 14, 9], [15, 5, 11, 10], [3, 6, 7, 8]]
Output: 10
Explanation: The earliest time at which a path exists from (0, 0) to (3, 3) is t = 10. Before that, every possible path contains at least one cell with a height greater than the current value of t.
```

```
Input: grid [][] = [[0, 4, 5], [1, 2, 6], [7, 3, 8]]
Output: 8
Explanation: The path (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2) has maximum height 8. 
Therefore, the earliest time at which the destination can be reached is t = 8.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T06:22:03.802Z  

```py
import heapq
class Solution:
    def minTime(self, grid):
        # code here
        
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = [[False]* n for _ in range(n)]
        visited[0][0] = True
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            if r == n - 1 and c == n - 1:
                return t
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))
                    
        return 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-travel-time/1)