# Adding Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Consider an array arr[] of size n, initially containing all zeros. You are also given an array  **updates[]**  of k positive integers.

For each value j in updates[], add 1 to every element arr[i] whose index satisfies i ≥ j.

The indices in updates[] are 1-based.

Perform all the updates and modify arr[] accordingly.

 **Examples:** 

```
Input: n = 3, updates[] = [1, 1, 2, 3]
Output: [2, 3, 4]
Explanation: Initially, arr[] = [0, 0, 0]. After the first update 1, the array becomes [1, 1, 1]. 
After the second update 1, it becomes [2, 2, 2]. The update 2 increments all elements from index 2 onward, giving [2, 3, 3]. Finally, the update 3 increments the element at index 3, resulting in [2, 3, 4].
```

```
Input: n = 2, updates[] = [1, 1, 1]
Output: [3, 3] 
Explanation: Initially the array is [0, 0]. After the first 1, it becomes [1, 1]. 
After the second 1 it becomes [2, 2]. After the third 1, it becomes [3, 3].
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T06:19:01.640Z  

```py
class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here
        
        diff = [0] * (n + 1)
        for x in updates:
            diff[x - 1] += 1
            diff[n] -= 1
            
        ans = [0] * n
        run_sum = 0
        for i in range(n):
            run_sum += diff[i]
            ans[i] = run_sum
            
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/adding-ones3628/1)