class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        n = len(arr)
        
        if totalTime >= n:
            return sum(arr)
            
        window_sum = sum(arr[:totalTime])
        max_packages = window_sum
        
        for i in range(totalTime, n):
            window_sum += arr[i] - arr[i - totalTime]
            if window_sum > max_packages:
                max_packages = window_sum
                
        return max_packages