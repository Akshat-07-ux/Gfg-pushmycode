# Minimum Steps Required

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **str**  consisting of only two characters  **'a'**  and  **'b'**. You need to find the minimum steps required to make the string empty by removing consecutive  **a's**  and  **b's**.

 **Examples:** 

```
Input: str = "bbaaabb"
Output: 2
Explanation:
Operation 1: Removal of all a's modifies str to "bbbb".
Operation 2: Removal of all remaining b's makes str empty.
Therefore, the minimum number of operations required is 2.
```

```
Input: str = "aababaa"
Output: 3
Explanation:
Operation 1: Removal of b's modifies str to "aaabaa".
Operation 2: Removal of b's modifies str = "aaaaa".
Operation 3: Removal of all remaining a's makes str empty.
Therefore, the minimum number of operations required is 3.

```

 **Constraints:** 

- 1 <= str.length() <= 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-01T05:23:47.196Z  

```py
class Solution:
    def minSteps(self, str: str) -> int:
        # code here
        
        if not str:
            return 0
            
        blocks = 1
        
        for i in range(1, len(str)):
            if str[i] != str[i - 1]:
                blocks += 1
                
        return (blocks // 2) + 1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-steps-required--170647/1)