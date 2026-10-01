# Minimum Time to Finish Project

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

An IT company is working on a large project consisting of  **n**  modules.

- The given array time required (in months) to complete the ith module is stored in the array duration[].
- The array dependencies[][], where dependencies[i] = [u, v], indicates that module v can be started only after module u is completed. 

Multiple modules can be worked on simultaneously as long as all their dependencies have been completed.

Find the minimum time required to complete the entire project.

- If the project cannot be completed due to a cyclic dependency, return -1.
- A module is never dependent on itself.

 **Examples** 

```
Input: duration[] = [10, 20, 30, 10, 30, 20], dependencies[][] = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
Output: 80
Explanation: 

The Graph of dependency forms this and the project will be completed when Module 1 is completed. The minimum taken time is 80 months, the maximum taken time is through the path 5 -> 2 -> 3 -> 1 which takes 20 + 30 + 10 + 20
```

```
Input: duration[] = [5, 5, 5], dependencies[][] = [[0, 1], [1, 2], [2, 0]]
Output: -1
Explanation: There is a cycle in the dependency graph hence the project cannot be completed.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T12:45:31.526Z  

```py
from collections import deque
class Solution:
    def minTime(self, duration: list[int], dependencies: list[list[int]]) -> int:
        # code here
        
        l = len(duration)
        grp = [[] for _ in range(l)]
        
        deg = [0] * l
        
        for u, v in dependencies:
            grp[u].append(v)
            deg[v] += 1
            
        queue = deque(i for i in range(l) if deg[i] == 0)
        dp = list(duration)
        
        
        processed = 0
        while queue:
            cur = queue.popleft()
            processed += 1
            
            for nxt in grp[cur]:
                dp[nxt] = max(dp[nxt], dp[cur] + duration[nxt])
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    queue.append(nxt)
                    
        return max(dp) if processed == l else -1

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/project-manager--141631/1)