# Optimal File Merge

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **files[]**, where  **files[i]**  represents the size of the i-th file, merge all the files into a single file with the minimum total computation cost.

The cost of merging two files of sizes  **x** and  **y** is  **x + y**. After merging, a new file of size **x + y**  is created, which can be merged further with other files.

Return the minimum total cost required to merge all the files.

 **Note:**  It is guaranteed that the minimum total computation cost fits within a 32-bit signed integer.

 **Examples:** 

```
Input: files[] = [3, 2, 4]
Output: 14
Explanation: There are different ways to combine these files. Optimal method is given below:

```

```
Input: files[] = [2, 3, 6, 5, 7, 4]
Output: 68
Explanation: There are different ways to combine these files. Optimal method is given below:

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T07:00:29.035Z  

```py
import heapq
class Solution:
    def minComputation(self, files):
        # code here
        
        if not files:
            return 0
            
            
        heapq.heapify(files)
        total = 0
        
        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)
            
            merged = first + second
            total += merged
            
            heapq.heappush(files, merged)
            
        return total
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/optimal-file-merge/1)