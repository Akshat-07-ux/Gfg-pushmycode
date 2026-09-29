# Most Frequent of Two

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[]**  and two elements  **x**  and  **y**, return the element that occurs more frequently. If both elements have the same frequency, return the smaller one.

 **Examples:** 

```
Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5], x = 4, y = 5
Output: 4
Explanation: frequency of 4 is 4.frequency of 5 is 1.Since 4>1 so return 4

```

```
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], x = 1, y = 7
Output: 1
Explanation: frequency of 1 is 1.frequency of 7 is 1.Since 1 < 7, return 1.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T07:13:19.126Z  

```py
class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        zx, zy = 1, 1
        
        for val in arr:
            if val == x:
                zx += 1
                
            elif val == y:
                zy += 1
                
        if zx > zy:
            return x
            
        elif zy > zx:
            return y
            
        else:
            return min(x, y)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/who-has-the-majority/1)