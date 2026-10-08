class Solution:
    def maxFrequency(self, arr, k):
        # code here
        arr.sort()
        left = 0
        total_sum = 0
        max_freq = 0
        
        for right in range(len(arr)):
            total_sum += arr[right]
            
            while (right - left + 1) * arr[right] - total_sum > k:
                total_sum -= arr[left]
                left += 1
                
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq