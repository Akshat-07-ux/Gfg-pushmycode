# Min Flips for Alternate

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary string  **s**, we can flip any bit (change 0 to 1 or 1 to 0) to make the string alternating. A string is called alternating if no two adjacent characters are the same.

Find the minimum number of bit flips required to make the string alternating.

 **Examples:** 

```
Input: s = "001"
Output: 1
Explanation: Flip the bit at index 0 from 0 to 1 to obtain "101", which is an alternating binary string. Hence, the minimum number of flips required is 1.

```

```
Input: s = "0001010111" 
Output: 2
Explanation: Flip the bit at indices 1 and 8 to obtain "0101010101", which is an alternating binary string. Hence, the minimum number of flips required is 2.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T06:05:41.723Z  

```py
class Solution:
    def minFlips(self, s):
        # Code here
        
        diff = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                diff += 1
                
        return min(diff, len(s) - diff)
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/min-number-of-flips3210/1)