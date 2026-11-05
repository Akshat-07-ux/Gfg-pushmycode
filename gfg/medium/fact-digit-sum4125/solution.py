class Solution:
	def FactDigit(self, n):
		# code here
		digits = []
		factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
		
		for i in range(9, 0, -1):
		    while n >= factorials[i]:
		        n -= factorials[i]
		        digits.append(i)
		        
		digits.sort()
		return digits