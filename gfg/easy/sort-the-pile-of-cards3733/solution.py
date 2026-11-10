class Solution:
    def minOps(self, arr):
        # code here
        n = len(arr)
        
        expected = n
        count = 0
        
        for i in range(n - 1, -1, -1):
            if arr[i] == expected:
                count += 1
                expected -= 1
                
        return n - count