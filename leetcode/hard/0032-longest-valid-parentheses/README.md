# Longest Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string containing just the characters `'('` and `')'`, return  *the length of the longest valid (well-formed) parentheses **substring*.

 

 **Example 1:** 

```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

```

 **Example 2:** 

```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

```

 **Example 3:** 

```
Input: s = ""
Output: 0

```

 

 **Constraints:** 

- 0 <= s.length <= 3 * 104
- s[i] is '(', or ')'.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 90.33%)  
**Memory:** 20.3 MB (beats 81.24%)  
**Submitted:** 2026-10-03T12:45:45.908Z  

```py
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        st = [-1]
        win = 0

        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)

            else:
                st.pop()
                if not st:
                    st.append(i)

                else:
                    win = max(win, i - st[-1])

        return win
        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)