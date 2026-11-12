class Solution:
    def maxChainLen(self, arr):
        # code here
        if not arr:
            return 0
            
        arr.sort(key=lambda x: x[1])
        
        chain_l = 1
        cur_end = arr[0][1]
        
        for i in range(1, len(arr)):
            if arr[i][0] > cur_end:
                cur_end = arr[i][1]
                chain_l += 1
                
        return chain_l
        
