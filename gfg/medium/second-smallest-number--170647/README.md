# Second Smallest with Sum and Count of Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two integers  **a**  and  **b**, where a represents the required sum of digits and b represents the number of digits, find the second smallest b-digit number whose sum of digits is equal to a. Return the second smallest number as a string. If no such number exists, return "-1".

 **Examples:** 

```
Input: a = 9, b = 2
Output: "27"
Explanation: 18 is the smallest 2-digit number whose digit sum is 9, while 27 is the second smallest.
```

```
Input: a = 16, b = 3
Output: "178"
Explanation: 169 is the smallest 3-digit number whose digit sum is 16, while 178 is the second smallest.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T06:02:25.850Z  

```py
class Solution:

    def secondSmallest(self, a: int, b: int) -> str:
        """ code here """
        
        if b == 1 or a <= 1 or a >= 9 * b:
            return "-1"
            
        s, temp_a = ['0'] * b, a - 1
        
        for i in range(b - 1, 0, -1):
            d = min(9, temp_a)
            s[i], temp_a = str(d), temp_a - d
            
        s[0] = str(temp_a + 1)
        
        i = b - 1
        while i > 0 and s[i] == '9':
            i -= 1
            
        if i == b - 1:
            if s[i] == '0': return "-1"
                
            s[i], s[i - 1] = str(int(s[i]) - 1), str(int(s[i - 1]) + 1)
            
        else:
            i += 1
            s[i], s[i - 1] = str(int(s[i]) - 1), str(int(s[i - 1]) + 1)
            
        return "".join(s)

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/second-smallest-number--170647/1)