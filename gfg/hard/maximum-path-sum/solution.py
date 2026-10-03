'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        # code here
        
        win = [float('-inf')]
        
        def dfs(node):
            if not node:
                return float('-inf')
            if not node.left and not node.right:
                return node.data
                
            l = dfs(node.left)
            r = dfs(node.right)
            
            if node.left and node.right:
                win[0] = max(win[0], l + r + node.data)
                return max(l, r) + node.data
                
            return (l if node.left else r) + node.data
            
        dfs(root)
        return win[0] if win[0] != float('-inf') else -1