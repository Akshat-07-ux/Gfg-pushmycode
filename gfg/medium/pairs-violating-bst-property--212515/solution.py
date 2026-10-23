
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def pairsViolatingBST(self, root):
        # code here
        
        vals = []
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            vals.append(curr.data)
            curr = curr.right
            
        def count_inversions(arr):
            if len(arr) <= 1:
                return arr, 0
                
            mid = len(arr) // 2
            left, left_inv = count_inversions(arr[:mid])
            right, right_inv = count_inversions(arr[mid:])
            
            res = []
            i = j = 0
            inv = left_inv + right_inv
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                    
                else:
                    res.append(right[j])
                    j += 1
                    inv += len(left) - i
                    
            res.extend(left[i:])
            res.extend(right[j:])
            
            return res, inv
        _, total_inversions = count_inversions(vals)
        return total_inversions
                
        