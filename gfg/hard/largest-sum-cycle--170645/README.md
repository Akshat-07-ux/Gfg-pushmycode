# Largest Sum Cycle

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array   edge[]   of size   n , there are   n   cells numbered from   0   to   n - 1 . Each cell has at most one outgoing edge.

For every cell i:

- edge[i] is the cell reached from i in one step.
- edge[i] = -1 means that cell i has no outgoing edge.

A cycle is a sequence of cells where, by following the outgoing edges, we eventually return to the starting cell. The sum of a cycle is the sum of the indices of all cells in that cycle.

Return the maximum cycle sum. If there is no cycle, return -1.

  Examples:  

```
Input: edge[] = [1, 2, 0, -1]
Output: 3
Explanation: There is only one cycle in the graph i.e. 0 -> 1 -> 2 -> 0. Sum of the cell index in that cycle = 0 + 1 + 2 = 3.

```

```
Input: edge[] = [2, 0, -1, 2]
Output: -1
Explanation: There is no cycle in the graph. The edges are 1 -> 0 -> 2 <- 3. Hence, 2 has no outgoing edge, so no cycle exists.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T10:42:01.966Z  

```py
class Solution:
    def largestSumCycle(self, edge):
        # code here
        
        n = len(edge)
        visited = [0] * n
        max_sum = -1
        
        for i in range(n):
            if visited[i] == 0:
                curr = i
                path = []
                path_index = {}
                
                while curr != -1 and visited[curr] == 0:
                    visited[curr] = 1
                    path_index[curr] = len(path)
                    path.append(curr)
                    curr = edge[curr]
                    
                    
                if curr != -1 and visited[curr] == 1:
                    start_idx = path_index[curr]
                    cycle_sum = sum(path[start_idx:])
                    if cycle_sum > max_sum:
                        max_sum = cycle_sum
                        
                for node in path:
                    visited[node] = 2
                    
        return max_sum
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/largest-sum-cycle--170645/1)