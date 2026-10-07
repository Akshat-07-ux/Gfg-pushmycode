# Remove Invalid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return  *a list of  **unique strings**  that are valid with the minimum number of removals*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "()())()"
Output: ["(())()","()()()"]

```

 **Example 2:** 

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

```

 **Example 3:** 

```
Input: s = ")("
Output: [""]

```

 

 **Constraints:** 

- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

## Solution

**Language:** Python  
**Runtime:** 75 ms (beats 66.09%)  
**Memory:** 20.1 MB (beats 34.36%)  
**Submitted:** 2026-10-07T06:15:20.664Z  

```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(st):
            cnt = 0
            for c in st:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        res = []
        visited = {s}

        q = [s]
        found = False

        while q:
            nxt = []
            for curr in q:
                if is_valid(curr):
                    res.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue

                    candidate = curr[:i] + curr[i+1:]
                    if candidate not in visited:
                        visited.add(candidate)
                        nxt.append(candidate)

            if found:
                break
            q = nxt

        return res
        
```

---

[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)