class Solution:
	def longestSubarrayDivK(self, arr, k):
		# code here
		first_idx = {0: -1}
		run_sum = 0
		best = 0
		
		
		for i, num in enumerate(arr):
		    run_sum += num
		    rem = run_sum % k
		    
		    if rem in first_idx:
		        best = max(best, i - first_idx[rem])
		    else:
		        first_idx[rem] = i
		        
		return best