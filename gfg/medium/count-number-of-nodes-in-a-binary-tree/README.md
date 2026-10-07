# Size of a Complete  Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given the root of a  **complete**  binary tree. Your task is to find the  **count** of nodes. A complete binary tree is a binary tree whose, all levels except the last one are completely filled, the last level may or may not be completely filled and Nodes in the last level are as left as possible.

 **Note**  : Design an algorithm that runs better than O(n).

 **Example:** 

```
Input: Root of the below tree  

Output: 7
```

```
Input: Root of the below tree  

Output: 5
```

**Constraints:
**0 ≤ N (number of nodes) ≤ 5 * 104
0 ≤ value of nodes ≤ 5 * 104
The tree is guaranteed to be complete.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T06:03:33.630Z  

```py
class Solution:

    def countNodes(self, root):
        # code here
        
        if not root:
            return 0
            
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
                
        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
                
        lh = get_left_height(root)
        rh = get_right_height(root)
            
        if lh == rh:
            return (1 << lh) - 1
                
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-number-of-nodes-in-a-binary-tree/1)