# Sum of Sortable Integers

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` of length `n`.

An integer `k` is called  **sortable**  if `k`  **divides**  `n` and you can sort `nums` in  **non-decreasing**  order by sequentially performing the following operations:

- Partition nums into consecutive subarrays of length k.
- Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers `k`.

 

 **Example 1:** 

 **Input:**  nums = [3,1,2]

 **Output:**  3

 **Explanation:** ​​​​​​​

- For n = 3, possible divisors are 1 and 3.
- For k = 1: each subarray has one element. No rotation can sort the array.
- For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
- Only k = 3 is sortable. Hence, the answer is 3.

 **Example 2:** 

 **Input:**  nums = [7,6,5]

 **Output:**  0

 **Explanation:** 

- For n = 3, possible divisors are 1 and 3.
- For k = 1: each subarray has one element. No rotation can sort the array.
- For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
- No k is sortable. Hence, the answer is 0.

 **Example 3:** 

 **Input:**  nums = [5,8]

 **Output:**  3

 **Explanation:** ​​​​​​​

- For n = 2, possible divisors are 1 and 2.
- Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

 

 **Constraints:** 

- 1 <= n == nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 409 ms (beats 89.01%)  
**Memory:** 33.3 MB (beats 32.97%)  
**Submitted:** 2026-10-20T07:19:11.096Z  

```py
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        total_sum = 0
        for k in divisors:
            valid = True
            for j in range(0, n, k):
                orig = nums[j : j + k]
                target = sorted_nums[j : j + k]

                if orig == target:
                    continue

                s_orig = '.'.join(map(str, orig))
                s_target = '.'.join(map(str, target))

                if s_target not in s_orig + '.' + s_orig:
                    valid = False
                    break

            if valid:
                total_sum += k

        return total_sum
```

---

[View on LeetCode](https://leetcode.com/problems/sum-of-sortable-integers/)