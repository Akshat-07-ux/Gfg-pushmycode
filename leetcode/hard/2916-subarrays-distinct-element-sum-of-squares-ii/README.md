# Subarrays Distinct Element Sum of Squares II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a  **0-indexed** integer array `nums`.

The  **distinct count**  of a subarray of `nums` is defined as:

- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return  *the sum of the  **squares**  of  **distinct counts**  of all subarrays of* `nums`.

Since the answer may be very large, return it  **modulo**  `109 + 7`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

```

 **Example 2:** 

```
Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 4363 ms (beats 58.62%)  
**Memory:** 123.9 MB (beats 20.69%)  
**Submitted:** 2026-10-16T05:12:15.734Z  

```py
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD, n = 10**9 + 7, len(nums)
        s, sq, lzy = [0] * (4 * n), [0] * (4 * n), [0] * (4 * n)
        
        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                ln = r - l + 1
                sq[node] = (sq[node] + 2 * v * s[node] + v * v * ln) % MOD
                s[node] = (s[node] + v * ln) % MOD
                lzy[node] = (lzy[node] + v) % MOD
                return
            if lzy[node]:
                lz, mid, left, right = lzy[node], (l + r) // 2, 2 * node, 2 * node + 1
                for ch, ln in ((left, mid - l + 1), (right, r - mid)):
                    sq[ch] = (sq[ch] + 2 * lz * s[ch] + lz * lz * ln) % MOD
                    s[ch] = (s[ch] + lz * ln) % MOD
                    lzy[ch] = (lzy[ch] + lz) % MOD
                lzy[node] = 0
            mid = (l + r) // 2
            if ql <= mid: update(2 * node, l, mid, ql, qr, v)
            if qr > mid: update(2 * node + 1, mid + 1, r, ql, qr, v)
            s[node], sq[node] = (s[2 * node] + s[2 * node + 1]) % MOD, (sq[2 * node] + sq[2 * node + 1]) % MOD

        last, ans = {}, 0
        for r, x in enumerate(nums):
            l = last.get(x, -1) + 1
            last[x] = r
            update(1, 0, n - 1, l, r, 1)
            ans = (ans + sq[1]) % MOD
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)