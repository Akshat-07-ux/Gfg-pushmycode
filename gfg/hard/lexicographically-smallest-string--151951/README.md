# Lexicographically Smallest Rotation

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string  **s**, find the lexicographically smallest string after rotating the string left any number of times including 0.

 **Example:** 

```
Input: s = "abcd"
Output: "abcd"
Explanation: String after each rotation are "abcd", "bcda", "cdab", "dabc" and so on. Lexicographically smallest among them is "abcd".

```

```
Input: s = "baca"
Output: "abac"
Explanation: Strings after each rotation are "baca", "acab", "caba", "abac" and so on. Lexicographically smallest among them is "abac".
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T06:02:18.526Z  

```py
class Solution:
    def lexiString(self, s: str) -> str:
        # code here
        l = len(s)
        
        twice = s + s
        i, j, k = 0, 1, 0
        
        while i < l and j < l and k < l:
            y = twice[i + k]
            z = twice[j + k]
            
            if y == z:
                k += 1
                
            elif y > z:
                i += k + 1
                if i <= j:
                    i = j + 1
                k = 0
            else:
                j += k + 1
                if j <= i:
                    j = i + 1
                k = 0
        
        res = min(i, j)
        return twice[res: res + l]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/lexicographically-smallest-string--151951/1)