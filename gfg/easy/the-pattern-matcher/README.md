# Repeated Pattern Check

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**  made of two characters of  **'x'** and  **'y'**.  The task is to verify whether  **s**  is made by concatenating substrings that follow the pattern  **xnyn**   (equal number of y' *s*  follow equal number of x' *s)*. 

 **Examples:** 

```
Input: s = "xxyyxy" 
Output: true
Explanation: The string can be split into "xxyy" + "xy". Both substrings contain an equal number of consecutive 'x' and 'y' characters.
```

```
Input: s = "xyx"
Output: false
Explanation: The last 'x' cannot form a valid substring because it is not followed by a matching 'y'. 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-17T07:08:03.451Z  

```py
class Solution:
    def findPattern(self, s):
        # code here
        i, n = 0, len(s)
        
        while i < n:
            if s[i] != 'x':
                return False
                
            x_cnt = 0
            while i < n and s[i] == 'x':
                x_cnt += 1
                i += 1
                
            y_cnt = 0
            while i < n and s[i] == 'y':
                y_cnt += 1
                i += 1
                
            if x_cnt != y_cnt:
                return False
                
        return True
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-pattern-matcher/1)