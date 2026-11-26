# Terms of Recursive Series

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Geek made a special series that follows recurrence   **Tn = (Tn-2)2 - (Tn-1)**. The first (or T1)  and the second term (or T2) are 0 and 1 respectively.

Given an integer  **n**, return the first n terms of the series.

 **Examples** 

```
Input: n = 3
Output: [0, 1, -1]
Explanation: First-term is given as 0 and the second term is 1. So the T3 = (T3-2)2 - (T3-1) = T12 - T2 = 02 - 1 = -1
```

```
Input: n = 6
Output: [0, 1, -1, 2, -1, 5]
Explanation:
T1 : 0
T2 : 1
T3 : -1
T4 = (1)2 - (-1) = 2
T5 = (-1)2 - (2) = 1 - 2 = -1
T6 = (2)2 - (-1) = 4 + 1 = 5 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-26T06:40:35.214Z  

```py
class Solution:
    def gfSeries(self, n):
        # code here
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-2] ** 2 - seq[-1])
            
        return seq
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/gf-series3535/1)