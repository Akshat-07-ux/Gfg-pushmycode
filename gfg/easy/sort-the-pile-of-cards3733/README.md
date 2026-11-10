# Minimum Front Moves to Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array  **arr[]** of size n containing a permutation of the integers from 1 to n (i.e., each integer from 1 to n appears exactly once), find the  **minimum**  number of operations to sort it in increasing order.

In one operation, pick any element and move it to the front, keeping the relative order of the rest unchanged.

 **Examples:** 

```
Input: arr[] = [5, 1, 2, 3, 4]
Output: 4
Explanation: Initially 5 1 2 3 4 
4 5 1 2 3 - move 4 to the front
3 4 5 1 2 - move 3 to the front
2 3 4 5 1 - move 2 to the front
1 2 3 4 5 - move 1 to the front
The array is now sorted after 4 operations, which is the minimum possible.
```

```
Input: arr[] = [3, 4, 2, 1]
Output: 2
Explanation: Initially 3 4 2 1
2 3 4 1 - move 2 to the front
1 2 3 4 - move 1 to the front
The array is now sorted after 2 operations, which is the minimum possible.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-10T08:46:05.419Z  

```py
class Solution:
    def minOps(self, arr):
        # code here
        n = len(arr)
        
        expected = n
        count = 0
        
        for i in range(n - 1, -1, -1):
            if arr[i] == expected:
                count += 1
                expected -= 1
                
        return n - count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sort-the-pile-of-cards3733/1)