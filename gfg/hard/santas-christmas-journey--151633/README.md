# Count Node Visits for All Tree Paths

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

A tree has  **n**  nodes numbered 1 to n, connected by n - 1 edges given as **edges[][]**, where edges[i] = [u, v] indicates a direct edge between nodes u and v.

You are also given  **queries[][]**, where each query [u, v] represents the unique path from node u to node v. Every node on this path (including u and v) is counted once.

For each node, find how many times it was counted across all queries in queries[][].

 **Note:**  The tree is connected and acyclic, with exactly n - 1 edges.

 **Examples:** 

```
Input: n = 5, edges[][] = [[1, 2], [1, 3], [3, 4], [3, 5]], queries[][] = [[1, 3], [2, 5], [1, 4]]
Output: [3, 1, 3, 1, 1]
Explanation:

- Query [1, 3]: the path visits nodes [1, 3].
- Query [2, 5]: the path visits nodes [2, 1, 3, 5].
- Query [1, 4]: the path visits nodes [1, 3, 4].
Node 1 is visited 3 times, node 2 is visited 1 time, node 3 is visited 3 times, and nodes 4 and 5 are each visited 1 time.
```

```
Input: n = 4, edges[][] = [[1, 2], [2, 3], [2, 4]], queries[][] = [[1, 3], [4, 1]]
Output: [2, 2, 1, 1]
Explanation:
- Query [1, 3]: the path visits nodes [1, 2, 3].
- Query [4, 1]: the path visits nodes [4, 2, 1].
Node 1 is visited 2 times, node 2 is visited 2 times, nodes 3 and 4 are each visited 1 time.
```

```
Input: n = 4, edges[][] = [[1, 2], [2, 3], [3, 4]], queries[][] = [[1, 3], [2, 3]]
Output: [1, 2, 2, 0]
Explanation:
- Query [1, 3]: the path visits nodes [1, 2, 3].
- Query [2, 3]: the path visits nodes [2, 3]. Node 1 is visited 1 time, node 2 is visited 2 times, node 3 is visited 2 times, and node 4 is not visited.
```

**Constraints:
**1 ≤ n, queries.size() ≤ 105 
1 ≤ u, v ≤ n

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T12:02:48.901Z  

```py
import sys

# Set higher recursion limit for deep trees
sys.setrecursionlimit(200_000)

class Solution:
    def countVisits(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length() + 1
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        # BFS to compute depths and immediate parents
        from collections import deque
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            curr = q.popleft()
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    depth[nxt] = depth[curr] + 1
                    up[nxt][0] = curr
                    q.append(nxt)

        # Precompute binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j - 1]][j - 1]

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # Apply tree difference array updates
        diff = [0] * (n + 1)
        for u, v in queries:
            lca = get_lca(u, v)
            diff[u] += 1
            diff[v] += 1
            diff[lca] -= 1
            p = up[lca][0]
            if p != 0:
                diff[p] -= 1

        # Calculate final counts via subtree sum DFS
        ans = [0] * (n + 1)
        def dfs(node, parent):
            total = diff[node]
            for nxt in adj[node]:
                if nxt != parent:
                    total += dfs(nxt, node)
            ans[node] = total
            return total

        dfs(1, 0)
        return ans[1:]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/santas-christmas-journey--151633/1)