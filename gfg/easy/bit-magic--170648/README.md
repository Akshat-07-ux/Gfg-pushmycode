# Minimum XOR Operations for Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary array  **arr[]**, find the minimum number of operations required to make it palindrome. In one operation, you may choose two different indices i and j and replace both values with their bitwise XOR: arr[i] = arr[j] = arr[i] ^ arr[j].

 **Examples:** 

```
Input: arr[] = {1, 0, 0, 0}
Output: 1
Explanation: We can take index 0 and 3 and apply the operation. Array becomes {1, 0, 0, 1}. Now the condition is satisfied 
```

```
Input: arr[] = {1, 0, 1}
Output: 0
Explanation: condition is satisfied initially. So no operation is required in this case.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-04T01:21:24.575Z  

```py
class Solution:
    def minOps(self, arr: list[int]) -> int:
        # code here
        
        n = len(arr)
        count = 0
        
        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                count += 1
                
        return (count + 1) // 2

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/bit-magic--170648/1)