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