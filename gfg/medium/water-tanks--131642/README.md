# Water Tanks

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **tank[]**, where tank[i] represents the initial amount of water in the ith tank.

- Each tank can hold at most x liters of water at the end and excess water needs to be transferred.
- You also have an unlimited number of additional empty tanks. You may perform any number of transfers and use the additional empty tanks whenever required.
- You can transfer any amount of water from one tank to another with maximum wastage of w liters for given w.

If  **y** liters are transferred:

- If y <= w, all y liters are lost.
- If y > w, exactly w liters are lost, and the remaining y - w liters are transferred successfully.

Find the maximum total amount of water that can remain across all tanks after all transfers.

 **Examples:** 

```
Input: tank[] = [5, 7, 9, 13], x = 6, w = 2
Output: 29
Explanation:
tank[0]: Contains 5 liters, less than 6, so no change.
tank[1]: Contains 7 liters. Excess 1 liter will be wasted since 1 <= w. The tank now holds 6 liters.
tank[2]: Contains 9 liters. Transfer 3 liters to tank[0], and 2 liters are wasted. The tank[2] and tank[0] now hold 6 liters each.
tank[3]: Contains 13 liters. Transfer 7 liters to a new tank, and 2 liters are wasted. The tank[3] now holds 6 liters, and the new tank holds 5 liters.
The final tank configuration will be [6, 6, 6, 6, 5], resulting in a total amount of water remaining: 6 + 6 + 6 + 6 + 5 = 29.
```

```
Input: tank[] = [2, 6, 12], x = 6, w = 4
Output: 16
Explanation:
tank[0]: Contains 2 liters, less than 6, so no change.
tank[1]: Contains 6 liters, which is already at the maximum allowed capacity, so no change.
tank[2]: Contains 12 liters. Transfer 8 liters to a new empty tank. Since w = 4, exactly 4 liters are wasted and the remaining 4 liters are transferred successfully. tank[2] now holds 4 liters, and the new tank holds 4 liters.
The final tank configuration will be [2, 6, 4, 4], resulting in a total amount of water remaining: 2 + 6 + 4 + 4 = 16.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T06:13:45.328Z  

```py
class Solution:
    def waterTank(self, tanks, x, w):
        # code here
        total = 0
        step = x + w
        
        for amt in tanks:
            if amt <= x:
                total += amt
                continue
            
            extra = amt - x
            full_moves, rem = divmod(extra, step)
            wasted = full_moves * w + min(rem, w)
            total += amt - wasted
            
        return total
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/water-tanks--131642/1)