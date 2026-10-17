# Count Graphs with n Vertices

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n**  representing number of vertices. Find out how many  **undirected graphs** (not necessarily connected) can be constructed out of a given n number of vertices.

 **Examples:** 

```
Input: 2
Output: 2
Explanation: One graph would have both vertices connected and other not
```

```
Input: 3
Output: 8
Explanation:
 
```

```
Input: 5
Output: 1024
```

 **Constraints:** 

1<=n<=10

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T06:18:01.097Z  

```py
class Solution:
    def count(self, n):
        # code here
        
        total_edges = n * (n - 1) // 2
        return 1 << total_edges
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/graph-and-vertices/1)