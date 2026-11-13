class Solution:
    def minOps(self, arr):
        # code here
        
        mini = min(arr)
        return sum(arr) - len(arr) * mini
