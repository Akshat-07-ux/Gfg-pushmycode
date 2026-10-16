# Odd Equals Even Path

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a tree of  **n**  nodes, rooted at node **0**. Each node is numbered from 0 to n-1. Also given a 2D integer array  **edges[][]** of size n-1 where each edges[i] = [ui, vi] denotes that there is an edge between nodes ui and vi in the tree. 

Find the number of paths starting from each subtree rooted at node i (0 ≤ i < n) such that the count of odd nodes in the path is equal to the count of even nodes in the path.

Return an array of size n, where the i-th element is the number of such paths starting from the subtree rooted at node i. 

 **Note:** The maximum depth of the tree is atmost 200.

 **Examples:** 

```
Input: edges[][] = [[0,1], [0,2]]
Output: [1, 0, 0]
Explanation: The tree is as follows:

For subtree rooted at node 0, the only path in which the number of odd nodes is equal to number of even nodes is the path [0, 1]. 
For subtree rooted at node 1, there is only one path which is [1] and it is not valid.
For subtree rooted at node 2, there is only one path which is [2] and it is not valid.
```

```
Input: edges[][] = [[0, 1], [0, 2], [2, 3]]
Output: [1, 0, 1, 0] 
Explanation: The tree is as follows:

For subtree rooted at node 0, the only path in which the number of odd nodes is equal to number of even nodes is the path [0, 1].
For subtree rooted at node 1, there is only one path which is [1] and it is not valid.
For subtree rooted at node 2, the only path in which the number of odd nodes is equal to number of even nodes is the path [2, 3].
For subtree rooted at node 3, there is only one path which is [3] and it is not valid.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T05:06:18.459Z  

```py
class Solution:
    def countPaths(self, edges):
        # code here
        
        
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        children = [[] for _ in range(n)]
            
        visited = [False] * n
        queue = [0]
        visited[0] = True
            
        idx = 0
        while idx < len(queue):
            curr = queue[idx]
            idx += 1
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    children[curr].append(nxt)
                    queue.append(nxt)
                        
        ans = [0] * n
            
        def dfs(curr, balance):
            count = 0
            if balance == 0:
                count += 1
                    
            for nxt in children[curr]:
                nb = balance + (1 if nxt % 2 == 1 else -1)
                count += dfs(nxt, nb)
                    
            return count
                 
        for i in range(n):
            init_balance = 1 if i % 2 == 1 else -1
            ans[i] = dfs(i, init_balance)
                
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/odd-equals-even-path-i--151405/1)