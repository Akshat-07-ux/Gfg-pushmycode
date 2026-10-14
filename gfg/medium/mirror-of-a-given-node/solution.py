''' Structure of binary tree Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''


class Solution:

    def findMirror(self, root, k):
        """code here"""
        
        if not root:
            return -1
            
        def get_mirror(l, r):
            if not l or not r:
                return -1
                
            if l.data == k:
                return r.data
                
            if r.data == k:
                return l.data
                
            return get_mirror(l.left, r.right) if get_mirror(l.left, r.right) != -1 else get_mirror(l.right, r.left)
            
        if root.data == k:
            return root.data
            
        return get_mirror(root.left, root.right)