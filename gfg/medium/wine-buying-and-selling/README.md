# Wine Buying and Selling

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array arr[] representing houses built along a straight line, each value arr[i] represents a certain number of wine bottles that a wants to buy or sell.

- If arr[i] < 0, then the i-th house wants to sell |arr[i]| bottles of wine.
- If arr[i] > 0, then the i-th house wants to buy arr[i] bottles of wine.

Find the  **minimum** total work required so that all houses can fulfill their wine buy/sell requirements.

- Transporting one bottle of wine from one house to an adjacent house costs 1 unit of work.
- It is guaranteed that the sum of all elements of the array is 0.

 **Examples:** 

```
Input: arr[] = [5, -4, 1, -3, 1]
Output: 9
Explanation: 
House 1 sells 4 bottles to house 0, so work done is 4 × 1 = 4.
Updated array becomes: [1, 0, 1, -3, 1]
Now, house 3 sells:
1 bottle to house 0 → work = 3
1 bottle to house 2 → work = 1
1 bottle to house 4 → work = 1
Total additional work = 3 + 1 + 1 = 5
Hence, total minimum work = 4 + 5 = 9.
So answer for this test case is 9.
```

```
Input: arr[] = [-1000, -1000, -1000, 1000, 1000, 1000]
Output: 9000
Explanation:  
House 0 sells 1000 bottles to house 3 → work = 1000 × 3 = 3000
House 1 sells 1000 bottles to house 4 → work = 1000 × 3 = 3000
House 2 sells 1000 bottles to house 5 → work = 1000 × 3 = 3000
Total minimum work = 3000 + 3000 + 3000 = 9000.
So answer for this test case is 9000.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-08T04:25:34.463Z  

```py
class Solution:
    def wineSelling(self, arr):
        # code here
        tot_wor = 0
        cur_bal = 0
        
        for val in arr:
            cur_bal += val
            tot_wor += abs(cur_bal)
            
        return tot_wor
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/wine-buying-and-selling/1)