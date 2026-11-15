# Maximal Disjoint Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a 2d array  **arr[][]**  of n time slots, represented as a list of  **intervals**, where each interval consists of a  **start time**  and an  **end time**. Your task is to return the  **maximum number**  of  **non-overlapping**  time slots.
 **Note:**  Two intervals  **[a, b]**  and  **[c, d]**  are considered  **non-overlapping**  if they do not share any common points.

 **Examples:** 

```
Input: n = 4, arr[][] = [[1, 4], [2, 3], [4, 6], [8, 9]]
Output: [[2, 3], [4, 6], [8, 9]]
Explanation: If we include the interval [1, 4], it overlaps with both [2, 3] and [4, 6]. Instead, by selecting [2, 3], [4, 6], and [8, 9], we obtain the maximum number of non-overlapping intervals.
```

```
Input: n = 3, arr[][] = [[1, 9], [2, 3], [5, 7]]
Output: [[2, 3], [5, 7]]
Explanation: By selecting [2, 3] and [5, 7], we obtain the maximum number of non-overlapping intervals.

```

**Constraints:
**1 ≤ n ≤  105
0 ≤ arr[i][0] < arr[i][1] ≤ 5*104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-15T13:29:51.405Z  

```py
def maxDisjointInterval(arr):
    # code here
    
    if not arr:
        return []
        
    arr.sort(key=lambda x: x[1])
    
    selected = []
    last_end = -float("inf")
    
    for interval in arr:
        start, end = interval
        
        if start > last_end:
            selected.append(interval)
            last_end = end
            
    return selected
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximal-disjoint-intervals/1)