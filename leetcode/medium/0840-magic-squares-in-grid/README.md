# Magic Squares In Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A `3 x 3`  **magic square**  is a `3 x 3` grid filled with distinct numbers  **from** 1 **to** 9 such that each row, column, and both diagonals all have the same sum.

Given a `row x col` `grid` of integers, how many `3 x 3` magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain numbers up to 15.

 

 **Example 1:** 

```
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.

```

 **Example 2:** 

```
Input: grid = [[8]]
Output: 0

```

 

 **Constraints:** 

- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 10
- 0 <= grid[i][j] <= 15

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 43.70%)  
**Memory:** 19.4 MB (beats 53.94%)  
**Submitted:** 2026-09-29T07:29:08.837Z  

```py
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
            
        def is_magic(r, c):
            nums = []
            for i in range(3):
                for j in range(3):
                    nums.append(grid[r + i][c + j])
            
            if sorted(nums) != list(range(1, 10)):
                return False
                
            # Check rows
            if grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15: return False
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15: return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15: return False
            
            # Check columns
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15: return False
            
            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False
            
            return True

        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1
                    
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/magic-squares-in-grid/)