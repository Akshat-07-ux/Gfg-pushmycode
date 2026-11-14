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