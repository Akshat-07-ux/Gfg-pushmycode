'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def maxLevelSum(self, root):
        # Code here
        
        if not root:
            return 0
            
        level, max_sum = [root], float('-inf')
        
        while level:
            max_sum = max(max_sum, sum(node.data for node in level))
            level = [child for node in level for child in (node.left, node.right) if child]
        return max_sum
        