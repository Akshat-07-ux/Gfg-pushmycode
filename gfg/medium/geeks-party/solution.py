class Solution:
    def maximumTime(self, amt, k):
        # code here
        
        total_gas = sum(amt)
        max_possible = total_gas // k
        
        low, high = 0, max_possible
        ans = 0
        
        
        while low <= high:
            mid = (low + high) // 2
            
            effective_gas = sum(min(x, mid) for x in amt)
            
            if effective_gas >= k * mid:
                ans = mid
                low = mid + 1
                
            else:
                high = mid - 1
                
        return ans