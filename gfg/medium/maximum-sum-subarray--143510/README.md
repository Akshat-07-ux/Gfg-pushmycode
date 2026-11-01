# Maximum Subarray Sum with One Square Allowed

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]**, find the maximum subarray sum by squaring at most one element.

 **Examples:** 

```
Input: arr[] =  [-1, -2, 3, -2, 3]
Output: 10
Explanation: The subarray {3, -2, 3} with squaring -2 will give the maximum sum as 3 + 4 + 3 = 10.
```

```
Input: arr[] =  [-4, -4, -2, 5, 2, -1]
Output: 27
Explanation: The subarray {5, 2} with squaring 5 will give a maximum sum of 25 + 2 = 27.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-01T05:21:11.703Z  

```py
class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        
        
        no_square = arr[0]
        one_square = arr[0] * arr[0]
        
        max_sum = max(no_square, one_square)
        
        
        for i in range(1, len(arr)):
            prev_no_square = no_square
            prev_one_square = one_square
            
            no_square = max(arr[i], prev_no_square + arr[i])
            
            one_square = max(
                arr[i] * arr[i],
                prev_no_square + arr[i] * arr[i],
                prev_one_square + arr[i]
            )
            
            max_sum = max(max_sum, no_square, one_square)
            
        return max_sum
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-sum-subarray--143510/1)