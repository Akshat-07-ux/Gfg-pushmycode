# Max Path Sum Between Two Leaves

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given the root of a binary tree, where each node contains an integer value, find the maximum possible path sum between any two leaf nodes. If the tree has fewer than two leaf nodes, return -1.

 **Examples:** 

```
Input: root = [3, 4, 5, -10, 4, N, N]
                   
Output: 16
Explanation: 

The leaf nodes are -10, 4 (right child of 4), and 5.
Possible paths between leaf nodes are:
-10 -> 4 -> 3 -> 5 = -10 + 4 + 3 + 5 = 2
-10 -> 4 -> 4 = -10 + 4 + 4 = -2
4 -> 4 -> 3 -> 5 = 4 + 4 + 3 + 5 = 16
Hence, the maximum path sum is obtained from the path 4 -> 4 -> 3 -> 5, giving 16.

```

```
Input: root = [-15, 5, 6, -8, 1, 3, 9, 2, -3, N, N, N, N, N, 0, N, N, N, N, 4, -1, N, N, 10]

Output: 27
Explanation: 

The leaf nodes are 2, -3, 1, 4, and 10.
Some possible paths between leaves are:
2 -> -8 -> 5 -> 1 = 2 + (-8) + 5 + 1 = 0
-3 -> -8 -> 5 -> 1 = -3 + (-8) + 5 + 1 = -5
2 -> -8 -> 5 -> -15 -> 6 -> 3 = 2 + (-8) + 5 + (-15) + 6 + 3 = -7
1 -> 5 -> -15 -> 6 -> 9 -> 0 -> 4 = 1 + 5 + (-15) + 6 + 9 + 0 + 4 = 10
3 -> 6 -> 9 -> 0 -> -1 -> 10 = 3 + 6 + 9 + 0 + (-1) + 10 = 27
Hence, the maximum path sum is obtained from the path 3 -> 6 -> 9 -> 0 -> -1 -> 10, giving 27.

```

```
Input: root = [3, 4, 1, -10, 4, N, N] 
                         
Output: 12
Explanation:

The leaf nodes are -10, 4 (right child of 4), and 1.
Possible paths between leaf nodes are:
-10 -> 4 -> 4 = -10 + 4 + 4 = -2
-10 -> 4 -> 3 -> 1 = -10 + 4 + 3 + 1 = -2
4 -> 4 -> 3 -> 1 = 4 + 4 + 3 + 1 = 12
Hence, the maximum path sum is obtained from the path 4 -> 4 -> 3 -> 1, giving 12.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T05:55:02.826Z  

```py
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        # code here
        
        win = [float('-inf')]
        
        def dfs(node):
            if not node:
                return float('-inf')
            if not node.left and not node.right:
                return node.data
                
            l = dfs(node.left)
            r = dfs(node.right)
            
            if node.left and node.right:
                win[0] = max(win[0], l + r + node.data)
                return max(l, r) + node.data
                
            return (l if node.left else r) + node.data
            
        dfs(root)
        return win[0] if win[0] != float('-inf') else -1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-path-sum/1)