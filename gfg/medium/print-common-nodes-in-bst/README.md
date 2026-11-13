# Common Nodes in Two BSTs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the roots  **r1**  and  **r2** of two Binary Search Trees (BST), find all nodes that are present in both trees i.e. the intersection nodes of the two BSTs.

Return the common node values in sorted order.

 **Examples:** 

```
Input: r1 = [5, 1, 10, 0, 4, 7, N, N, N, N, N, N, 9], r2 = [10, 7, 20, 4, 9, N, N]  

Output: [4, 7, 9, 10]
Explanation: The values present in both BSTs are 4, 7, 9, and 10. Hence, the answer is [4, 7, 9, 10].
```

```
Input: r1 = [10, 2, 11, 1, 3, N, N], r2 = [2, 1, 3]

Output: [1, 2, 3]
Explanation: The values 1, 2, and 3 are present in both BSTs. Hence, the answer is [1, 2, 3].
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T08:43:57.822Z  

```py
''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        # code here
        stack1, stack2 = [], []
        
        cur1, cur2 = r1, r2
        result = []
        
        while (stack1 or cur1) and (stack2 or cur2):
            
            while cur1:
                stack1.append(cur1)
                cur1 = cur1.left
                
            while cur2:
                stack2.append(cur2)
                cur2 = cur2.left
                
            if not stack1 or not stack2:
                
                break
            
            node1 = stack1[-1]
            node2 = stack2[-1]
            
            if node1.data == node2.data:
                result.append(node1.data)
                stack1.pop()
                stack2.pop()
                cur1 = node1.right
                cur2 = node2.right
                
            elif node1.data < node2.data:
                stack1.pop()
                cur1 = node1.right
                
            else:
                stack2.pop()
                cur2 = node2.right
                
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-common-nodes-in-bst/1)