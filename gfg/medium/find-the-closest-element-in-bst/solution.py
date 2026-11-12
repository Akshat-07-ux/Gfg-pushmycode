'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        # code here
        min = float('inf')
        cur = root
        
        while cur:
            diff = abs(cur.data - k)
            if diff < min:
                min = diff
                
            if cur.data == k:
                return 0
                
            elif k < cur.data:
                cur = cur.left
            else:
                cur = cur.right
                
        return min