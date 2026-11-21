class Solution:
    def smallestSubWithSum(self, arr, x):
        # code here 
        
        n = len(arr)
        total = 0
        ans = n  + 1
        left = 0
        
        for right in range(n):
            total += arr[right]
            
            while total > x:
                ans = min(ans, right - left + 1)
                total -= arr[left]
                left += 1
                
        
        return 0 if ans == n + 1 else ans