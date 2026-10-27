# Last Person After Repeated K Removals from Ends

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers n and k, consider people numbered from 1 to n. Repeatedly remove the first k remaining people, followed by the last k people from the updated sequence. If fewer than k people remain at any step, remove all of them.

Return the number of the last person removed.

 **Examples:** 

```
Input: n = 9, k = 3
Output: 6
Explanation: Starting queue will like [1, 2, 3, 4, 5, 6, 7, 8, 9].
After the first distribution queue will look like [4, 5, 6, 7, 8, 9].
And after the second distribution queue will look like [4, 5, 6]. 
The last person will be 6.
```

```
Input: n = 5, k = 1
Output: 3
Explanation: Queue start as [1, 2, 3, 4, 5] -> [2, 3, 4, 5] -> [2, 3, 4] -> [3, 4] -> [3]. Last person will be 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T04:55:34.615Z  

```py
from collections import deque
class Solution:
    def distributeTicket(self, n: int, k: int) -> int:
        # Code Here
        
        dq = deque(range(1, n + 1))
        last_removed = -1
        
        while dq:
            
            for _ in range(min(k, len(dq))):
                last_removed = dq.popleft()
                
            if not dq:
                break
            
            for _ in range(min(k, len(dq))):
                last_removed = dq.pop()
                
        return last_removed
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/ticket-counter-2731/1)