# Minimum Changes for Beautiful Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a square matrix  **mat[][]**  **.**  A matrix is called beautiful if:

- In each column, there is at least one element that is equal to the sum of all other elements in that column (excluding itself).
- All these "beautiful numbers" (one from each column) must be in the same row.

Find the minimum number of operations needed to transform the matrix into a beautiful matrix. In one operation, you can increase or decrease any element by 1.

 **Examples:** 

```
Input: mat[][] = [[2, 4, 6], [1, 2, 3], [1, 2, 3]]
Output: 0
Explanation: No operation is required as first row contains all beautiful numbers.
```

```
Input: mat[][] = [[2, 4, 4], [1, 2, 3], [1, 2, 3]]
Output: 2
Explanation: In the first operation, increase mat[0][2] by 1, and in the second operation, increase mat[0][2] by 1 again. After these two operations, the matrix becomes beautiful, as the first row contains all beautiful numbers.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-19T07:20:46.449Z  

```py
class Solution:
    def minOperation(self, mat: list[list[int]]) -> int:
        # code here
        
        n = len(mat)
        col_s = [sum(mat[r][c] for r in range(n)) for c in range(n)]
        
        best = float("inf")
        for r in range(n):
            ops = 0
            
            for c in range(n):
                val = mat[r][c]
                rest = col_s[c] - val
                ops += abs(val - rest)
                
            if ops < best:
                best = ops
                
        return best
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/beautiful-matrix--130419/1)