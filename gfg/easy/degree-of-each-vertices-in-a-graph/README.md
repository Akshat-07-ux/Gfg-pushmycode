# Degree For Each Vertex

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a directed graph with  **V** vertices numbered from 0 to V-1 and  **E**  edges, represented as a 2D array  **edges[][]**, where each entry  **edges[i] = [u, v]**  denotes a directed edge from vertices  **u**  to  **v**. determine the  **in-degree**  (number of incoming edges) and  **out-degree**  (number of outgoing edges) for every vertex in the graph.

 **Examples :** 

```
Input: V = 4, edges[][] = [[0, 1], [0, 3], [1, 0], [2, 0], [3, 0], [3, 2]]
    
Output: [[3, 2], [1, 1], [1, 1], [1, 2]] 
Explanation: 
Vertex 0 has 3 incoming and 2 outgoing edges.
Vertex 1 has 1 incoming and 1 outgoing edges.
Vertex 2 has 1 incoming and 1 outgoing edges.
Vertex 3 has 1 incoming and 2 outgoing edges.

```

```
Input: V = 5, edges[][] = [[0, 1], [0, 3], [1, 2], [2, 4], [3, 4], [4, 1]]
    
Output: [[0, 2], [2, 1], [1, 1], [1, 1], [2, 1]]
Explanation: 
Vertex 0 has 0 incoming and 2 outgoing edges.
Vertex 1 has 2 incoming and 1 outgoing edges.
Vertex 2 has 1 incoming and 1 outgoing edges.
Vertex 3 has 1 incoming and 1 outgoing edges.
Vertex 4 has 2 incoming and 1 outgoing edges.
```

 **Constraints:** 
1 ≤ V, E ≤ 106
0 ≤ edges[i][0], edges[i][1] < V

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T05:14:09.715Z  

```py
class Solution:
    def findInOutDegree(self, V, edges):
        # code here
        
        in_deg = [0] * V
        out_deg = [0] * V
        
        for u, v in edges:
            out_deg[u] += 1
            in_deg[v] += 1
            
        return [[in_deg[i], out_deg[i]] for i in range(V)]

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/degree-of-each-vertices-in-a-graph/1)