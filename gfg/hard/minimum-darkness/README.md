# Minimum Disnace Tree Queries

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a tree with  **n** nodes (numbered as 1 to n) and an array  **query[]**  containing the order in which nodes are colored red.

After each operation:

- Make the node number query[i] red.
- Find the minimum distance between any two red nodes.
- If fewer than two nodes are red, return -1.

All values in query are unique.

 **Examples:** 

```
Input: n = 6, query[] = [2, 6, 1, 3], edges[][] = [[2, 4], [6, 5], [5, 3], [3, 4], [1, 3]]

Output: [-1, 4, 3, 1]
Explanation: 2 -> only one red -> -1, 6 -> distance to 2 is 4 -> 4, 1 -> closest to 6 is 3 -> 3, 3 -> directly connected to 1 -> 1

```

```
Input: n = 8, query[] = [8], edges[][] = [[5, 3], [6, 2], [2, 1], [7, 4], [3, 2], [4, 1], [8, 4]]
Output: [-1]
Explanation: Since there is only one operation to be performed so result is -1.

```

**Constraints:
**1 ≤ n ≤ 105
1 ≤ query.length < n
query contains distinct node values from 1 to n.
edges.length = n - 1
The edges form a tree.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T07:00:14.122Z  

```py
from collections import deque

class Solution:
    def minDistQueries(self, n: int, query: list[int], edges: list[list[int]]) -> list[int]:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        reds = set()
        ans = []
        min_dist = float('inf')

        for q_node in query:
            if reds:
                q = deque([(q_node, 0)])
                vis = {q_node}
                while q:
                    u, d = q.popleft()
                    if d >= min_dist:
                        break
                    if u in reds:
                        min_dist = d
                        break
                    for v in g[u]:
                        if v not in vis:
                            vis.add(v)
                            q.append((v, d + 1))

                ans.append(min_dist)
            else:
                ans.append(-1)
            reds.add(q_node)

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-darkness/1)