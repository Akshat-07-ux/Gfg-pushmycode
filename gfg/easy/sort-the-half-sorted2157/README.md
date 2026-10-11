# Sort Two Parts  Sorted

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array  **arr[]**  where the two parts around a break point are individually sorted, merge them into a single sorted array.  The break point can be anywhere in the array, including at the beginning or end.

 **Examples:** 

```
Input: arr[] = [2, 3, 8, -1, 7, 10]
Output: [-1, 2, 3, 7, 8, 10] 
Explanation: [2, 3, 8] and [-1, 7, 10] are sorted in the original array. The overall sorted version is [-1 2 3 7 8 10].
```

```
Input: arr[] = [-4, 6, 9, -1, 3]
Output: [-4, -1, 3, 6, 9]
Explanation: [-4, 6, 9] and [-1, 3] are sorted in the original array. The overall sorted version is [-4 -1 3 6 9].
```

```
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: One part is empty and the other part is whole array which is already sorted.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T05:53:37.180Z  

```py
class Solution:
    def mergeTwoParts(self, arr):
        # code here
        n = len(arr)
        
        idx = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                idx = i + 1
                break
            
        if idx == 0:
            return 
            
        temp = [0] * n
        i, j, k = 0, idx, 0
        
        while i < idx and j < n:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
                
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
            
        while i < idx:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j < n:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        arr[:] = temp
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sort-the-half-sorted2157/1)