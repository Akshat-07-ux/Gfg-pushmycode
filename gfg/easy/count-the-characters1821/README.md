# Count Group Occurrences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**  and an integer  **k**, count the number of distinct characters that appear in exactly  **k groups**  in the string.

A group is defined as one or more consecutive occurrences of the same character. For example, in the string "aaabbcca", the groups are "aaa", "bb", "cc" and "a".

 **Examples:** 

```
Input: s = "abc", k = 1
Output: 3
Explanation: The characters 'a', 'b' and 'c' each appear in exactly one group.
```

```
Input: s = "geeksforgeeks", k = 2
Output: 4
Explanation: The characters 'g', 'e', 'k' and 's' each appear in exactly two groups.
```

```
Input: s = "aaaaa", k = 2
Output: 0
Explanation: The character 'a' appears in only one group, so no character appears in exactly two groups.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-09T03:34:00.213Z  

```py
class Solution:
    def getCount (self, s, k):
        # code here
        freq = {}
        n = len(s)
        
        i = 0
        
        while i < n:
            ch = s[i]
            while i < n and s[i] == ch:
                i += 1
            freq[ch] = freq.get(ch, 0) + 1
            
        return sum(1 for ch in freq if freq[ch] == k)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-the-characters1821/1)