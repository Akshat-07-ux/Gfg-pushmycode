# Maximum Packages within Time

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A delivery agent has to deliver packages at locations arranged in a line. The number of packages at the **ith**  location is given by  **arr[i]**.

- The agent can start at any location and can only visit consecutive locations.
- Visiting each location takes 1 unit of time.

Given  **arr[]**  and  **totalTime**, find the maximum number of packages the agent can deliver within  **totalTime**.

 **Examples:** 

```
Input: arr[] = [2, 1, 3, 5, 0, 1, 4], totalTime = 3
Output: 9
Explanation: The agent can visit three consecutive locations. Starting from the second location, it delivers arr[1] + arr[2] + arr[3] = 1 + 3 + 5 = 9 packages.
```

```
Input: arr[] = [1, 6, 2, 5, 3, 4], totalTime = 2
Output: 8
Explanation: The agent can visit two consecutive locations. Starting from the second location, it delivers arr[1] + arr[2] = 6 + 2 = 8 packages. Starting from the fourth location gives arr[3] + arr[4] = 5 + 3 = 8 packages. Hence, the maximum is 8 packages.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T05:46:24.998Z  

```py
class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        n = len(arr)
        
        if totalTime >= n:
            return sum(arr)
            
        window_sum = sum(arr[:totalTime])
        max_packages = window_sum
        
        for i in range(totalTime, n):
            window_sum += arr[i] - arr[i - totalTime]
            if window_sum > max_packages:
                max_packages = window_sum
                
        return max_packages
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/bird-and-maximum-fruit-gathering0509/1)