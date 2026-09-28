# Insertion Sort Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the  **head** of a singly linked list, sort the linked list in non-decreasing order using the  **Insertion Sort**  algorithm and return the head of the sorted list.

 **Examples:** 

```
Input: 

Output: 2 -> 5 -> 8 -> 9
Explanation: After sorting the given linked list, the resultant list will be:

```

```
Input:

Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60
Explanation: After sorting the given linked list, the resultant list will be:

```

 **Constraints:** 

1 ≤ number of nodes ≤ 103
1 ≤ node->val ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T06:26:12.652Z  

```py
# Structure of linked list Node
# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSort(self, head):
        # code here
        if not head or not head.next:
            return head
            
        dummy = Node(0)
        cur = head
        
        while cur:
            prev = dummy
            nxt = cur.next
            
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
                
            cur.next = prev.next
            prev.next = cur
            
            cur = nxt
            
        return dummy.next
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/insertion-sort-list/1)