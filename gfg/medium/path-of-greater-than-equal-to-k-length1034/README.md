# Path of Total Weight Greater Than or Equal to K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an undirected weighted graph with  **V**  vertices numbered from **0**  to  **V - 1**  and an integer  **k**, find if there exists a simple path starting from the source vertex  **0**  such that the total weight of the path is greater than or equal to  **k**.

A simple path is a path that does not contain repeated vertices. Return true if such a path exists; otherwise, return false.

 **Example 1:** 

```
Input: V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [4, 3, 10]], k = 8
Output: true
Explanation: One possible simple path is 0 -> 1 -> 4. The total path weight is 4 + 6 = 10, which is greater than or equal to k = 8.

```

```
Input: V = 4, edges[][] = [[0, 1, 5], [1, 2, 1], [2, 3, 1]], k = 8
Output: false
Explanation: There exists no path which has a distance of 8 or more.
```

 **Constraints:** 
2 ≤ V ≤ 5
1 ≤ edges.size() ≤ 20
1 ≤ k ≤ 100

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T06:24:22.844Z  

```py
class Solution:
    def pathMoreThanK(self, V, edges, k):
        # code here
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        def dfs(u, current_weight):
            if current_weight >= k:
                return True
                
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v, current_weight + w):
                        return True
                        
                    visited[v] = False
            return False
            
        visited = [False] * V
        visited[0] = True
        return dfs(0, 0)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/path-of-greater-than-equal-to-k-length1034/1)