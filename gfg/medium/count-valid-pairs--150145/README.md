# Connected Pairs in Bitwise AND Graph

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A graph has n nodes, where node i has weight w[i]. An undirected edge exists between nodes i and j (i ≠ j) if and only if w[i] & w[j] ≠ 0, where & is the bitwise AND operator. A pair of nodes (i, j) with i < j is valid if a path exists between them. Find the total number of valid pairs in the graph

 **Examples:** 

```
Input: w[] = [1, 2, 3]
Output: 3
Explanation: The graph forms a single connected component containing edges between the nodes (1, 3), (2, 3). Therefore, there is a path between all three nodes. Hence, the total number of valid pairs in the graph is 3.
```

```
Input: w[] = [1, 5, 2, 10]
Output: 2
Explanation: The graph consists of two connected components: 
- Component 1 includes the edge between 1st and 2nd node. (1 & 5 = 1)
- Component 2 includes the edge between 3rd and 4th node. (2 & 10 = 2)
Hence, the total number of valid pairs in the graph is 2.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T05:42:14.878Z  

```py
from collections import Counter
class Solution:
    def cntValid(self, w: list[int]) -> int:
        # code here
        p = list(range(len(w)))
        
        def find(i):
            while p[i] != i:
                p[i] = p[p[i]]
                
                i = p[i]
            return i
            
        for b in range(31):
            first = -1
            for i, x in enumerate(w):
                if (x >> b) & 1:
                    if first < 0:
                        first = i
                    else:
                        p[find(first)] = find(i)
                        
        return sum(c * (c - 1) // 2 for c in Counter(find(i) for i in range(len(w))).values())
                        
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-valid-pairs--150145/1)