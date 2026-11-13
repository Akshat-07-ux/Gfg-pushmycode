# Minimum Operation To Make Equal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array  **arr[]**  consisting of n elements. At each operation you can select any one element and  **increase** rest of n-1 elements by 1. Your task is to make all elements equal performing such operation as many times as needed. Find the  **minimum** number of operations needed for this.

 **Examples:** 

```
Input: arr[] = [1, 2, 3]
Output: 3
Explanation:
Operation 1: Increase all except 3rd, we get 2, 3, 3
Operation 2: Increase all except 3rd, we get 3, 4, 3
Operation 3: Increase all except 2nd, we get 4, 4, 4
```

```
Input: arr[] = [4, 3, 4]
Output: 2
Explanation:
Operation 1: Increase all except 3rd, we get 5, 4, 4
Operation 2: Increase all except 1st, we get 5, 5, 5
```

 **Constraint:** 
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T08:51:21.366Z  

```py
class Solution:
    def minOps(self, arr):
        # code here
        
        mini = min(arr)
        return sum(arr) - len(arr) * mini

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-operation-to-make-equal/1)