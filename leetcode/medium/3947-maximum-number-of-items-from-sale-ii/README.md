# Maximum Number of Items From Sale II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a 2D integer array `items`, where `items[i] = [factori, pricei]` represents the `ith` item. You are also given an integer `budget`.

There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most `budget`.

After buying items, you may receive free copies according to the following rules:

- Each purchased copy of item i can give you at most one free copy of another item j.
- The free item must satisfy i != j and factori divides factorj.
- For each ordered pair (i, j), you can receive a free copy of item j from purchases of item i at most once, regardless of how many copies of item i you buy.
- The same item j can be received multiple times for free if it is received from purchases of different item types.

Return the  **maximum total number of item copies**  you can obtain, including both purchased copies and free copies, while spending at most `budget` on purchased items.

 

Original
Python3
 **Example 1:** 

 **Input:**  items = [[1,6],[2,4],[3,5]], budget = 19

 **Output:**  5

 **Explanation:** 

- You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of 2 * 6 + 4 = 16, which is not greater than budget = 19.
- One purchased copy of item 0 gives 1 free copy of item 1, because factor0 = 1 divides factor1 = 2.
- The other purchased copy of item 0 gives 1 free copy of item 2, because factor0 = 1 divides factor2 = 3.
- You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.

 **Example 2:** 

 **Input:**  items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35

 **Output:**  7

 **Explanation:** 

- You can buy 2 copies of item 0, 1 copy of item 1, and 1 copy of item 2 for a total cost of 2 * 8 + 10 + 6 = 32, which is not greater than budget = 35.
- One purchased copy of item 0 gives 1 free copy of item 2, because factor0 = 2 divides factor2 = 6.
- The other purchased copy of item 0 gives 1 free copy of item 3, because factor0 = 2 divides factor3 = 4.
- The purchased copy of item 1 gives 1 free copy of item 2, because factor1 = 1 divides factor2 = 6.
- Buying item 2 gives no free copy, because factor2 = 6 does not divide the factor of any other item.
- You leave with 4 purchased copies and 3 free copies, for a total of 7 item copies.

 

 **Constraints:** 

- 1 <= items.length <= 105
- items[i] = [factori, pricei]
- 1 <= factori <= items.length
- 1 <= pricei <= 109
- 1 <= budget <= 109

## Solution

**Language:** Python  
**Runtime:** 1165 ms (beats 5.41%)  
**Memory:** 69.9 MB (beats 5.41%)  
**Submitted:** 2026-11-28T06:28:48.076Z  

```py
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        mx = max(f for f, _ in items)
        freq = [0] * (mx + 1)
        for f, _ in items:
            freq[f] += 1

        mult = [0] * (mx + 1)
        for d in range(1, mx + 1):
            mult[d] = sum(freq[m] for m in range(d, mx + 1, d))


        opt = []
        for f, p in items:
            if p <= budget:
                free_cap = mult[f] - 1
                if free_cap > 0:
                    opt.append((p / 2, 2, p, min(free_cap, budget // p)))
                opt.append((p, 1, p, budget // p))

        opt.sort()
        total = 0
        for _, gain, p, cap in opt:
            take = min(cap, budget // p)
            total += take * gain
            budget -= take * p

        return total


        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/)