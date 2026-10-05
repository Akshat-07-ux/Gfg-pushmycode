# Count Leaves in a Perfect n-ary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Count leaf nodes in a perfect  **n-ary**  tree of height  **m**. A perfect n-ary tree is a specialized hierarchical data structure where every internal node has exactly n children, and all leaf nodes exist at the exact same depth.

 **Note:**  You have to return the answer module 109+7.

 **Examples:** 

```
Input: n = 2, m = 2
Output: 4
Explanation: A full Binary tree of height 2 has 4 leaf nodes. 
```

```
Input: n = 2, m = 1
Output: 2
Explanation: A full Binary tree of height 1 has 2 leaf nodes.
```

 **Constraints:** 
1 ≤ k, m ≤ 108

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T06:12:54.562Z  

```py
class Solution:
    def karyTree(self, n, m):
        # code here
        MOD = 10**9 + 7
        return pow(n, m, MOD)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/k-ary-tree1235/1)