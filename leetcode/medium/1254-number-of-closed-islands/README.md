# Number of Closed Islands

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An  *island*  is a maximal 4-directionally connected group of `0s` and a  *closed island*  is an island  **totally**  (all left, top, right, bottom) surrounded by `1s.`

Return the number of  *closed islands*.

 

 **Example 1:** 

```
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
```

 **Example 2:** 

```
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

```

 **Example 3:** 

```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

```

 

 **Constraints:** 

- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <=1

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 84.01%)  
**Memory:** 20 MB (beats 53.53%)  
**Submitted:** 2026-10-25T12:24:42.468Z  

```py
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1:
                return True

            grid[r][c] = 1

            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)

            return left and right and up and down

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count

        
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-closed-islands/)