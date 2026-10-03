# Coils in Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a positive integer n, consider a 4n  *4n matrix filled with integers from 1 to (4n)*  (4n) in row-major order (left to right, top to bottom). Form two coils from the matrix:

- The first coil starts from the top-left cell (0, 0) and spirals inward.
- The second coil starts from the bottom-right cell (4n - 1, 4n - 1) and spirals inward in the opposite direction.

Return these two coils in the same order.

 **Examples:** 

```
Input: n = 1
Output: [[1, 5, 9, 13, 14, 15, 11, 7], [16, 12, 8, 4, 3, 2, 6, 10]] 
Explanation: The matrix is 
 
So, the two coils are as given in the Output.
```

```
Input: n = 2
Output:
[[1, 9, 17, 25, 33, 41, 49, 57, 58, 59, 60, 61, 62, 63, 55, 47, 39, 31, 23, 15, 14, 13, 12, 11, 19, 27, 35, 43, 44, 45, 37, 29], 
 [64, 56, 48, 40, 32, 24, 16, 8, 7, 6, 5, 4, 3, 2, 10, 18, 26, 34, 42, 50, 51, 52, 53, 54, 46, 38, 30, 22, 21, 20, 28, 36]]  
Explanation:
 

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T12:34:20.639Z  

```py
class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        # code here
        m = 4 * n
        total = 8 * n * n
        
        coila = []
        
        r, c = 0, 0
        
        dir = 0
        
        
        steps = [m - 1]
        for step in range(m -2, 0, -2):
            steps.extend([step, step])
            
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        
        coila.append(r * m + c + 1)
        
        for step in steps:
            for _ in range(step):
                r += dr[dir]
                c+= dc[dir]
                
                coila.append(r * m + c + 1)
            dir = (dir + 1) % 4
            
        max_val = m * m + 1
        coilb = [max_val - val for val in coila]
        
        return [coila, coilb]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/form-coils-in-a-matrix4726/1)