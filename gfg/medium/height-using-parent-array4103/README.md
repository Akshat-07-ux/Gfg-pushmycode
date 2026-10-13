# Height Using Parent Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a parent array a **rr[]**  representing a binary tree, where arr[i] denotes the parent of node i, return the  **height**  of the tree. The root is the unique node whose parent is -1.

 **Note:**  The height of a tree is the number of nodes on the longest path from the root to a leaf.

 **Examples:** 

```
Input: arr[] = [-1, 0, 0, 1, 1, 3, 5]
Output: 5
Explanation: The longest path from the root node 0 to a leaf is 0 -> 1 -> 3 -> 5 -> 6, which contains 5 nodes. 
Therefore, the height of the tree is 5.

```

```
Input: arr[] = [-1, 0, 0]
Output: 2
Explanation: The longest root-to-leaf path is either 0 -> 1 or 0 -> 2, each containing 2 nodes. Therefore, the height of the tree is 2.
 
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
-1 ≤ arr[i] ≤ arr.size()

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T06:25:29.529Z  

```py
class Solution:
    def findHeight(self, arr):
        # code here
        
        n = len(arr)
        memo = {}
        
        def get_height(node):
            if node == -1:
                return 0
                
            if node in memo:
                return memo[node]
                
            memo[node] = 1 + get_height(arr[node])
            return memo[node]
            
        max_h = 0
        for i in range(n):
            max_h = max(max_h, get_height(i))
            
            
        return max_h
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/height-using-parent-array4103/1)