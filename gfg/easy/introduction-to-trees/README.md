# Introduction to Trees

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **i**. Print the  **maximum number of nodes**  on level i of a binary tree.

 **Note** : The level of a binary tree starts with  **1**  (i.e., level 1 contains the root of the tree, level 2 contains the children of the root, and so on).

 **Examples:** 

```
Input: 5
Output: 16
Explanation: The maximum number of nodes at level 5 is 16.
```

```
Input: 1
Output: 1
Explanation: The maximum number of nodes at level 1 is 1.
```

**Constraints:
**1<= i <=20

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T12:52:33.338Z  

```py
class Solution:
    def countNodes(self, i):
        # Code here
        return 1 << (i - 1)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/introduction-to-trees/1)