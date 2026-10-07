class Solution:

    def countNodes(self, root):
        # code here
        
        if not root:
            return 0
            
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
                
        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
                
        lh = get_left_height(root)
        rh = get_right_height(root)
            
        if lh == rh:
            return (1 << lh) - 1
                
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)