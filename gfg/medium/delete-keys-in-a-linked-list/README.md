# Delete All Occurrences in a Linked list

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a single linked list  **head**  and an integer  **x.**  Your task is to deletes all occurences of a key x present in the linked list. The function should returns the  **head**  of the modified linked list.

 **Examples:** 

```
Input: head = 2->2->1->4->4, x = 4
Output: 2 2 1 
Explanation:
After deleting all occurrences of 4, the remaining nodes in the linked list are: 2 2 1. 
```

```
Input: head = 1->2->2->3->2->3, x = 2
Output: 1 3 3
Explanation: Given number to delete is 2.
First line of output contains the number of remaining elements in the list.
After deleting all occurrences of 2, we have elements in the list as 1, 3, and 3.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T16:04:41.835Z  

```py
"""Structure of a linked list node

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
class Solution:

    def deleteAllOccurances(self, head, x):
        # Code Here
        
        while head and head.data == x:
            head = head.next
            
            
        if not head:
            return None
            
        cur = head
        while cur and cur.next:
            if cur.next.data == x:
                cur.next = cur.next.next
                
            else:
                cur = cur.next
                
        return head
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/delete-keys-in-a-linked-list/1)