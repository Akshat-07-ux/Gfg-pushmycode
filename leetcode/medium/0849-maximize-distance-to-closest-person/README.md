# Maximize Distance to Closest Person

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array representing a row of `seats` where `seats[i] = 1` represents a person sitting in the `ith` seat, and `seats[i] = 0` represents that the `ith` seat is empty  **(0-indexed)**.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return  *that maximum distance to the closest person*.

 

 **Example 1:** 

```
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

```

 **Example 2:** 

```
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

```

 **Example 3:** 

```
Input: seats = [0,1]
Output: 1

```

 

 **Constraints:** 

- 2 <= seats.length <= 2 * 104
- seats[i] is 0 or 1.
- At least one seat is empty.
- At least one seat is occupied.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 74.09%)  
**Memory:** 20.4 MB (beats 24.19%)  
**Submitted:** 2026-10-07T06:24:41.649Z  

```py
class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        max_dist = 0
        last_person = -1
        n = len(seats)

        for i in range(n):
            if seats[i]  == 1:
                if last_person == -1:
                    max_dist = i

                else:
                    max_dist = max(max_dist, (i - last_person) // 2)
                last_person = i

        max_dist = max(max_dist, n - 1 - last_person)

        return max_dist
```

---

[View on LeetCode](https://leetcode.com/problems/maximize-distance-to-closest-person/)