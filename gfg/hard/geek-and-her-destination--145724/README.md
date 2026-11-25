# Geek's Destination with Special Jump

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Geek starts at position  **0**  on the positive X-axis and needs to reach or pass position  **d**  on the positive X-axis.

Geek normally follows a repeating movement pattern:

- Move forward by a units, taking a seconds.
- Move backward by b units, taking b seconds.

Geek also has a special jump that moves him exactly  **j**  units forward in 1 second. He can use it at any time, even in the middle of a forward or backward movement, and the journey ends immediately after the jump.

Given five integers  **a**,  **b**,  **d**,  **l**, and  **r**. For every integer j in the range [l, r], find the minimum time required for Geek to reach or pass position d. He may either use the special jump or reach the destination using normal movement alone, whichever takes less time.

Return the sum of the minimum times for all jump lengths from l to r. Since, the answer can be large, return modulo 109 + 7. 

 **Note:** Each jump length is considered independently.

 **Examples:** 

```
Input: a = 2, b = 1, d = 5, l = 3, r = 4
Output: 5
Explanation: 
For j = 3, Geek moves 2 units forward, then takes a jump of 3 units to reach the destination. The minimum time required is 3 seconds.
For j = 4, Geek moves 1 unit forward, then takes a jump of 4 units to reach the destination. The minimum time required is 2 seconds.
Total sum for the range [l, r] = 3 + 2 = 5.
```

```
Input: a = 4, b = 2, d = 8, l = 2, r = 4
Output: 26
Explanation:
For j = 2, Geek moves 4 units forward, then 2 units backward. She then moves 4 units forward again and takes a jump of 2 units to reach the destination. The minimum time required is 11 seconds.
For j = 3, Geek moves 4 units forward, then 2 units backward. She then moves 3 units forward and takes a jump of 3 units to reach the destination. The minimum time required is 10 seconds.
For j = 4, Geek moves 4 units forward, then takes a jump of 4 units to reach the destination. The minimum time required is 5 seconds.
Total sum for the range [l, r] = 11 + 10 + 5 = 26.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T06:19:02.987Z  

```py
class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        # code here
        
        MOD = 10**9 + 7
        net = a - b
        
        def normal_time(x):
            if x <= 0:
                return 0
                
                
            k = max(0, (x - a + net -1) // net)
            return x + 2 * b * k
            
        limit = normal_time(d)
        
        left = d - r
        right = d - l
        
        lo, hi = left, right + 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if normal_time(mid) + 1>= limit:
                hi = mid
            else:
                lo = mid + 1
                
        cut = lo
        
        def sum_time(L, R):
            if L > R:
                return 0
                
            count = R - L + 1
            total = ( L + R) * count // 2
            
            sum_k = 0
            
            start = max(L, a + 1)
            
            for rem in range(net):
                first = start + (rem - start) % net
                
                if first > R:
                    continue
                
                n = ( R - first) // net + 1
                k = max(0, (first - a + net -1) // net)
                
                sum_k += n * k + n * (n - 1) // 2
                
            return total + 2 * b * sum_k
            
        fast_sum = sum_time(left, cut - 1)
        fast_count = max(0, cut - left)
        
        slow_count = max(0, right - max(left, cut) + 1)
        
        ans = fast_sum + fast_count + slow_count * limit
        
        return ans % MOD
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geek-and-her-destination--145724/1)