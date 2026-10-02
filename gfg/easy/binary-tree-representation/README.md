# Binary Tree Representation

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array  **nodes[]**  of size  **n**, where each element represents the value of a node in the level-order traversal of a complete binary tree, construct the  **complete binary tree**  and return its  **root** node.

 **Example:** 

```
Input: nodes[] = [1, 2, 3, 4, 5, 6, 7]
Output: 

Explanation: We start from the root and fill the tree level by level. First 1 becomes the root, then 2 and 3 become its children, and then 4, 5, 6, 7 fill the next level from left to right.

Input: nodes[] = [10, 20, 30, 40, 50]
Output:

Explanation: We start from the root and fill the tree level by level. 10 is the root, 20 and 30 are its children, and 40 and 50 are placed as the left and right children of 20.
```

 **Constraints:** 

1 ≤ n ≤ 103
0 ≤ nodes[i] ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T06:09:59.584Z  

```py
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, nodes):
        # code here
        l = len(nodes)
        
        if not nodes:
            return None
            
        tree_nodes = [Node(val) for val in nodes]
        
        for i in range(l):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            
            if left_index < l:
                tree_nodes[i].left = tree_nodes[left_index]
                
            if right_index < l:
                tree_nodes[i].right = tree_nodes[right_index]
                
        return tree_nodes[0]
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/binary-tree-representation/1)