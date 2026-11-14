# Minimum Items with Buy 2 Get 1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer  **n**  representing the amount of money available, you can purchase the following items:

- T-shirt: $ 1000
- Bag: $  2000
- Jacket: $ 3000
- Ball: $ 4000
- Shoes: $ 5000

Each item type has at least 100 pieces available. For every 2 items of the same type that you buy, you get 1 additional item of that same type for free. Your task is to spend exactly  **n**  dollars and determine the minimum total number of items you can take home, including the free items.

 **Note:**  The Buy 2 Get 1 Free offer applies separately to each item type.

 **Examples:** 

```
Input: n = 22000
Output: 6 
Explanation: For $ 22000 he will buy 1 ball for 4000, 1 jacket for 3000 & 3 shoes for 15000 and he will get 1 extra pair of shoes free. On total making it 6 items.

```

```
Input: n = 3500
Output: -1
Explanation: Impossible to use full amount of 3500.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T11:55:28.541Z  

```py
class Solution:
    def minimumItem(self, n: int) -> int:
        # code here
        
        if n % 1000 != 0:
            return -1
            
        n //= 1000
        ans = float('inf')
        
        for mask in range(32):
            total = 0
            cnt = 0
            
            for i in range(5):
                if mask & (1 << i):
                    total += i + 1
                    cnt += 1
                    
            if total > n:
                continue
            
            rem = n - total
            
            if rem % 2 == 0:
                cnt += 3 * ((rem + 9) // 10)
                ans = min(ans, cnt)
        
        return ans if ans != float('inf') else -1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/lets-go-shopping4621/1)