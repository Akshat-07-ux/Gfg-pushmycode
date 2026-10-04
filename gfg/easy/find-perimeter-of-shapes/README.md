# Perimeter of Shapes in Binary Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary matrix  **mat[][]**  of size  **n × m**, where each cell contains either  **0**  or  **1**, find the total perimeter of all figures formed by cells containing  **1s**. Two cells are considered adjacent if they share a common side.

A single cell containing 1 has a perimeter of 4, whereas two adjacent cells containing 1 (i.e., 11) together have a perimeter of 6.

 

 **Examples :** 

```
Input: mat[][] = [[0,1,0,0,0], [1,1,1,0,0], [1,0,0,0,0]]
Output: 12
Explanation: The five cells form a single figure. Hence, the perimeter of the figure is 12.     

```

```
Input: mat[][] = [[1,0], [1,1]]
Output: 8
Explanation: The two adjacent cells share one common side. Hence, the perimeter of the figure is 6.  

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T15:22:52.669Z  

```py
class Solution:
    def findPerimeter(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        
        perimeter = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += 4
                    
                    if j + 1 < m and mat[i][j + 1] == 1:
                        perimeter -= 2
                        
                    if i + 1 < n and mat[i + 1][j] == 1:
                        perimeter -= 2
                        
        return perimeter
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-perimeter-of-shapes/1)