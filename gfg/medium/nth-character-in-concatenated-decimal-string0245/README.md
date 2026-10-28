# Nth in Concatenated Decimal String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider a string  **s**  formed by concatenating the decimal representations of all positive integers in order:

s = "12345678910111213141516171819202122232425262728293031..."

Given an integer **n**, find the nth character (1-based indexing) in the string s.

 **Examples:** 

```
Input: n = 10
Output: '1'
Explanation: The 10th in "1234567891.." character is '1'.
```

```
Input: n = 11
Output: '0'
Explanation: The 11th character in "12345678910.."  is '0'.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T07:23:53.228Z  

```py
class Solution:

    def nthCharacter(self, n):
        # code here
        length = 1
        count = 9
        start = 1
        
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
            
        num = start + (n - 1) // length
        digit_idx = (n - 1) % length
        
        return str(num)[digit_idx]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/nth-character-in-concatenated-decimal-string0245/1)