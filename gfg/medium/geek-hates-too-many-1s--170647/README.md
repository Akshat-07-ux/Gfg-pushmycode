# Maximum Without 3 Consecutive Set Bits

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a non-negative integer  **n**, you can only change a set bit (1) to an unset bit (0). Find the maximum possible value of n such that its binary representation does not contain three consecutive set bits (111) after performing zero or more allowed operations.

 **Examples:** 

```
Input: n = 2
Output: 2
Explanation: The binary representation of 2 is 10, which does not contain three consecutive set bits. Therefore, no change is required.
```

```
Input: n = 7
Output: 6
Explanation: The binary representation of 7 is 111, which contains three consecutive set bits. Changing the rightmost set bit to 0 gives: 111 -> 110. Thus, the maximum possible value is 6.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T04:56:33.545Z  

```py
class Solution:

    def maxValue(self, n: int) -> int:
        """code here"""
        
        bits = [0] * 32
        for i in range(32):
            if (n & (1 << (31 - i))) != 0:
                bits[i] = 1
                
        ans = 0
        for i in range(30):
            if bits[i] == 1:
                ans += (1 << (31 - i))
                if bits[i + 1] == 1:
                    bits[i + 2] = 0
                    
        if bits[30] == 1:
            ans += 2
        if bits[31] == 1:
            ans += 1
            
        return ans

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geek-hates-too-many-1s--170647/1)