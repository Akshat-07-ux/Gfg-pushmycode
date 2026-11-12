# Maximum Length Chain of Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a 2d array  **arr[][],** where each arr[i] consists of two integers (a, b) such that a < b.  A pair (c, d) can follow another pair (a, b) if and only if b < c.  A chain of pairs is a sequence of pairs where each pair can follow the previous one.

Return the length of the longest chain that can be formed using the given pairs. You may arrange the pairs in any order.

 **Examples:** 

```
Input: arr[][] = [[5, 24], [15, 25], [27, 40], [50, 60]]
Output: 3
Explanation: One of the longest pairs is [5, 24] -> [27, 40] -> [50, 60].
```

```
Input: arr[][] = [[6, 8], [3, 4]]
Output: 2
Explanation: The longest chain pair is [3, 4] -> [6, 8]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-12T06:42:54.963Z  

```py
class Solution:
    def maxChainLen(self, arr):
        # code here
        if not arr:
            return 0
            
        arr.sort(key=lambda x: x[1])
        
        chain_l = 1
        cur_end = arr[0][1]
        
        for i in range(1, len(arr)):
            if arr[i][0] > cur_end:
                cur_end = arr[i][1]
                chain_l += 1
                
        return chain_l
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-length-chain-of-pairs/1)