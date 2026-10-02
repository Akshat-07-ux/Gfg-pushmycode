# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, nodes):
        # code here
        l = len(nodes)
        
        if not nodes:
            return None
            
        tree_nodes = [Node(val) for val in nodes]
        
        for i in range(l):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            
            if left_index < l:
                tree_nodes[i].left = tree_nodes[left_index]
                
            if right_index < l:
                tree_nodes[i].right = tree_nodes[right_index]
                
        return tree_nodes[0]
        