# Largest Palindrome by Changing at most K Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string **s**  consisting of digits (0-9) and an integer  **k**. Convert the string into a palindrome by changing at most k digits. If multiple palindromes are possible, return the lexicographically largest one. If it's impossible to form a palindrome with k changes, return "-1".

 **Examples:** 

```
Input: s = "19495", k = 3 
Output: "99999"
Explanation: Change 1 and 5 to 9, and then change the middle digit 4 to 9, using exactly 3 changes to form the lexicographically largest palindrome "99999".
```

```
Input: s = "11345", k = 1 
Output: "-1"
Explanation: It is not possible to make s palindrome after 1 changes.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-24T07:19:28.579Z  

```py
class Solution:
    def maxPalindrome(self, s: str, k: int) -> str:
        # code here
        a = list(s)
        n = len(a)
        mod = [0] * n
        
        for i in range(n // 2):
            j = n - 1 - i
            if a[i] != a[j]:
                m = max(a[i], a[j])
                a[i] = a[j] = m
                mod[i if a[i] == m else j] = 1
                
                k -= 1
                
        if k < 0:
            return "-1"
            
        for i in range(n // 2):
            j = n - 1 - i
            if a[i] < "9":
                need = 2 - mod[i] - mod[j]
                
                if k >= need:
                    a[i] = a[j] = "9"
                    k -= need
                    
                    
        if n % 2 and k:
            a[n // 2] = "9"
            
        return "".join(a)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/largest-palindrome-by-changing-at-most-k-digits/1)