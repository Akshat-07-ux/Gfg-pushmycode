# K-Similar Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Strings `s1` and `s2` are `k` **-similar**  (for some non-negative integer `k`) if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

Given two anagrams `s1` and `s2`, return the smallest `k` for which `s1` and `s2` are `k` **-similar**.

 

 **Example 1:** 

```
Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".

```

 **Example 2:** 

```
Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".

```

 

 **Constraints:** 

- 1 <= s1.length <= 20
- s2.length == s1.length
- s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
- s2 is an anagram of s1.

## Solution

**Language:** Python  
**Runtime:** 250 ms (beats 15.87%)  
**Memory:** 24.9 MB (beats 10.58%)  
**Submitted:** 2026-10-12T06:15:20.565Z  

```py
from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            curr, steps = queue.popleft()

            i = 0
            while i < len(curr) and curr[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i]:
                    next_str = list(curr)
                    next_str[i], next_str[j] = next_str[j], next_str[i]

                    next_str = "".join(next_str)

                    if next_str == s2:
                        return steps + 1

                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append((next_str, steps + 1))

        return 0

```

---

[View on LeetCode](https://leetcode.com/problems/k-similar-strings/)