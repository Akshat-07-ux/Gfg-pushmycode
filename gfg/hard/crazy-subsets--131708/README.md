# Subsets with MEX in Range

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array **arr[]** of integers and a range  **[l, r]**, count the number of subsets whose Minimum Excluded (MEX) value lies within the given range, inclusive.

- Minimum Excluded (or MEX) of a subset is the smallest non-negative integer that is not present in the subset.
- An empty subset has Minimum Excluded as zero.

Since the answer can be very large, return the answer modulo  **109 + 7**.

 **Examples:** 

```
Input: arr[] = [2, 0, 1, 0], l = 1, r = 2
Output: 9
Explanation: The subsets whose MEX lies in the range [1, 2] are counted as follows:
MEX = 1: The subsets must contain at least one 0 and must not contain 1. These subsets are [0] (2 ways), [2, 0] (2 ways), [0, 0] (1 way), and [2, 0, 0] (1 way). Total = 6.
MEX = 2: The subsets must contain both 0 and 1 but must not contain 2. These subsets are [0, 1] (2 ways) and [0, 1, 0] (1 way). Total = 3.
The subsets [2, 0, 1] and [2, 0, 1, 0] have MEX = 3, which is outside the given range. Therefore, the total number of valid subsets is 6 + 3 = 9.
```

```
Input: arr[] = [2, 0, 1], l = 1, r = 2
Output: 3
Explanation: The subsets whose MEX lies in the range [1, 2] are [0] (MEX = 1), [2, 0] (MEX = 1), and [0, 1] (MEX = 2). Hence, the answer is 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T10:50:22.876Z  

```py
from typing import List
class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        """ code here """
        n = len(arr)
        M = 1000000007
        
        
        mp = {}
        
        for num in arr:
            mp[num] = mp.get(num, 0) + 1
            
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % M
            
        res = 0
        cur = 1
        seen = 0
        
        for i in range(l):
            freq = mp.get(i, 0)
            if freq == 0:
                return 0
                
            seen += freq
            cur = (cur * (power[freq] - 1 + M)) % M
            
        
        for i in range(l, r + 1):
            freq = mp.get(i, 0)
            here = (cur * power[n - seen - freq]) % M
            res = (res + here) % M
            
            if freq == 0:
                break
            seen += freq
            cur = (cur * (power[freq] - 1 + M)) % M
            
        return res

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/crazy-subsets--131708/1)