# Page Faults in LRU

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sequence of pages in an array  **pages[]**  of length  **n**  and memory capacity  **c**, find the number of page faults using the Least Recently Used (LRU) page replacement algorithm.

A page fault occurs when a referenced page is not present in memory. When memory is full, the least recently used page is replaced by the new page.

 **Examples:** 

```
Input: c = 4, pages[] = [5, 0, 1, 3, 2, 4, 1, 0, 5]
Output: 8
Explanation: Page 5: not in memory, fault, memory = [5], faults = 1
Page 0: fault, memory = [5, 0], faults = 2
Page 1: fault, memory = [5, 0, 1], faults = 3
Page 3: fault, memory = [5, 0, 1, 3], faults = 4
Page 2: fault, replaces LRU page 5, memory = [0, 1, 3, 2], faults = 5
Page 4: fault, replaces LRU page 0, memory = [1, 3, 2, 4], faults = 6
Page 1: already in memory, memory = [3, 2, 4, 1], faults = 6
Page 0: fault, replaces LRU page 3, memory = [2, 4, 1, 0], faults = 7
Page 5: fault, replaces LRU page 2, memory = [4, 1, 0, 5], faults = 8
```

```
Input: c = 4, pages[] = [1, 1, 1, 1]
Output: 1
Explanation: Page fault occurs only for the first 1.
```

**Constraints:
**1 ≤ n ≤ 105
1 ≤ c ≤ 104
1 ≤ pages[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T03:37:43.630Z  

```py
class Solution:
    def pageFaults(self, pages, c):
        # code here
        
        memo = {}
        faults = 0
        
        for p in pages:
            if p in memo:
                del memo[p]
                memo[p] = True
                
            else:
                faults += 1
                if len(memo) == c:
                    oldest_page = next(iter(memo))
                    del memo[oldest_page]
                memo[p] = True
                
        return faults
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/page-faults-in-lru5603/1)