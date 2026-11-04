# Minimum Operations to Make Elements Within K Subarrays Equal

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` and two integers, `x` and `k`. You can perform the following operation any number of times (**including zero**):

- Increase or decrease any element of nums by 1.

Return the  **minimum**  number of operations needed to have  **at least**  `k`  *non-overlapping subarrays*  of size  **exactly**  `x` in `nums`, where all elements within each subarray are equal.

 

 **Example 1:** 

 **Input:**  nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

 **Output:**  8

 **Explanation:** 

- Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
- Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
- Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

 **Example 2:** 

 **Input:**  nums = [9,-2,-2,-2,1,5], x = 2, k = 2

 **Output:**  3

 **Explanation:** 

- Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
- Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

 

 **Constraints:** 

- 2 <= nums.length <= 105
- -106 <= nums[i] <= 106
- 2 <= x <= nums.length
- 1 <= k <= 15
- 2 <= k * x <= nums.length

## Solution

**Language:** Python  
**Runtime:** 3122 ms (beats 82.69%)  
**Memory:** 66.1 MB (beats 7.69%)  
**Submitted:** 2026-11-04T01:50:28.909Z  

```py
from typing import List
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        left, right = [], []
        delayed = {}
        size_l = size_r = 0
        sum_l = sum_r = 0

        def prune(heap):
            while heap:
                v = -heap[0] if heap is left else heap[0]
                if delayed.get(v, 0):
                    heappop(heap)
                    delayed[v] -= 1
                    if delayed[v] == 0:
                        del delayed[v]
                else:
                    break

        def balance():
            nonlocal size_l, size_r, sum_l, sum_r

            if size_l > size_r + 1:
                prune(left)
                v = -heappop(left)
                size_l -= 1
                sum_l -= v
                heappush(right, v)
                size_r += 1
                sum_r += v

            elif size_l < size_r:
                prune(right)
                v = heappop(right)
                size_r -= 1
                sum_r -= v
                heappush(left, -v)
                size_l += 1
                sum_l += v

        def add(v):
            nonlocal size_l, size_r, sum_l, sum_r

            prune(left)

            if not left or v <= -left[0]:
                heappush(left, -v)
                size_l += 1
                sum_l += v
            else:
                heappush(right, v)
                size_r += 1
                sum_r += v

            balance()

        def remove(v):
            nonlocal size_l, size_r, sum_l, sum_r

            prune(left)
            prune(right)

            delayed[v] = delayed.get(v, 0) + 1

            if v <= -left[0]:
                size_l -= 1
                sum_l -= v
                if v == -left[0]:
                    prune(left)
            else:
                size_r -= 1
                sum_r -= v
                if right and v == right[0]:
                    prune(right)

            balance()

        costs = []

        for i, v in enumerate(nums):
            add(v)

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                prune(left)
                m = -left[0]
                costs.append(m * size_l - sum_l + sum_r - m * size_r)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for j in range(1, k + 1):
            for i in range(x, n + 1):
                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i - x][j - 1] + costs[i - x]
                )

        return dp[n][k]
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)