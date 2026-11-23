# Character at Position in Infinite String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  and an integer  **pos**, an infinite string is constructed by repeatedly applying the following operation. In the i-th step, append i consecutive $ characters, followed by the reverse of the current string, to the current string.

Formally, if the current string is s, update it as:

- s = s + ('$' repeated i times) + reverse(s)

The initial string is the given s, and the process continues indefinitely.

Find and return the character at the pos(1-based indexing) in the resulting infinite string.

 **Examples:** 

```
Input: s = "12345", pos = 3
Output: 3
Explanation: In "12345...", the character at pos 3 is 3.

```

```
Input: s = "12345", pos = 10
Output: 2
Explanation: In "12345$54321...", the character at pos 10 is 2.

```

```
Input: s = "abc", pos = 7
Output: a
Explanation: In "abc$cba...", the character at pos 7 is a.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-23T06:36:01.748Z  

```py
class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        
        lens = [len(s)]
        step = 0
        
        while lens[-1] < pos:
            step += 1
            lens.append(2 * lens[-1] + step)
            
        for i in range(step, 0, -1):
            prev = lens[i - 1]
            if pos <= prev:
                continue
            
            if pos <= prev + i:
                return "$"
                
            offset = pos - (prev + i)
            pos = prev - offset + 1
            
        return s[pos - 1]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-infinite-string1049/1)