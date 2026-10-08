# Range Covering All Levels In BST

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a BST (Binary Search Tree), find the shortest range  **[x, y]**, such that, at least one node of every level of the BST lies in the range. If there are multiple ranges with the same gap (i.e.  **(y-x)**) return the range with the smallest **x**.

 **Examples:** 

```
Input: root : [8, 3, 10, 2, 6, N, 14, N, N, 4, 7, 12, N, N, N, N, N, 11, 13]

Output: [6, 11]
Explanation: Level order traversal of the tree is [8], [3, 10], [2, 6, 14], [4, 7, 12], [11, 13]. The shortest range which satisfies the above mentioned condition is [6, 11]. 
```

```
Input: root : [12, N, 13, N, 14, N, 15, N, 16]

Output: [12, 16]
Explanation: Each level contains one node, so the shortest range is [12, 16].
```

 **Constraints:** 
1 ≤ n ≤ 2 * 105
1 ≤ Node Value ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T07:27:35.910Z  

```py
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

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/shortest-range-in-bst--141631/1)