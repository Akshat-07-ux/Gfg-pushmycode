# Equal Islands

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

There are  **n**  islands, where the importance value of island i is represented by  **arr[i - 1].**  Initially, all n islands are separate. A 2D array  **queries[][]**  of size  **q**  represents operations where each query consists of two 1-based island numbers u and v that must be merged into a single island.

The importance value of the newly merged island is the sum of the importance values of the two component islands. After processing all queries, check if the remaining distinct islands can be partitioned into two non-empty groups such that both groups have equal total importance values.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 5, 6], queries[][] = [[1, 2], [2, 3], [4, 5]] 
Output: false
Explanation: The remaining components have importance values [6, 9, 6]. Their total sum is 21, which is odd and cannot be partitioned into two equal integers.
```

```
Input: arr[] = [2, 1, 3], queries[][] = [[1, 2]]
Output: true
Explanation: Merging 1 and 2 gives an island with importance 3. The remaining islands have importance [3, 3], which can be partitioned into two groups of value 3 each.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T12:19:39.184Z  

```py
class Solution:
    def isEqual(self, arr: list[int], queries: list[list[int]]) -> bool:
        # code here
        
        parent = list(range(len(arr)))
        comp_sum = list(arr)
        
        
        def find(i):
            path = []
            
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
                
            return i
            
        for u, v in queries:
            root_u = find(u - 1)
            root_v = find(v - 1)
            
            if root_u != root_v:
                parent[root_v] = root_u
                comp_sum[root_u] += comp_sum[root_v]
                
        sums = [comp_sum[i] for i in range(len(arr)) if parent[i] == i]
        
        total = sum(sums)
        
        if total % 2 != 0:
            return False
            
        target = total // 2
        dp = 1
        for s in sums:
            dp |= (dp << s)
            
        return bool((dp >> target) & 1)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/equal-islands--151537/1)