# Maximum Stove Runtime

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Geek is organizing a party at his house. He has an integer array  **amt[]**, where amt[i] represents the amount of gas available in the ith LPG cylinder.

- There are k stoves, and each stove consumes one unit of gas per unit time.
- A stove can switch from one cylinder to another instantly, and replacing a cylinder takes zero time.

Find the maximum time for which all k stoves can remain lit simultaneously.

 **Examples:** 

``` Input: amt[] = [1, 2, 3], k = 2 Output: 3 Explanation: One stove uses the cylinders with 1 and 2 units of gas, while the other stove uses the cylinder with 3 units of gas. Thus, both stoves remain lit for 3 units of time.  ```
``` Input: amt[] = [5, 7, 8], k = 2 Output: 10 Explanation: One possible allocation is Stove 1 uses the first cylinder completely (5 units) and then 5 units from the second cylinder. Stove 2 uses the remaining 2 units from the second cylinder and all 8 units from the third cylinder. Thus, both stoves remain lit simultaneously for 10 units of time. ```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-17T07:14:09.536Z  

```py
class Solution:
    def maximumTime(self, amt, k):
        # code here
        
        total_gas = sum(amt)
        max_possible = total_gas // k
        
        low, high = 0, max_possible
        ans = 0
        
        
        while low <= high:
            mid = (low + high) // 2
            
            effective_gas = sum(min(x, mid) for x in amt)
            
            if effective_gas >= k * mid:
                ans = mid
                low = mid + 1
                
            else:
                high = mid - 1
                
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geeks-party/1)