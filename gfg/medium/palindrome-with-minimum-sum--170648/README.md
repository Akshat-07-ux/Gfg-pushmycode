# Palindrome with Replacement

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  consisting of lowercase English letters and the character '?', 

- Replace every '?' with a lowercase English letter such that the resulting string is a palindrome.
- If it is possible to form a palindrome, return the minimum possible sum of the absolute ASCII differences between every pair of adjacent characters in the resulting string.
- If it is not possible to form a palindrome, return -1.

 **Examples:** 

```
Input: s = a???c??c????
Output: 4
Explanation: One optimal palindrome is "abbbccccbbba". The sum of the absolute ASCII differences between adjacent characters is 1 + 0 + 0 + 1 + 0 + 0 + 0 + 1 + 0 + 0 + 1 = 4, which is the minimum possible. 
```

```
Input: s = a???c??c???c
Output: -1
Explanation: It is not possible to replace the '?' characters to make the string a palindrome because the first and last characters are different and cannot be changed.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T05:35:34.024Z  

```py
class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        
        n = len(s)
        arr = list(s)
        
        left, right = 0, n - 1
        while left < right:
            if arr[left] != '?' and arr[right] != '?':
                if arr[left] != arr[right]:
                    return -1
                    
            elif arr[left] != '?':
                arr[right] = arr[left]
            elif arr[right] != '?':
                arr[left] = arr[right]
            left += 1
            right -= 1
            
        prev_char = None
        for i in range(n // 2):
            if arr[i] != '?':
                prev_char = arr[i]
            elif prev_char is not None:
                arr[i] = prev_char
                arr[n - 1 - i] = prev_char
                
        prev_char = None
        for i in range(n // 2 - 1, -1, -1):
            if arr[i] != '?':
                prev_char = arr[i]
            elif prev_char is not None:
                arr[i] = prev_char
                arr[n - 1 - i] = prev_char
                
        for i in range(n):
            if arr[i] == '?':
                arr[i] = 'a'
                arr[n - 1 - i] = 'a'
                
        total_sum = 0
        for i in range(n - 1):
            total_sum += abs(ord(arr[i]) - ord(arr[i + 1]))
            
        return total_sum

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/palindrome-with-minimum-sum--170648/1)