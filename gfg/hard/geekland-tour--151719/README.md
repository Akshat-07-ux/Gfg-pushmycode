# Maximum Cities Visited in Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Geek is planning a tour of Geekland, a country with cities numbered from  **1** to  **n**.

- Cities are connected by roads in the form of a tree with n cities and n-1 roads.
- Each city i (1 to n) is located at a position loc[i - 1], where the distance between two connected cities is the absolute difference between their locations.
- The roads in Geekland are represented by a 2D array roads[][] of size (n - 1) * 2, where roads[j] = [u, v] indicates a bi-directional road between city u and city v.

Find the maximum number of cities Geek can visit with the following conditions,

- Can only travel along roads where the distance between the two connected cities is less than or equal to k
- It is not allowed to traverse any road more than once. 

 **Examples:** 

```
Input: loc[] = [1, 2, 4, 5], roads[][] = [[1,2], [2,3], [4,2]], k = 1
Output: 2
Explanation: Geek can start at city 1 (location 1) and visit city 2 (location 2) since the distance between these two cities is |1 - 2| = 1 <= k. The other roads have distances 2 and 3, which exceed k. This allows Geek to visit a total of 2 cities.
```

```
Input: loc[] = [1, 2, 4, 5], roads[][] = [[1,2], [2,3], [4,2]], k = 3
Output: 3
Explanation: All connected road distances are <= 3 (|1 - 2| = 1, |2 - 4| = 2, |5 - 2| = 3). Geek can go on a tour along either (1 -> 2 -> 3), (1 -> 2 -> 4), or (3 -> 2 -> 4), visiting a total of 3 cities.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T10:21:51.895Z  

```py
from collections import deque
class Solution:
    def maxCities(self, loc: list[int], roads: list[list[int]], k: int) -> int:
        # code here
        
        n = len(loc)
        adj = [[] for _ in range(n + 1)]
        
        for u, v in roads:
            if abs(loc[u - 1] - loc[v - 1]) <= k:
                adj[u].append(v)
                adj[v].append(u)
                
        seen = [False] * (n + 1)
        best = 1
        
        
        def bfs_f(start: int) -> tuple[int, int]:
            dist = {start: 0}
            q = deque([start])
            far_node = start
            while q:
                cur = q.popleft()
                if dist[cur] > dist[far_node]:
                    far_node = cur
                    
                for nxt in adj[cur]:
                    if nxt not in dist:
                        dist[nxt] = dist[cur] + 1
                        q.append(nxt)
            return far_node, dist[far_node]
            
        for i in range(1, n + 1):
            if seen[i]:
                continue
            
            u, _ = bfs_f(i)
            v, diameter = bfs_f(u)
            best = max(best, diameter + 1)
            
            q = deque([u])
            seen[u] = True
            while q:
                cur = q.popleft()
                for nxt in adj[cur]:
                    if not seen[nxt]:
                        seen[nxt] = True
                        q.append(nxt)
                        
        return best
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geekland-tour--151719/1)