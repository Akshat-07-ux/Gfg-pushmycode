class Solution:

    def minOperations(self, arr):
        """code here"""
        
        
        return len({val for val in arr if val > 0})
