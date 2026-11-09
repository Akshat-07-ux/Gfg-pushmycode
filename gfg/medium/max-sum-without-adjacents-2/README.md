# Max Sum Without 3 Adjacent

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array arr of positive integers, find the maximum sum subsequence such that no three selected elements are consecutive in the original array.

 **Examples:** 

```
Input: arr[] = [1, 2, 3]
Output: 5
Explanation: All three element present in the array is consecutive, hence we have to consider just two element sum having maximum,which is 2+3 = 5
```

```
Input: arr[] = [3000, 2000, 1000, 3, 10]
Output: 5013
Explanation: 3000 + 2000 + 3 + 10 = 5013. 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-09T03:40:11.028Z  

```py
class Solution:
	def findMaxSum(self, arr):
		# code here
		
		n = len(arr)
		if n == 0:
		    return 0
		    
		if n == 1:
		    return arr[0]
		    
		if n == 2:
		    return arr[0] + arr[1]
		    
		dp3 = arr[0]
		dp2 = arr[0] + arr[1]
		dp1 = max(dp2, arr[2] + arr[0], arr[2] + arr[1])
		
		
		
		
		if n == 3:
		    return dp1
		    
		current = dp1
		
		for i in range(3, n):
		    current = max(dp1, arr[i] + dp2, arr[i] + arr[i - 1] + dp3)
		    
		    dp3 = dp2
		    dp2 = dp1
		    dp1 = current
		    
		return current
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents-2/1)