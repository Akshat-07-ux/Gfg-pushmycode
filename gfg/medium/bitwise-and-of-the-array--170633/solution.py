class Solution:
    def count(self, arr, x):
        # code here
        
        n = len(arr)
        ans = n
        pref = 0
        
        for bit in range(30, -1, -1):
            if (x >> bit) & 1:
                pref |= (1 << bit)
                continue
            
            need = pref | (1 << bit)
            keep = 0
            
            for value in arr:
                if (value & need) == need:
                    keep += 1
                    
            ans = min(ans, n - keep)
        return ans