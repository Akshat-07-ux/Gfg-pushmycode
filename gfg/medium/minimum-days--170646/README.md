# Minimum Days

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  of length n containing only lowercase English letters, and a permutation array  **p[]**  of length n containing integers from 0 to n - 1.

On the (i + 1)th day, the character at index p[i] in the string is replaced with '?'. For example:

- On day 1, replace s[p[0]] with '?'.
- On day 2, replace s[p[1]] with '?'.
- On day 3, replace s[p[2]] with '?'.
- And so on.

Find the minimum number of days required so that no two adjacent characters in s are equal, unless at least one of them is '?'.

Formally, for every index i (0 <= i < n - 1), the string must satisfy: If s[i] != '?' and s[i+1] != '?', then s[i] != s[i+1].

 **Examples:** 

```
Input: s = "aabb", p = [2, 1, 3, 0]
Output: 2
Explanation:
On Day 1, we replace s[p[0]] (index 2) with '?'. String becomes "aa?b". Index 0 and 1 still have equal adjacent characters 'a'.
On Day 2, we replace s[p[1]] (index 1) with '?'. String becomes "a??b". Now no two adjacent non-'?' characters are equal.
```

```
Input: s = "abca", p = [3, 0, 2, 1]
Output: 0
Explanation:
The initial string "abca" already satisfies the condition without replacing any characters.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-05T09:33:05.761Z  

```py
class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # code here
        n = len(s)
        
        def can_make_valid(k):
            arr = list(s)
            
            for i in range(k):
                arr[p[i]] = "?"
                
                
            for i in range(n - 1):
                if arr[i] != '?' and arr[i + 1] != '?' and arr[i] == arr[i + 1]:
                    return False
                    
            return True
            
        left, right = 0, n
        result = n
        
        
        while left <= right:
            mid = (left + right) // 2
            if can_make_valid(mid):
                result = mid
                right = mid - 1
                
            else:
                left = mid + 1
                
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-days--170646/1)