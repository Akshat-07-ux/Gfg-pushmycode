# Maximum Weight Transformation of String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  consisting only of the characters ' **A** ' and ' **B** ', you can toggle any character. A toggle changes 'A' to 'B' or 'B' to 'A'.

The weight of a string is calculated using the following rules:

- An alternating adjacent pair ("AB" or "BA") contributes 4 to the weight.
- Each character can belong to at most one pair, so the pairs must not overlap.
- Every character that does not belong to any pair contributes 1 to the weight.
- Each toggle performed decreases the total weight by 1.

Therefore, Weight = Weight of alternating adjacent pairs + Weight of characters that do not belong to any pair - Number of Toggles

You can toggle characters to make adjacent characters different and form pairs. Find the maximum possible weight obtainable from the string by choosing pairs and toggling characters optimally.

 **Examples:** 

```
Input: s = "AA"
Output: 3
Explanation: The possible transformed strings are "AA", "AB", "BA", and "BB". The strings "AB" and "BA" each contain one alternating adjacent pair, contributing 4 to the weight. One toggle is required to obtain either string from "AA", reducing the weight by 1. Therefore, the maximum weight is 4 - 1 = 3.
```

```
Input: s = "ABB"
Output: 5
Explanation: Possible transformations are "ABB", "ABA", "AAB", "AAA", "BBB", "BBA", "BAB" and "BAA". The original string "ABB" contains the alternating adjacent pair "AB", contributing 4 to the weight, while the remaining character 'B' contributes 1. No toggles are required. Therefore, the maximum weight is 4 + 1 = 5.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T04:53:28.600Z  

```py
class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        
        dp = [-float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == -float('inf'):
                continue
            
            if i + 1 <= n:
                dp[i + 1] = max(dp[i + 1], dp[i])
                
            if i + 2 <= n:
                    
                togg_ab = (0 if s[i] == 'A' else 1) + (0 if s[i + 1] == 'B' else 1)
                dp[i + 2] = max(dp[i + 2], dp[i] + 2 - togg_ab)
                    
                togg_ba = (0 if s[i] == 'B' else 1) + (0 if s[i + 1] == 'A' else 1)
                dp[i + 2] = max(dp[i + 2], dp[i] + 2 - togg_ba)
                    
        return n + dp[n]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-weight-transformation-of-a-given-string3551/1)