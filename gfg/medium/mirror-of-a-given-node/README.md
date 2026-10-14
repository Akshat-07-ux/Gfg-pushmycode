# Mirror of Node

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the  **root** of a binary tree and an integer  **k**, find the mirror node of the node with value k. The mirror node is the node at the corresponding position in the opposite subtree with respect to the root.

If no such node exists, return **-1**. 

 **Examples:** 

```
Input: root = [1, 2, 3, 4, 5, 6, 7], k = 4 
    
Output: 7
Explanation: You can see below that the mirror node of 4 is 7.

```

```
Input: root = [1, 2, 3, 4, 5], k = 4
 
Output: -1
Explanation: There is no mirror element present of 4.

```

```
Input: root = [1, 2, 3, 4, 5], k = 2
 
Output: 3
Explanation: Mirror of 2 is 3
```

 **Constraints:** 
1 ≤ number of nodes ≤ 104
1 ≤ node->data, k ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T05:34:01.930Z  

```py
''' Structure of binary tree Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''


class Solution:

    def findMirror(self, root, k):
        """code here"""
        
        if not root:
            return -1
            
        def get_mirror(l, r):
            if not l or not r:
                return -1
                
            if l.data == k:
                return r.data
                
            if r.data == k:
                return l.data
                
            return get_mirror(l.left, r.right) if get_mirror(l.left, r.right) != -1 else get_mirror(l.right, r.left)
            
        if root.data == k:
            return root.data
            
        return get_mirror(root.left, root.right)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/mirror-of-a-given-node/1)