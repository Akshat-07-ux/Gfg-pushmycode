# Population Count After n Days

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n**, consider a special species where population starts with one member on day 1 and grows using the follows rules:

- Each member produces 2 new members every day while it is alive.
- Each member has a lifespan of 6 days which means a member born on day d is removed before reproduction on day d + 6.

Find the total number of members present on the n-th day.

 **Examples:** 

```
Input: n = 2
Output: 3
Explanation: Day 1: 1, Day 2: 1 + 2 = 3
```

```
Input: n = 3
Output: 9
Explanation: Day 1: 1, Day 2: 3, Day 3: 3 + (3 x 2) = 9
```

```
Input: n = 7
Output: 726
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-28T06:29:34.059Z  

```py
class Solution:

    def countPopulation(self, n: int) -> int:
        """code here"""
        
        births = [0] * (n + 1)
        births[1] = 1
        active = 1
        
        for day in range(2, n + 1):
            if day - 6 >= 1:
                active -= births[day - 6]
                
            new_born = active * 2
            births[day] = new_born
            active += new_born
            
        return active
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/chicks-in-a-zoo1159/1)