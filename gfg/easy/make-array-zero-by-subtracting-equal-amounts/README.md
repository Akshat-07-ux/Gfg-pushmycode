# Minimum Subtraction to Make All 0

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a non-negative integer array  **arr[]**. In one operation, you must:

- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in arr[].
- Subtract x from every positive element in arr[].

Return the minimum number of operations required to make every element of the array equal to 0.

 **Examples:** 

```
Input: arr[] = [1, 5, 0, 3, 5]
Output: 3
Explanation:
Choose x = 1. Array becomes [0, 4, 0, 2, 4].
Choose x = 2. Array becomes [0, 2, 0, 0, 2].
Choose x = 2. Array becomes [0, 0, 0, 0, 0].
Thus, the minimum number of operations required is 3.
```

```
Input: arr[] = [0]
Output: 0
Explanation: All elements are already 0, so no operation is required.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-23T06:38:24.583Z  

```py
class Solution:

    def minOperations(self, arr):
        """code here"""
        
        
        return len({val for val in arr if val > 0})

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/make-array-zero-by-subtracting-equal-amounts/1)