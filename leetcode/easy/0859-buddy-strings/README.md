# Buddy Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `goal`, return `true` *if you can swap two letters in* `s` *so the result is equal to* `goal` *, otherwise, return* `false` *.* 

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`.

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

 **Example 1:** 

```
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

```

 **Example 2:** 

```
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

```

 **Example 3:** 

```
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

```

 

 **Constraints:** 

- 1 <= s.length, goal.length <= 2 * 104
- s and goal consist of lowercase letters.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 49.80%)  
**Memory:** 19.1 MB (beats 94.00%)  
**Submitted:** 2026-10-17T06:37:09.934Z  

```py
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True

                seen.add(ch)
            return False

        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)

        return len(diff_indices) == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]
        
```

---

[View on LeetCode](https://leetcode.com/problems/buddy-strings/)