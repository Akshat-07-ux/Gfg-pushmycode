# Geek Village and Wells

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a matrix  **mat[][]**  of size n × m representing Geek's village, where:

- 'H' represents a House.
- 'W' represents a Well.
- '.' represents Open Ground.
- 'N' represents a Restricted Area that cannot be entered.

Every house needs water from a well. For each house, find the minimum distance required to reach the nearest well and return back to the same house.

A person can move only in four directions: up, down, left, and right. Movement outside the matrix and entering a restricted cell ('N') is not allowed, however a person can move through an open ground ('.') and another house ('H').

Return a matrix of the same size as mat[][] where:

- For every house ('H'), store the minimum round-trip distance to the nearest reachable well.
- If a house cannot reach any well, store -1.
- For every well ('W'), open ground ('.'), and restricted cell ('N'), store 0.

 **Examples :** 

```
Input: n = 3, m = 3, mat[][] = [[H, H, H], [H, W, H], [H, H, H]]
Output: [[4, 2, 4], [2, 0, 2], [4, 2, 4]]
Explanation: The only well is at the center of the grid. The answer for each house is the round-trip distance: 2 * distance to well. 
```

```
Input: n = 4, m = 5, mat[][] = [[H, N, H, N, H], [N, N,., H, W], [W, H, H, H,.], [H,.,., N, H]]
Output: [[-1, 0, 6, 0, 2], [0, 0, 0, 2, 0], [0, 2, 4, 4, 0], [2, 0, 0, 0, 4]] 
Explanation: There are two wells in the grid. For each house, the minimum distance to reach the nearest well and return back is calculated. The answer is 2 * shortest distance to the well. Cells containing N,., and W have value 0. The house at (0, 0) cannot reach any well due to blocked paths, so its value is -1. 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T07:03:12.167Z  

```py
from collections import deque
class Solution:
    def geeksAndWells(self, mat: list[list[str]]) -> list[list[int]]:
        # code here
        
        n, m, q, d = len(mat), len(mat[0]), deque(), {}
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'W':
                    q.append((r, c));
                    d[(r, c)] = 0
                    
        while q:
            r, c = q.popleft()
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] != 'N' and (nr, nc) not in d:
                    d[(nr, nc)] = d[(r, c)] + 1
                    q.append((nr, nc))
                    
        return [[-1 if mat[r][c] == 'H' and (r, c) not in d else d.get((r, c), 0) * 2 if mat[r][c] == 'H' else 0 for c in range(m)] for r in range(n)]
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geeks-village-and-wells--170647/1)