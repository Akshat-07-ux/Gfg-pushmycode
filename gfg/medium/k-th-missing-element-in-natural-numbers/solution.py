import bisect
class Solution:
    def findKthSmall(self, arr, k):
        # code here
        
        arr.sort()
        
        low = k
        high = k + len(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            count = bisect.bisect_right(arr, mid)
            
            if mid - count >= k:
                ans = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return ans