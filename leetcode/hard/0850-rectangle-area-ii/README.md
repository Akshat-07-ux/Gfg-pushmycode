# Rectangle Area II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a 2D array of axis-aligned `rectangles`. Each `rectangle[i] = [xi1, yi1, xi2, yi2]` denotes the `ith` rectangle where `(xi1, yi1)` are the coordinates of the  **bottom-left corner**, and `(xi2, yi2)` are the coordinates of the  **top-right corner**.

Calculate the  **total area**  covered by all `rectangles` in the plane. Any area covered by two or more rectangles should only be counted  **once**.

Return  *the  **total area***. Since the answer may be too large, return it  **modulo**  `109 + 7`.

 

 **Example 1:** 

```
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.

```

 **Example 2:** 

```
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is 49.

```

 

 **Constraints:** 

- 1 <= rectangles.length <= 200
- rectanges[i].length == 4
- 0 <= xi1, yi1, xi2, yi2 <= 109
- xi1 <= xi2
- yi1 <= yi2
- All rectangles have non zero area.

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 13.47%)  
**Memory:** 19.4 MB (beats 69.95%)  
**Submitted:** 2026-10-08T07:34:33.743Z  

```py
class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        X = sorted(set([x for r in rectangles for x in (r[0], r[2])]))
        x_idx = {x: i for i, x in enumerate(X)}
        
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 1, x_idx[x1], x_idx[x2]))
            events.append((y2, -1, x_idx[x1], x_idx[x2]))
        events.sort()
        
        counts = [0] * len(X)
        last_y = ans = 0
        
        for y, typ, i1, i2 in events:
            ans += sum(X[i+1] - X[i] for i in range(len(X)-1) if counts[i] > 0) * (y - last_y)
            for i in range(i1, i2):
                counts[i] += typ
            last_y = y
            
        return ans % (10**9 + 7)
```

---

[View on LeetCode](https://leetcode.com/problems/rectangle-area-ii/)