# Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given `n` pairs of parentheses, write a function to  *generate all combinations of well-formed parentheses*.

 

 **Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

 **Example 2:** 

```
Input: n = 1
Output: ["()"]

```

 

 **Constraints:** 

- 1 <= n <= 8

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 36.93%)  
**Submitted:** 2026-10-02T06:06:03.157Z  

```py
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def bt(cur, open_c, close_c):
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if open_c < n:
                bt(cur + '(', open_c + 1, close_c)

            if close_c < open_c:
                bt(cur + ')', open_c, close_c + 1)

        bt("", 0, 0)
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)