# Geek and Her Destination

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given five integers  **a**,  **b**,  **d**,  **l**, and  **r**, where:

- a is the distance Geek moves forward in one forward movement.
- b is the distance Geek moves backward in one backward movement.
- d is the destination position on the positive X-axis.
- [l, r] represents the range of possible jump lengths.

Geek starts at position x = 0 and normally follows this movement pattern:

- Move a units forward, taking a seconds.
- Move b units backward, taking b seconds.
- Repeat this pattern as needed.

Geek also has a special jump:

- The jump moves Geek exactly j units forward.
- The jump takes 1 second.
- The jump can be used at any moment during the movement, including in the middle of a forward or backward movement.
- Once the jump is used, the movement ends.

For every integer jump length j from l to r, determine the minimum time required for Geek to reach or pass position d. Geek may choose not to use the jump if reaching d through normal movement is faster.

Return the sum of the minimum times for all jump lengths from l to r.

In other words, if f(j) represents the minimum time required when the jump length is j, return:

 **f(l) + f(l + 1) +... + f(r - 1) + f(r)** 

The answer might be too large so return it modulo 10^9 + 7

 **Note:**  Each jump length is considered independently.

 **Examples:** 

```
Input: a = 2, b = 1, d = 5, l = 3, r = 4
Output: 5
Explanation: 
For j = 3, Geek moves 2 units forward, then takes a jump of 3 units to reach the destination. The minimum time required is 3 seconds.
For j = 4, Geek moves 1 unit forward, then takes a jump of 4 units to reach the destination. The minimum time required is 2 seconds.
Total sum for the range [l, r] = 3 + 2 = 5
```

```
Input: a = 4, b = 2, d = 8, l = 2, r = 4
Output: 26
Explanation:
For j = 2, Geek moves 4 units forward, then 2 units backward. She then moves 4 units forward again and takes a jump of 2 units to reach the destination. The minimum time required is 11 seconds.
For j = 3, Geek moves 4 units forward, then 2 units backward. She then moves 3 units forward and takes a jump of 3 units to reach the destination. The minimum time required is 10 seconds.
For j = 4, Geek moves 4 units forward, then takes a jump of 4 units to reach the destination. The minimum time required is 5 seconds.
Total sum for the range [l, r] = 11 + 10 + 5 = 26 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T11:13:23.353Z  

```py
class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        def get_T(X):
            if X <= 0:
                return 0
            elif X <= a:
                return X
            else:
                m = a - b
                k = (X - a + m - 1) // m
                return 2 * k * b + X

        def jump_time(j):
            return get_T(d - j) + 1

        k_norm = (d - b - 1) // (a - b)
        T_norm = 2 * k_norm * b + d

        
        low, high = l, r
        j_star = r + 1
        while low <= high:
            mid = (low + high) // 2
            if jump_time(mid) < T_norm:
                j_star = mid
                high = mid - 1
            else:
                low = mid + 1

        total_sum = 0

        
        if j_star > l:
            count1 = j_star - l
            total_sum = (total_sum + count1 * T_norm) % MOD

        
        if j_star <= r:
            X_min = d - r
            X_max = d - j_star

            
            min_a = min(X_max, a)
            if X_min <= min_a:
                cntA = min_a - X_min + 1
                sumA = (X_min + min_a) * cntA // 2 + cntA
                total_sum = (total_sum + sumA) % MOD

            
            max_X_min = max(X_min, a + 1)
            if max_X_min <= X_max:
                X1 = max_X_min
                X2 = X_max
                cntB = X2 - X1 + 1
                sum_X_plus_1 = (X1 + X2 + 2) * cntB // 2

                m = a - b
                Z1 = X1 - a + m - 1
                Z2 = X2 - a + m - 1

                def F(N):
                    if N < 0:
                        return 0
                    q = N // m
                    r_rem = N % m
                    return m * q * (q - 1) // 2 + q * (r_rem + 1)

                sum_ceil = F(Z2) - F(Z1 - 1)
                sum_T_plus_1 = sum_X_plus_1 + 2 * b * sum_ceil
                total_sum = (total_sum + sum_T_plus_1) % MOD

        return total_sum % MOD
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geek-and-her-destination--145724/1)