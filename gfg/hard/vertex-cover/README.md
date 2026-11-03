# Vertex Cover

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an undirected graph with  **n**  vertices and a 2D array  **edges[][]**, where edges[i] = [u, v] represents an edge between vertices u and v, find the minimum number of vertices required to form a vertex cover.

A vertex cover is a set of vertices such that at least one endpoint of every edge belongs to the set.

 **Examples:** 

```
Input: n = 5, edges[][] = [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]
Output: 3
Explanation: One possible vertex cover is [2, 3, 4].
Check each edge:
[1,2] -> vertex 2 is selected.
[4,1] -> vertex 4 is selected.
[2,4] -> vertex 2 or 4 is selected.
[3,4] -> vertex 3 or 4 is selected.
[5,2] -> vertex 2 is selected.
[1,3] -> vertex 3 is selected.
Thus, all edges are covered using 3 vertices. No vertex cover with fewer than 3 vertices is possible, so the answer is 3.
```

```
Input: n = 2, edges[][] = [[1, 2]]
Output: 1
Explanation: The only edge connects vertices 1 and 2. Selecting either 1 or 2 covers this edge.
Therefore, the minimum vertex cover has size 1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-03T05:41:57.856Z  

```py
class Solution:
    def vertexCover(self, edges):
        n = max(max(u, v) for u, v in edges)

        edge_masks = []
        for u, v in edges:
            edge_masks.append((1 << (u - 1)) | (1 << (v - 1)))

        ans = n

        for mask in range(1 << n):
            count = bin(mask).count('1')

            if count >= ans:
                continue

            valid = True

            for edge in edge_masks:
                if not (mask & edge):
                    valid = False
                    break

            if valid:
                ans = count

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/vertex-cover/1)