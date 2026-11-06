# Balanced Binary Tree Counter

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a height  **h**, find the maximum number of distinct balanced binary trees of height exactly h.

A binary tree is balanced if, for every node, the heights of its left and right subtrees differ by at most 1. A tree with a single node has height 1. An empty tree has height 0.

 **Note:**  Since the answer can be very large, return it modulo 109 + 7.

 **Examples:** 

```
Input: h = 1
Output: 1
Explanation: Only one tree of height 1 exists i.e. a single node.
```

```
Input: h = 2
Output: 3 
Explanation: 3 distinct balanced trees of height 2 exist.

```

```
Input: h = 3
Output: 15
Explanation: 15 distinct balanced trees of height 3 exist.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T15:42:38.974Z  

```py
class Solution:
    def countBT(self, h: int) -> int:
        # code here
        MOD = 1000000007
        
        if h <= 0:
            return 0
            
        if h == 1:
            return 1
            
        prev2 = 1
        prev1 = 1
        
        for _ in range(2, h + 1):
            current = (prev1 * prev1 + 2 * prev1 * prev2) % MOD
            prev2 = prev1
            prev1 = current
            
        return prev1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/bbt-counter4914/1)