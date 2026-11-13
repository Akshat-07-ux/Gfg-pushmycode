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