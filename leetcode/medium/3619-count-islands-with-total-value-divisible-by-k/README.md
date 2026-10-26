# Count Islands With Total Value Divisible by K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an `m x n` matrix `grid` and a positive integer `k`. An  **island**  is a group of  **positive**  integers (representing land) that are  **4-directionally**  connected (horizontally or vertically).

The  **total value**  of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value  **divisible by**  `k`.

 

 **Example 1:** 

 **Input:**  grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

 **Output:**  2

 **Explanation:** 

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

 **Example 2:** 

 **Input:**  grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

 **Output:**  6

 **Explanation:** 

The grid contains six islands, each with a total value that is divisible by 3.

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 105
- 0 <= grid[i][j] <= 106
- 1 <= k <= 106

## Solution

**Language:** Python  
**Runtime:** 253 ms (beats 95.52%)  
**Memory:** 30.6 MB (beats 87.93%)  
**Submitted:** 2026-10-26T03:25:29.596Z  

```py
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    current_sum = 0
                    stack = [(r, c)]

                    current_sum += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        curr_r, curr_c = stack.pop()

                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0,1)]:
                            nr, nc = curr_r + dr, curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                current_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if current_sum % k == 0:
                        count += 1
        return count   
```

---

[View on LeetCode](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/)