# Maximum Nesting Depth of the Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a  **valid parentheses string**  `s`, return the  **nesting depth**  of `s`. The nesting depth is the  **maximum**  number of nested parentheses.

 

 **Example 1:** 

 **Input:**  s = "(1+(2*3)+((8)/4))+1"

 **Output:**  3

 **Explanation:** 

Digit 8 is inside of 3 nested parentheses in the string.

 **Example 2:** 

 **Input:**  s = "(1)+((2))+(((3)))"

 **Output:**  3

 **Explanation:** 

Digit 3 is inside of 3 nested parentheses in the string.

 **Example 3:** 

 **Input:**  s = "()(())((()()))"

 **Output:**  3

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
- It is guaranteed that parentheses expression s is a VPS.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 7.32%)  
**Memory:** 19.3 MB (beats 14.71%)  
**Submitted:** 2026-09-28T06:29:57.635Z  

```py
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0

        for char in s:
            if char == "(":
                cur_depth += 1
                if cur_depth > max_depth:
                    max_depth = cur_depth

            elif char == ")":
                cur_depth -= 1

        return max_depth
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)