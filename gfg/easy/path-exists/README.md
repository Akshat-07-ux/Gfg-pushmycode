# Path Exists Between Two Vertices

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an undirected graph with  **V**  vertices numbered from 0 to V - 1, represented by an adjacency list  **adj[][]**, where adj[i] contains all vertices adjacent to vertex **i**. Also given two vertices  **u** and  **v**, check whether a path exists between them.

Return true if a path exists, otherwise return false.

 **Examples:** 

```
Input: adj[][] = [[2, 3], [2], [0, 1], [0], [5], [4]], u = 1, v = 5

Output: false
Explanation: There is no path from vertex 1 to vertex 5.
```

```
Input: adj[][] = [[2, 3], [2], [0, 1], [0], [5], [4]], u = 2, v = 3

Output: true
Explanation: We can reach vertex 3 from vertex 2 via vertex 0.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-28T06:25:15.420Z  

```py
from collections import deque
class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        # code here
        
        visit = set([u])
        q = deque([u])
        
        while q:
            cur = q.popleft()
            if cur == v:
                return True
                
            for nxt in adj[cur]:
                if nxt not in visit:
                    visit.add(nxt)
                    q.append(nxt)
                    
        return False
        
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/path-exists/1)