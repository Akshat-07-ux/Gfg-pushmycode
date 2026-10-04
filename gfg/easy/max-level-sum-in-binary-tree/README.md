# Max Level Sum in Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the  **root** of a binary tree, return the  **maximum** sum of values among all levels of the tree. A level sum is the sum of all node values at the same depth.

 **Examples:** 

```
Input: root = [4, 2, -5, -1, 3, -2, 6]

Output: 6
Explanation: Sum of all nodes of 0th level is 4. 
Sum of all nodes of 1st level is 2 - 5 = -3. 
Sum of all nodes of 2nd level is -1 + 3 -2 + 6 = 6. 
Hence, maximum sum is 6.
```

```
Input: root = [1, 2, 3, 4, 5, N, 8, N, N, N, N, N, N, 6, 7]    

Output: 17
Explanation: Sum of all nodes of 0th level is 1. 
Sum of all nodes of 1st level is 2 + 3 = 5. 
Sum of all nodes of 2nd level is 4 + 5 + 8 = 17. 
Sum of all nodes of 3rd level is 6 + 7 = 13. 
Hence, maximum sum is 17.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T15:26:37.380Z  

```py
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def maxLevelSum(self, root):
        # Code here
        
        if not root:
            return 0
            
        level, max_sum = [root], float('-inf')
        
        while level:
            max_sum = max(max_sum, sum(node.data for node in level))
            level = [child for node in level for child in (node.left, node.right) if child]
        return max_sum
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1)