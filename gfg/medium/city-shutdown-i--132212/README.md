# Max Disconnected Pairs with Single Removal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given  **n**  cities (0 to n-1) connected by n-1 roads such that there is exactly one path between any two cities, and a 2D array  **roads[][]**  where roads[i] = [u, v] denotes a road connecting city u and city v, find the maximum number of pairs of cities that become disconnected after removing any single city.

 **Note:**  The removed city itself is not counted in the disconnected pairs.

 **Examples:** 

```
Input: n = 5, roads[][] = [[0, 1], [1, 2], [1, 3], [1, 4]]

Output: 6

Explanation: Removing city 1 disconnects the following pairs of cities: [0, 2], [0, 3], [0, 4], [2, 3], [2, 4], and [3, 4].
```

```
Input: n = 3, roads[][] = [[0, 2], [1, 2]]

Output: 1

Explanation: Removing city 2 disconnects city 0 from city 1.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T08:47:20.983Z  

```py
import sys
sys.setrecursionlimit(100000)
class Solution:

    def maxCities(self, roads: list[list[int]], n: int) -> int:
        # code here
        
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
            
        sz = [0] * n
        
        def get_sizes(u, p):
            sz[u] = 1
            for v in adj[u]:
                if v != p:
                    get_sizes(v, u)
                    sz[u] += sz[v]
                    
        get_sizes(0, -1)
        
        min_sum_sq = float('inf')
        
        def evaluate(u, p):
            nonlocal min_sum_sq
            sum_sq = 0
            for v in adj[u]:
                if v != p:
                    sum_sq += sz[v] * sz[v]
                    
            parent_sz = n - sz[u]
            sum_sq += parent_sz * parent_sz
            
            if sum_sq < min_sum_sq:
                min_sum_sq = sum_sq
                
            for v in adj[u]:
                if v != p:
                    evaluate(v, u)
                    
        evaluate(0, -1)
        return ((n - 1) * (n - 1) - min_sum_sq) // 2
        
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/city-shutdown-i--132212/1)