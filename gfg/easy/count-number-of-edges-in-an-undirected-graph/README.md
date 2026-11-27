# Count Edges in Graph

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an undirected graph with  **V**  vertices numbered from  **0**  to  **V - 1**, represented by an adjacency list  **adj[][]**, where  **adj[i]**  contains the vertices adjacent to vertex  **i.** 

Return the total number of edges present in the graph.

 **Examples:** 

```
Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3], [2]]

Output: 4
Explanation: The edges in the graph are: (0-1), (0-2), (2-3), (1-2). Hence, total number of edges = 4.

```

```
Input: adj[][] = [[1], [0, 2], [1, 3], [2]]

Output: 3
Explanation: The edges in the graph are: (0-1), (1-2), (2-3). Hence, total number of edges = 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T09:39:04.663Z  

```py
class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        total = 0
        for neighbours in adj:
            total += len(neighbours)
            
        return total // 2
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-number-of-edges-in-an-undirected-graph/1)