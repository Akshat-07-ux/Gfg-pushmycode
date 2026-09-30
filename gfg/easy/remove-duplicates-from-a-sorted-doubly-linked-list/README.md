# Remove duplicates from a sorted DLL

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a doubly linked list of  **n** nodes sorted by values, remove duplicate nodes present in the linked list.

 **Examples:** 

```
Input: head: 1<->1<->1<->2<->3<->4
Output: 1<->2<->3<->4
Explanation: Only the first occurance of node with value 1 is retained along with other distinct values. 
```

```
Input: head: 1<->2<->2<->3<->3<->4<->4
Output: 1<->2<->3<->4
Explanation:
Only the first occurance of nodes with values 2, 3 and 4 are retained, rest repeating nodes are deleted.
```

 **Constraint:** 
1 ≤ n ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T04:37:54.536Z  

```py
# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        if not headRef:
            return None
           
        cur = headRef
        while cur and cur.next:
            if cur.data == cur.next.data:
                nxt_node = cur.next.next
                cur.next = nxt_node
                
                if nxt_node:
                    nxt_node.prev = cur
                    
            else:
                cur = cur.next
                
        return headRef
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1)