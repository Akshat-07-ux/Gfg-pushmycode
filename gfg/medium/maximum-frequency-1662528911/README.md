# Maximum Frequency with K Increments

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]**. In one operation, you can choose an index and increment its value by 1.

Find the maximum possible frequency of any element after performing at most k operations.

 **Examples:** 

```
Input: arr[] = [2, 2, 4], k = 4
Output: 3
Explanation: Apply two increment operations on index 0 and two operations on index 1 to make arr[]= [4, 4, 4]. Frequency of 4 is 3.

```

```
Input: arr[] = [7, 7, 7, 7], k = 5
Output: 4
Explanation: The frequency of 7 is already 4, so no operations are needed.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T07:10:13.006Z  

```py
class Solution:
    def maxFrequency(self, arr, k):
        # code here
        arr.sort()
        left = 0
        total_sum = 0
        max_freq = 0
        
        for right in range(len(arr)):
            total_sum += arr[right]
            
            while (right - left + 1) * arr[right] - total_sum > k:
                total_sum -= arr[left]
                left += 1
                
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-frequency-1662528911/1)