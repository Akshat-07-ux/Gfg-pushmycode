# Successful Binary Searches Irrespective of Pivot

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  of n distinct integers (not necessarily sorted), consider the following search for a target:

- Maintain a range [lo, hi], initially [0, n-1].
- At each step, pick any index p in [lo, hi] (not necessarily the middle) as pivot. If arr[p] == target, stop - found.
- If target < arr[p], set hi = p - 1; if target > arr[p], set lo = p + 1. If lo > hi, stop - not found.

Count the number of indices i such that searching for target = arr[i] succeeds no matter which pivot is chosen at every step (i.e., for every possible sequence of pivot choices).

 **Examples:** 

```
Input: arr[] = [3, 7, 9, 8, 15]
Output: 3
Explanation: 3, 7, and 15 (indices 0, 1, 4) are always found: every possible pivot comparison happens to steer the search toward them, no matter the order. 9 and 8 are not: e.g. if the first pivot picked is 8, searching for 9 gets pushed right and index 2 is lost forever; if the first pivot is 9, searching for 8 gets pushed left and index 3 is lost forever.

```

```
Input: arr[] = [9, 4, 1, 10, 22, 23, 20]
Output: 1
Explanation: Only 10 (index 3) is always found — every pivot, left or right, happens to steer toward it. Everything else can fail on some pivot order: e.g. picking 4 first pushes a search for 9 away permanently, and picking 20 first makes a search for 22 run off the end of the array entirely.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T04:44:38.587Z  

```py
class Solution:
    def countAlwaysFound(self, arr):
        # code here
        
        n = len(arr)
        if n == 0:
            return 0
            
        left_max = [0] * n
        cur_max = arr[0]
        
        for i, x in enumerate(arr):
            if x > cur_max:
                cur_max = x
            left_max[i] = cur_max
            
        right_min = [0] * n
        cur_min = arr[-1]
        
        for i in range(n-1, -1, -1):
            if arr[i] < cur_min:
                cur_min = arr[i]
                
            right_min[i] = cur_min
            
        valid_count = 0
        for i in range(n):
            ok_left = (i == 0) or (arr[i] > left_max[i - 1])
            ok_right = (i == n - 1) or (arr[i] < right_min[i + 1])
            if ok_left and ok_right:
                valid_count += 1
                
        return valid_count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-always-found/1)