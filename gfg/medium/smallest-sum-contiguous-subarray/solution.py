class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        min_ending_here = arr[0]
        min_so_far = arr[0]
        
        for x in arr[1:]:
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
            
        return min_so_far