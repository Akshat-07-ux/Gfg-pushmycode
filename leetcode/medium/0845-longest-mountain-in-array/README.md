# Longest Mountain in Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You may recall that an array `arr` is a  **mountain array**  if and only if:

- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that: arr[0] < arr[1] <... < arr[i - 1] < arr[i] arr[i] > arr[i + 1] >... > arr[arr.length - 1]

Given an integer array `arr`, return  *the length of the longest subarray, which is a mountain*. Return `0` if there is no mountain subarray.

 

 **Example 1:** 

```
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

```

 **Example 2:** 

```
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

```

 

 **Constraints:** 

- 1 <= arr.length <= 104
- 0 <= arr[i] <= 104

 

 **Follow up:** 

- Can you solve it using only one pass?
- Can you solve it in O(1) space?

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 81.34%)  
**Memory:** 20.5 MB (beats 17.88%)  
**Submitted:** 2026-10-03T12:53:23.837Z  

```py
class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        i = 1

        while i < n - 1:
            is_peak = arr[i - 1] < arr[i] > arr[i + 1]
            if not is_peak:
                i += 1
                continue

            left = i - 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            ans = max(ans, right - left + 1)
            i = right + 1

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-mountain-in-array/)