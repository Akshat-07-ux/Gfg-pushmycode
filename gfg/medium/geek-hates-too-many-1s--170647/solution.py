class Solution:

    def maxValue(self, n: int) -> int:
        """code here"""
        
        bits = [0] * 32
        for i in range(32):
            if (n & (1 << (31 - i))) != 0:
                bits[i] = 1
                
        ans = 0
        for i in range(30):
            if bits[i] == 1:
                ans += (1 << (31 - i))
                if bits[i + 1] == 1:
                    bits[i + 2] = 0
                    
        if bits[30] == 1:
            ans += 2
        if bits[31] == 1:
            ans += 1
            
        return ans
