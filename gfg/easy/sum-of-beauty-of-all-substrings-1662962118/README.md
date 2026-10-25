# Sum of Beauty of All Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**, return the sum of the beauty of all substrings of s. The beauty of a substring is defined as the difference between the maximum and minimum frequencies of the characters present in that substring.

 **Examples:** 

```
Input: s = "aaac"
Output: 3
Explanation: The substrings with non-zero beauty are "aaac" and "aac". 
For "aaac", the frequencies are a = 3 and c = 1. Its beauty is 3 − 1 = 2. 
For "aac", the frequencies are a = 2 and c = 1. Its beauty is 2 − 1 = 1. 
The remaining substrings have a beauty of 0. Therefore, the sum of the beauties of all substrings is 2 + 1 = 3.
```

```
Input: s = "aabc"
Output: 2
Explanation: The substrings with non-zero beauty are "aab" and "aabc". 
For "aab", the frequencies are a = 2 and b = 1. Its beauty is 2 − 1 = 1. 
For "aabc", the frequencies are a = 2, b = 1, and c = 1. Its beauty is 2 − 1 = 1. 
Therefore, the sum of the beauties of all substrings is 1 + 1 = 2.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T12:13:32.125Z  

```py
class Solution:
    def beautySum(self, s: str) -> int:
        # code here
        ans = 0
        n = len(s)
        
        for i in range(n):
            counts = {}
            
            for j in range(i, n):
                counts[s[j]] = counts.get(s[j], 0) + 1
                
                max_freq = max(counts.values())
                min_freq = min(counts.values())
                
                ans += (max_freq - min_freq)
                
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-beauty-of-all-substrings-1662962118/1)