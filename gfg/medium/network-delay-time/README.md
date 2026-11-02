# Network Delay Time

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a network of nodes numbered from 0 to V- 1, represented by an adjacency list  **adj[][][]**, where adj[u] contains pairs [v, w] representing a directed connection from node u to node v with a signal propagation time of w units.

A signal is transmitted from a source node  **src**  at time 0. Find the minimum time required for the signal to reach all nodes. If any node is unreachable from the source, return -1.

 **Note:** There are no multiple edges between the same pair of nodes.

 **Examples:** 

```
Input: adj[][][] = [[[2, 1], [1, 4]], [], [[1, 2]]], src = 0
Output: 3
Explanation: 

In 3 units of time the signal can cover all the nodes by following this path: 0 -> 2 -> 1.
```

```
Input: adj[][][] = [[], [[0, 5]]], src = 0
Output: -1
Explanation: 

There is no connection from 0 to 1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T10:49:17.947Z  

```py
import heapq
class Solution:
    def findDelayTime(self, adj: list[list[list[int]]], src: int) -> int:
        # code here
        
        n = len(adj)
        dist = [float('inf')] * n
        dist[src] = 0
        
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
        max_delay = 0
        for d in dist:
            if d == float('inf'):
                return - 1
                
            if d > max_delay:
                max_delay = d
                
        return max_delay
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/network-delay-time/1)