# Minimum Insertions to Balance a Parentheses String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is  **balanced**  if:

- Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat `'('` as an opening parenthesis and `'))'` as a closing parenthesis.

- For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters `'('` and `')'` at any position of the string to balance it if needed.

Return  *the minimum number of insertions*  needed to make `s` balanced.

 

 **Example 1:** 

```
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

```

 **Example 2:** 

```
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

```

 **Example 3:** 

```
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of '(' and ')' only.

## Solution

**Language:** Python  
**Runtime:** 79 ms (beats 42.46%)  
**Memory:** 19.8 MB (beats 59.30%)  
**Submitted:** 2026-10-09T07:11:33.522Z  

```py
class Solution:
    def minInsertions(self, s: str) -> int:


        insertions = 0
        open_needed = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                if open_needed % 2 != 0:
                    insertions += 1
                    open_needed -= 1
                open_needed += 2
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2

                else:
                    insertions += 1
                    i += 1

                if open_needed > 0:
                    open_needed -= 2

                else:
                    insertions += 1

        return insertions + open_needed

        
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)