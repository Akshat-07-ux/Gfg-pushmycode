# Towers and Jumps

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given  **n**  towers standing in a row from left to right, with two arrays:

- heights[]: heights[i] is the height of the i-th tower.
- jumps[]: jumps[i] is the maximum number of jumps allowed for the person starting at the i-th tower.

A person starts at every tower, so there are n people in total.

Jump rules:

- In one jump, a person moves to the nearest tower on the right whose height is strictly greater than the current tower's height.
- Towers that are shorter than or equal to the current tower are skipped.
- If no such tower exists, the person cannot jump further.

Also given an array  **queries[]**. For each queries[i], find the number of people who can reach a tower of height at least queries[i]. A person whose starting tower already has height at least queries[i] is also counted, without needing any jump.

 **Note:**  Towers and people are numbered from 1 in the explanations, and arrays are 0-indexed. Person k starts at tower k, which is heights[k-1].

 **Examples:** 

```
Input: heights[] = [2, 4, 3, 5], jumps[] =  [1, 2, 1, 3], queries[] = [3, 5]
Output: [4, 3]
Explanation:
Person 1 starts at tower 1 with height 2 and can jump to tower 2 with height 4.
Person 2 starts at tower 2 with height 4 and can jump to tower 4 with height 5.
Person 3 starts at tower 3 with height 3 and can jump to tower 4 with height 5.
Person 4 starts at tower 4 with height 5.
For query 3, all 4 people can reach a tower with height at least 3.
For query 5, persons 2, 3, and 4 can reach a tower with height at least 5.
```

```
Input: heights[] = [1, 2, 3], jumps[] =  [1, 1, 0], queries[] = [2, 3]
Output: [3, 2]
Explanation:
Person 1 starts at height 1 and can jump to height 2.
Person 2 starts at height 2 and can jump to height 3.
Person 3 starts at height 3 and cannot jump.
For query 2, all 3 people can reach a tower with height at least 2.
For query 3, persons 2 and 3 can reach a tower with height at least 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-18T05:42:27.315Z  

```py
from bisect import bisect_left
class Solution:

    def reachableCount(self, heights: list[int], jumps: list[int],
                       queries: list[int]) -> list[int]:
        """ code here """
        
        st, ans = [], []
        for i in range(len(heights) - 1, -1, -1):
            while st and heights[st[-1]] <= heights[i]:
                st.pop()
                
            s = min(jumps[i], len(st))
            ans.append(heights[st[-s]] if s else heights[i])
            
            st.append(i)
            
        ans.sort()
        return [len(heights) - bisect_left(ans, q) for q in queries]
        
        
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/towers-and-jumps--145804/1)