# Rotate Array Clockwise

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array  **arr** [] of integers and an integer  **k**. Your task is to  **rotate** the array **k** times in the **clockwise direction**.
In a single clockwise rotation, the last element of the array moves to the front, and all other elements shift one position to the right.

**Examples:
**

```
Input: arr[] = [1, 2, 3, 4, 5, 6], k = 2
Output: [5, 6, 1, 2, 3, 4]
Explanation: Rotating the array 2 times in clockwise gives the array [5, 6, 1, 2, 3, 4].
```

```
Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: [2, 3, 4, 5, 1]
Explanation: Rotating the array [1, 2, 3, 4, 5] four times clockwise gives the array [2, 3, 4, 5, 1].
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-21T10:59:07.991Z  

```py
class Solution:
    def rotateclockwise(self, arr, k):
        # code here
        
        n = len(arr)
        k %= n
        if k == 0:
            return arr
            
        def flip(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                
                left += 1
                right -= 1
                
        flip(0, n - 1)
        flip(0, k - 1)
        flip(k, n - 1)
        return arr
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/rotate-array-clockwise/1)