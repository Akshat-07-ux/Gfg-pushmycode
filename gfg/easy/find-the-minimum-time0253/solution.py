class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        
        
        if s1 > s2:
            s1, s2 = s2, s1
            
        low, high = 0, n
        ans = s2 * n
        
        while low <= high:
            mid = (low + high) // 2
            t1 = mid * s1
            t2 = (n - mid) *s2
            
            ans = min(ans, max(t1, t2))
            
            if t1 < t2:
                low = mid + 1
                
            else:
                high = mid - 1
        return ans