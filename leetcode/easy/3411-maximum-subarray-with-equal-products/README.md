# Maximum Subarray With Equal Products

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array of  **positive**  integers `nums`.

An array `arr` is called  **product equivalent**  if `prod(arr) == lcm(arr) * gcd(arr)`, where:

- prod(arr) is the product of all elements of arr.
- gcd(arr) is the GCD of all elements of arr.
- lcm(arr) is the LCM of all elements of arr.

Return the length of the  **longest**   **product equivalent**  subarray of `nums`.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [1,2,1,2,1,1,1]

 **Output:**  5

 **Explanation:**  

The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

 **Example 2:** 

 **Input:**  nums = [2,3,4,5,6]

 **Output:**  3

 **Explanation:**  

The longest product equivalent subarray is `[3, 4, 5].`

 **Example 3:** 

 **Input:**  nums = [1,2,3,1,4,5,1]

 **Output:**  5

 

 **Constraints:** 

- 2 <= nums.length <= 100
- 1 <= nums[i] <= 10

## Solution

**Language:** Python  
**Runtime:** 37 ms (beats 44.58%)  
**Memory:** 19.4 MB (beats 30.42%)  
**Submitted:** 2026-11-24T07:15:12.595Z  

```py
import math
from typing import List
class Solution:
    def maxLength(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            c_g = 0
            c_l = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                c_g = math.gcd(c_g, x)
                c_l = math.lcm(c_l, x)

                if prod == c_l * c_g:
                    ans = max(ans, j - i + 1)

        return ans



        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/)