# Minimum Weight Subtree Connecting Given Nodes

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a tree with n nodes numbered from 1 to n, represented by a 2D array edges[][] of size n-1, where edges[i] = [a, b] denotes an undirected edge between nodes a and b. The weight of an edge [a, b] is the absolute difference of their node numbers.

An array nodes[] contains distinct nodes of the tree. Find the minimum total weight of a connected subgraph of the tree that contains all the nodes in nodes[].

 **Examples:** 

```
Input: edges[][] = [[1, 2], [2, 3], [3, 4], [3, 5]], nodes[] = [1, 4, 5]
Output: 5
Explanation: The smallest subtree containing nodes 1, 4 and 5 uses the edges (1-2), (2-3), (3-4), (3-5) with weights 1, 1, 1, 2. Total = 5.
```

```
Input: edges[][] = [[1, 2], [2, 3], [2, 4], [4, 5]], nodes[] = [2, 5]
Output: 3
Explanation: The smallest subtree containing nodes 2 and 5 uses the edges (2-4) and (4-5) with weights 2 and 1. Total = 3.
```

```
Input: edges[][] = [[1, 2], [1, 3], [1, 4]], nodes[] = [1]
Output: 0
Explanation: A single node is already connected, so no edge is needed. Total = 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T05:39:18.522Z  

```py
class Solution:
    def minWeight(self, edges: list[list[int]], nodes: list[int]) -> int:
        # code here
        
        
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        is_required = [False] * (n + 1)
        for node in nodes:
            is_required[node] = True
            
        root = nodes[0]
        parent = [0] * (n + 1)
        order = []
        
        queue = [root]
        visited = [False] * (n + 1)
        visited[root] = True
        
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            order.append(curr)
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = curr
                    queue.append(neighbor)
                    
                    
        cnt = [1 if is_required[i] else 0 for i in range(n + 1)]
        total_weight = 0
        
        for curr in reversed(order):
            if curr == root:
                continue
            
            if cnt[curr] > 0:
                total_weight += abs(curr - parent[curr])
                cnt[parent[curr]] += cnt[curr]
                
                
        return total_weight
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-cost-to-visit-favorite-cities--132208/1)