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