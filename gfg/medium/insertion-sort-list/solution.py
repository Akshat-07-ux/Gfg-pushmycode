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