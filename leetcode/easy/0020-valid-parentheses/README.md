# Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

 

 **Example 1:** 

 **Input:**  s = "()"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "()[]{}"

 **Output:**  true

 **Example 3:** 

 **Input:**  s = "(]"

 **Output:**  false

 **Example 4:** 

 **Input:**  s = "([])"

 **Output:**  true

 **Example 5:** 

 **Input:**  s = "([)]"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 32.77%)  
**Memory:** 19.3 MB (beats 24.83%)  
**Submitted:** 2026-10-01T13:05:14.130Z  

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracks = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracks:
                top = stack.pop() if stack else ''

                if top != bracks[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0
```

---

[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)