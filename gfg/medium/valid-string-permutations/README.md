# Count Strings Formed by One Swap

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  consisting of lowercase English alphabets, count the number of unique strings that can be obtained by swapping any two  **distinct** characters of s. The original string should also be included in the count.

 **Examples:** 

```
Input: s = "sstt"
Output: 5
Explanation: Unique strings obtained are: "sstt", "tsst", "tsts", "stst", "stts". So, the answer is 5.
```

```
Input: s = "abcd"
Output: 7
Explanation: All characters are distinct. Swapping any pair gives a new unique string.
Number of possible swaps: 4 * 3 / 2 = 6
Including the original string: 6 + 1 = 7
```

 **Constraints:** 
1 ≤ |s| ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-16T08:45:03.938Z  

```py
class Solution:

    def countStrings(self, s):
        """code here"""
        
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
            
        total_swaps = 0
        n = len(s)
        
        for char in s:
            idx = ord(char) - 97
            total_swaps += n - counts[idx]
            counts[idx] -= 1
            n -= 1
            
        return total_swaps + 1



```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/valid-string-permutations/1)