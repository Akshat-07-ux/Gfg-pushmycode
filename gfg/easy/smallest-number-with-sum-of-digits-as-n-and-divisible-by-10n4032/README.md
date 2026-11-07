# Smallest with digit sum n and divisible by 10^n

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n**, find the smallest number whose  **sum** of digits is equal to n and which is  **divisible** by 10n.

 **Note:** Return the resultant number as a string.

 **Examples :** 

```
Input: n = 5
Outptut: 500000
Explanation: Sum of digits of 500000 is 5 and divisible by 105.

```

```
Input: n = 20
Output: 29900000000000000000000
Explanation: Sum of digits of 29900000000000000000000 is 20 and divisible by 1020.

```

 **Constraint:** 
1 ≤ n ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-07T01:46:20.984Z  

```py
class Solution:
    def smallestNum(self, n: int) -> str:
        # code here
        
        digits= []
        original = n
        
        while n > 0:
            d = min(n, 9)
            digits.append(str(d))
            n -= d
            
        digits.reverse()
        return "".join(digits) + "0" * original
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-number-with-sum-of-digits-as-n-and-divisible-by-10n4032/1)