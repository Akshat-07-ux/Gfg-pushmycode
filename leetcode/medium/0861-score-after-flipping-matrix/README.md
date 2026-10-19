# Score After Flipping Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an `m x n` binary matrix `grid`.

A  **move**  consists of choosing any row or column and toggling each value in that row or column (i.e., changing all `0`'s to `1`'s, and all `1`'s to `0`'s).

Every row of the matrix is interpreted as a binary number, and the  **score**  of the matrix is the sum of these numbers.

Return  *the highest possible  **score**  after making any number of  **moves**  (including zero moves)*.

 

 **Example 1:** 

```
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

```

 **Example 2:** 

```
Input: grid = [[0]]
Output: 1

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- grid[i][j] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 24.37%)  
**Memory:** 19.2 MB (beats 66.67%)  
**Submitted:** 2026-10-19T05:29:48.915Z  

```py
class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        for j in range(1, n):
            ones_count = sum(grid[i][j] for i in range(m))

            if ones_count < m - ones_count:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        
        score = 0
        for i in range(m):
            row_value = 0
            for j in range(n):
                row_value = (row_value << 1) | grid[i][j]

            score += row_value

        return score
```

---

[View on LeetCode](https://leetcode.com/problems/score-after-flipping-matrix/)