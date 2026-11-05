# Sum of Factorials of Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

For any positive integer  **x**, let  **A(x)**  be defined ad the sum of factorials of its digits. For example, A(154) = 1! + 5! + 4!= 145.

Given an integer  **n**, find the minimum number  **x**  such that  **A(x) = n**. Since the resulting integer x can be extremely large, return its digits as an array of integers, ordered from most significant to least significant, without any leading zeros.

 **Examples:** 

```
Input: n = 40321
Output: 18
Explanation: A(18) = 1!+ 8! = 40321. Note that A(80) and A(81) are also 40321, But 18 is the smallest number.

```

```
Input: n = 5040
Output: 7
Explanation: A(7) = 7! = 5040.

```

 **Constraints:** 
1 ≤ n ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-05T09:39:00.162Z  

```py
class Solution:
	def FactDigit(self, n):
		# code here
		digits = []
		factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
		
		for i in range(9, 0, -1):
		    while n >= factorials[i]:
		        n -= factorials[i]
		        digits.append(i)
		        
		digits.sort()
		return digits
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/fact-digit-sum4125/1)