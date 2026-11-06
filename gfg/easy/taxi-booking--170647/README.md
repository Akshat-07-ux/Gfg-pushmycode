# Taxi Booking

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

The task is to the minimum time required for any taxi to reach your position.

- You are given positions of the available taxis in an array pos[], where pos[i] represents the position of the ith taxi.
- Another array time[] is given, where time[i] represents the time taken by the ith taxi to travel one unit of distance.
- Also given your position as curr.  The time taken by a taxi to reach your position is |pos[i] - cur| * time[i]. 

 **Examples:** 

```
Input: cur = 4, pos = [1, 5, 6], time = [2, 3, 1]
Output: 2
Explanation: Total time taken by the 1st taxi will be: (4-1) *2 = 6 Total time taken by the 2nd taxi will be: (5-4)* 3 = 3 Total time taken by the 3rd taxi will be: (6-4)*1 = 2 So, the minimum time will be 2 sec.
```

```
Input: cur = 1, pos = [1, 6], time = [10, 3]
Output: 0
Explanation: Total time taken by the 1st taxi will be: (1-1) *10 = 0 Total time taken by the 2nd taxi will be: (6-1)* 3 = 15 So, the minimum time will be 0 sec.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T15:44:21.529Z  

```py
class Solution:
    def minimumTime(self, cur: int, pos: list[int], time: list[int]) -> int:
        # code here
        
        return min(abs(p - cur) * t for p, t in zip(pos, time))

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/taxi-booking--170647/1)