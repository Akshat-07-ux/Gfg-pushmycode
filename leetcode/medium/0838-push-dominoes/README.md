# Push Dominoes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string `dominoes` representing the initial state where:

- dominoes[i] = 'L', if the ith domino has been pushed to the left,
- dominoes[i] = 'R', if the ith domino has been pushed to the right, and
- dominoes[i] = '.', if the ith domino has not been pushed.

Return  *a string representing the final state*.

 

 **Example 1:** 

```
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

```

 **Example 2:** 

```
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

```

 

 **Constraints:** 

- n == dominoes.length
- 1 <= n <= 105
- dominoes[i] is either 'L', 'R', or '.'.

## Solution

**Language:** Python  
**Runtime:** 88 ms (beats 82.81%)  
**Memory:** 22.4 MB (beats 68.53%)  
**Submitted:** 2026-09-28T06:35:54.615Z  

```py
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = list('L' + dominoes + 'R')
        win, i = [], 0

        for j in range(1, len(l)):
            if l[j] == '.':
                continue

            mid = j - i - 1
            if i > 0:
                win.append(l[i])
            if l[i] == l[j]:
                win.append(l[i] * mid)

            elif l[i] == 'L' and l[j] == 'R':
                win.append('.' * mid)

            else:
                win.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))

            i = j

        return ''.join(win)
```

---

[View on LeetCode](https://leetcode.com/problems/push-dominoes/)