# Count Pairs Violating  BST Property

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given  **root**  of a binary tree in which all node values are  **distinct**, count pairs of nodes that violate any of the following Binary Search Tree (BST) properties.

- All values in the left subtree are strictly smaller.
- All values in the right subtree are strictly greater.

 **Examples:** 

```
Input: root[] = [10, 50, 40, N, N, 20, 30]

Output: 5
Explanation: Pairs violating BST property are:-
(10, 50), 10 should be greater than its left child value.
(40, 30), 40 should be less than its right child value.
(50, 20), (50, 30) and (50, 40), maximum of left subtree of 10 is 50 greater than 20, 30 and 40 of its right subtree.
```

```
Input: root[] = [80, 40, 30, 70, N, 60, 50]

Output: 10
Explanation: There are total 10 pairs (80, 30), (80, 60), (80, 50), (30, 60), (40, 70), (40, 30), (40, 50), (70, 30), (70, 60), (70, 50) which violate the BST properties.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T08:30:09.846Z  

```py

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
                
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/pairs-violating-bst-property--212515/1)