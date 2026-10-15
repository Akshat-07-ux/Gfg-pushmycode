# Node in Subtree or Not

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a tree with   n   nodes rooted at node 1 and a 2D vector   edges[][] , where edges[i] = [u, v] represents an undirected edge between nodes u and v. 

You are also given a 2D array   queries[][]   of size q, where each query is of the form [a, b]. For each query, check whether node a belongs to the subtree rooted at node b.

Return a boolean array where the ith element is true if a is in the subtree of b; otherwise, false.

 **Examples:** 

```
Input: n = 9, edges[][] = [[1, 2], [1, 3], [2, 6], [2, 7], [6, 9], [7, 8], [3, 4], [3, 5]], queries[][] = [[8, 2], [2, 8], [6, 5], [5, 6], [9, 1]]

Output: [true, false, false, false, true]
Explanation: 8 is present in the subtree of 2 and 9 is present in the subtree of 1. For the other queries, the given node does not belong to the specified subtree, so they return false.
```

```
Input: n = 5, edges[][] = [[1, 2], [1, 3], [3, 4], [3, 5]], queries[][] = [[3, 2], [1, 4], [4, 1]]

Output: [false, false, true]
Explanation: Node 4 is the only queried node that belongs to the subtree rooted at node 1. Therefore, only the last query returns true.
```

 **Constraints:** 
1 ≤ n ≤ 105
edges.length = n - 1
1 ≤ edges[i][0], edges[i][1] ≤ n
1 ≤ a, b ≤ n
1 ≤ q ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T05:03:01.363Z  

```py
import sys
sys.setrecursionlimit(2000000)
class Solution:
    def checkIfSubtree(self, n, edges, queries):
        # code here
        
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        in_time = [0] * (n + 1)
        out_time = [0] * (n + 1)
        timer = 0
        
        def dfs(u, p):
            nonlocal timer
            timer += 1
            in_time[u] = timer
            for v in adj[u]:
                if v != p:
                    dfs(v, u)
                    
            timer += 1
            out_time[u] = timer
            
        dfs(1, 0)
        
        result = []
        for a, b in queries:
            if in_time[b] <= in_time[a] <= out_time[b]:
                result.append(True)
            else:
                result.append(False)
                
        return result
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-alice/1)