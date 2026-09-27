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