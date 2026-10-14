# Roll Characters of String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  consisting of lowercase English letters and an integer array  **roll[],**  perform a sequence of roll operations on the string.

For each value roll[i], increment each of the first roll[i] characters of the string by 1 in the English alphabet. After 'z', the character wraps around to 'a'.

Return the final string after applying all roll operations.

 **Note:**  A roll operation affects the current state of the string, including all previous modifications.

 **Examples:** 

```
Input: s = "bca", roll[] = [1, 2, 3]
Output: eeb
Explanation: Initially, s = "bca" 
roll[0] = 1: Roll the first 1 character. "bca" -> "cca" 
roll[1] = 2: Roll the first 2 characters. "cca"-> "dda" 
roll[2] = 3: Roll the first 3 characters. "dda" -> "eeb" 
After applying all the roll operations, the final string is "eeb".

```

```
Input: s = "zcza", roll[] = [1, 1, 3, 4]
Output: debb
Explanation: Initially, s = "zcza". 
Roll first 1 character: "zcza" -> "acza" 
Roll first 1 character again: "acza" -> "bcza" 
Roll first 3 characters: "bcza" -> "cdaa" 
Roll first 4 characters: "cdaa" -> "debb" 
Therefore, the final string is "debb".
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T05:28:21.544Z  

```py
class Solution:
    def findRollOut(self, s, roll):
        # code here
        
        n = len(s)
        diff = [0]*(n + 1)
        
        for r in roll:
            diff[0] += 1
            diff[r] -= 1
            
        res = []
        curr_roll = 0
        
        for i in range(n):
            curr_roll += diff[i]
            base = ord(s[i]) - ord('a')
            shifted = chr(ord('a') + (base + curr_roll) % 26)
            
            res.append(shifted)
            
        return "".join(res)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/roll-the-characters-of-a-string2127/1)