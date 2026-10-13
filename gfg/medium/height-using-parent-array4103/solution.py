class Solution:
    def findHeight(self, arr):
        # code here
        
        n = len(arr)
        memo = {}
        
        def get_height(node):
            if node == -1:
                return 0
                
            if node in memo:
                return memo[node]
                
            memo[node] = 1 + get_height(arr[node])
            return memo[node]
            
        max_h = 0
        for i in range(n):
            max_h = max(max_h, get_height(i))
            
            
        return max_h