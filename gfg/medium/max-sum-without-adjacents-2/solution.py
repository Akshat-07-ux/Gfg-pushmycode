class Solution:
	def findMaxSum(self, arr):
		# code here
		
		n = len(arr)
		if n == 0:
		    return 0
		    
		if n == 1:
		    return arr[0]
		    
		if n == 2:
		    return arr[0] + arr[1]
		    
		dp3 = arr[0]
		dp2 = arr[0] + arr[1]
		dp1 = max(dp2, arr[2] + arr[0], arr[2] + arr[1])
		
		
		
		
		if n == 3:
		    return dp1
		    
		current = dp1
		
		for i in range(3, n):
		    current = max(dp1, arr[i] + dp2, arr[i] + arr[i - 1] + dp3)
		    
		    dp3 = dp2
		    dp2 = dp1
		    dp1 = current
		    
		return current