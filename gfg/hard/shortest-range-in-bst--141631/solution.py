''' Node Structure:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:

    def shortestRange(self, root):
        """code here"""
        
        nodes, q = [], deque([(root, 0)])
        while q:
            n, l = q.popleft()
            nodes.append((n.data, l))
            if n.left: q.append((n.left, l + 1))
            if n.right: q.append((n.right, l + 1))
            
        nodes.sort()
        K, covered, cnt = l + 1, 0, [0] * (l + 1)
        ans, left = [-10**9, 10**9], 0
        
        
        for r_val, r_l in nodes:
            if cnt[r_l] == 0:
                covered += 1
                
            cnt[r_l] += 1
            
            while covered == K:
                l_val, l_l = nodes[left]
                if r_val - l_val < ans[1] - ans[0]:
                    ans = [l_val, r_val]
                    
                cnt[l_l] -= 1
                if cnt[l_l] == 0:
                    covered -= 1
                    
                left += 1
                
        return ans
