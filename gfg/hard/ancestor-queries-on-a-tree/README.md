# Ancestor Queries on a Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a tree with  **n**  nodes numbered from  **0**  to  **n - 1**, rooted at node 0 and an array  **arr[]**, where arr[i] represents the parent of node i. For the root node, arr[0] = -1.

Also given a 2D array  **queries[][]** of size q × 2, where each query is of the form [u, k].

For each query, find the k-th ancestor of node u, i.e., the node obtained after moving k times from u to its parent. If the k-th ancestor does not exist, return -1.

Return an array containing the answer for each query in the same order.

 **Examples:** 

```
Input: arr[] = [-1, 0, 0, 1, 1], queries[][] = [[4, 1], [3, 2], [4, 3]]

Output: [1, 0, -1]
Explanation: 
The 1st ancestor of 4 is 1.
The 2nd ancestor of 6 is 0.
The 3rd ancestor of 4 does not exist.

```

```
Input: arr[] = [-1, 0, 1, 0, 1, 1, 3, 3], queries[][] = [[5, 1], [5, 2], [2, 2], [7, 2]]

Output: [1, 0, 0, 0]
Explanation: 
The 1st ancestor of 5 is 1.
The 2nd ancestor of 5 is 0.
The 2nd ancestor of 2 is 0.
The 2nd ancestor of 7 is 0.
```

**Constraints:
**1 ≤ n, q ≤ 105
1 ≤ queries[i][0] ≤ n-1
1 ≤ queries[0][1] ≤ n

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T06:09:24.044Z  

```py
class Solution:
    def kthAncestorQueries(self, arr, queries):
        # code here
        
        n = len(arr)
        LOG = 18
        
        up = [[-1] * LOG for _ in range(n)]
        
        for i in range(n):
            up[i][0] = arr[i]
            
        for j in range(1, LOG):
            for i in range(n):
                parent = up[i][j - 1]
                if parent != -1:
                    up[i][j] = up[parent][j - 1]
                    
        ans = []
        for u, k in queries:
            curr = u
            
            for j in range(LOG):
                if (k >> j) & 1:
                    curr = up[curr][j]
                    if curr == -1:
                        break
            ans.append(curr)
            
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/ancestor-queries-on-a-tree/1)