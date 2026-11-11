# Min Changes For Bitwise AND Greater Than x

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  of size  **n**  and an integer  **x**, in one operation you can replace any element of the array with an integer.

Find the minimum number of operations required to make the bitwise AND of all array elements strictly greater than x.

 **Examples:** 

```
Input: x = 2, arr[] = [3, 1, 2, 7]
Output: 2
Explanation: The initial bitwise AND is 3 & 1 & 2 & 7 = 0, which is not greater than 2. Replace 1 with 3 and 2 with 11 to get [3, 3, 11, 7]. Now, 3 & 3 & 11 & 7 = 3, which is greater than 2. Hence, the answer is 2.
```

```
Input: x = 1, arr[] = [2, 2, 2]
Output: 0
Explanation: The bitwise AND of the array is 2 & 2 & 2 = 2, which is already greater than 1. Therefore, no operation is required.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-11T09:04:00.212Z  

```py
class Solution:
    def count(self, arr, x):
        # code here
        
        n = len(arr)
        ans = n
        pref = 0
        
        for bit in range(30, -1, -1):
            if (x >> bit) & 1:
                pref |= (1 << bit)
                continue
            
            need = pref | (1 << bit)
            keep = 0
            
            for value in arr:
                if (value & need) == need:
                    keep += 1
                    
            ans = min(ans, n - keep)
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/bitwise-and-of-the-array--170633/1)