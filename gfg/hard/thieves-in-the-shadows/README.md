# Thieves in the Shadows

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

In a town plagued by thieves, the mayor has a list of  **n**  thieves that are scheduled to be caught, numbered  **1**  through  **n.**  Each thief:

- Has a threat level ai (positive integer), and
- Belongs to a specific gang type b? (an integer between 1 and m inclusive).

To aid in the operation, the mayor can assign up to  **m**   **special guards**,  **one per gang**. The guard of gang type  **j**  can neutralize all threats from that gang's thieves.
The mayor begins the operation with a total preparedness level  **h**  (his ability to endure threats without failing the mission). The plan is carried out in order from thief  **1**  to thief  **n**, following these steps:
For each thief  **i = 1 to n**, as long as preparedness is positive:
If no guard is assigned for the gang  **b?** :

- The thief deals a? threat to the mayor (subtract a? from h).

If after that, h > 0:

- The thief is captured.

Otherwise:

- The mayor fails, and no more thieves can be dealt with.

You are to solve the following task for every possible number of guards  **k= 0, 1, …, m:** 
Determine the maximum number of thieves that the mayor can successfully capture when he assigns exactly  **k**  guards (choosing them from the available  **m**  gang types).

 **Examples:** 

```
Input: n = 5, m = 2, h = 13.
       a[] = [10, 10, 6, 9, 3]
       b[] = [2, 1, 2, 2, 1]
Output: [1, 4, 5]
Explanation: For k = 0, no guards are deployed. The first thief reduce the mayor’s health to 3, but the second thief  drops it below zero. So only 1 thief is captured.
For k = 1, choosing the gang 2 to guard allows capturing 4 thieves before health runs out.
For k = 2, choosing two optimal gangs 2, 1 avoids most damage, allowing 5 captures.
```

```
Input: n = 3, m = 1, h = 4.
       a[] = [1, 1, 2]
       b[] = [1, 1, 1]
Output: [2, 3]
Explanation: it can be seen that 2 thieves can be captured when k = 0, 3 when k = 1.

```

**Constraints:
**1 ≤ m ≤ n ≤ 105 
1 ≤ h ≤ 107
1 ≤ ai ≤ 106
1 ≤ bi ≤ m
for each 1 ≤ i ≤ m, there is 1 ≤ j ≤ n, such that bj = i.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T07:22:10.478Z  

```py
class Solution:
    def solve(self, n, m, h, a, b):
        vals = []
        cur = [0] * m
        prefix = [[] for _ in range(n)]

        for i in range(n):
            x = b[i] - 1
            cur[x] += a[i]
            prefix[i] = cur[x]
            vals.append(cur[x])

        vals = sorted(set(vals))
        size = len(vals)
        pos = {v: i for i, v in enumerate(vals)}

        count = [0] * (4 * size)
        sums = [0] * (4 * size)

        def update(node, left, right, idx, dc, ds):
            count[node] += dc
            sums[node] += ds

            if left == right:
                return

            mid = (left + right) // 2
            if idx <= mid:
                update(node * 2, left, mid, idx, dc, ds)
            else:
                update(node * 2 + 1, mid + 1, right, idx, dc, ds)

        def required(node, left, right, need):
            if left == right:
                return need // vals[left] + 1

            mid = (left + right) // 2
            rnode = node * 2 + 1

            if sums[rnode] > need:
                return required(rnode, mid + 1, right, need)

            return count[rnode] + required(
                node * 2, left, mid, need - sums[rnode]
            )

        total = [0] * m
        ans = [0] * (m + 1)
        damage = 0

        for i in range(n):
            gang = b[i] - 1
            old = total[gang]
            new = old + a[i]
            total[gang] = new
            damage += a[i]

            if old:
                update(1, 0, size - 1, pos[old], -1, -old)

            update(1, 0, size - 1, pos[new], 1, new)

            if damage < h:
                guards = 0
            else:
                guards = required(1, 0, size - 1, damage - h)

            ans[guards] = i + 1

        for k in range(1, m + 1):
            ans[k] = max(ans[k], ans[k - 1])

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/thieves-in-the-shadows/1)