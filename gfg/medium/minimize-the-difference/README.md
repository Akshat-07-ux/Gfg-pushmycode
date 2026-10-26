# Minimize Max Min Diff with Subarray Removal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array  **arr[]**  of size  **n**. You need to remove a subarray of size  **k** , such that the difference between the maximum and minimum values of the remaining array is minimized. Find the minimum value obtained after performing the operation of the removal of the subarray.

 **Examples:** 

```
Input: arr = [1, 2, 3, 4, 5], k = 3 
Output: 1
Explanation: We remove first subarray of length 3, the remaining array is [4,5] and the difference of maximum and minimum element is 1 i.e 5 - 4 = 1
```

```
Input: arr = [2, 3, 1, 4, 6, 7], k = 3
Output: 2
Explanation: 
If we remove the subarray [2,3,1] then remaining array is [4,6,7] and the difference  = 7-4 = 3
If we remove the subarray [3,1,4] then remaining array is [2,6,7] and the difference  = 7-2 = 5
If we remove the subarray [1,4,6] then remaining array is [2,3,7] and the difference  = 7-2 = 5
If we remove the subarray [4,6,7] then remaining array is [2,3,1] and the difference  = 3-1 = 2
So the answer is min(3,5,5,2) = 2
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T03:34:44.744Z  

```py
class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        # code here
        
        n = len(arr)
        if k >= n:
            return 0
            
        if k == 0:
            return max(arr) - min(arr)
            
        pref_max = [0] * n
        pref_min = [0] * n
        
        cur_max = arr[0]
        cur_min = arr[0]
        for i in range(n):
            cur_max = max(cur_max, arr[i])
            cur_min = min(cur_min, arr[i])
            
            pref_max[i] = cur_max
            pref_min[i] = cur_min
            
        suff_max = [0] * n
        suff_min = [0] * n
        
        cur_max = arr[-1]
        cur_min = arr[-1]
        
        for i in range(n - 1, -1, -1):
            cur_max = max(cur_max, arr[i])
            cur_min = min(cur_min, arr[i])
            suff_max[i] = cur_max
            suff_min[i] = cur_min

            
        ans = float('inf')
        
        for i in range(n - k + 1):
            rem_max = -float('inf')
            rem_min = float('inf')
            
            if i > 0:
                rem_max = max(rem_max, pref_max[i - 1])
                rem_min = min(rem_min, pref_min[i - 1])
                
            if i + k < n:
                rem_max = max(rem_max, suff_max[i + k])
                rem_min = min(rem_min, suff_min[i + k])
                
            ans = min(ans, rem_max - rem_min)
            
        return ans
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimize-the-difference/1)