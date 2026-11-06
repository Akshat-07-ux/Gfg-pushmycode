class Solution:
    def countBT(self, h: int) -> int:
        # code here
        MOD = 1000000007
        
        if h <= 0:
            return 0
            
        if h == 1:
            return 1
            
        prev2 = 1
        prev1 = 1
        
        for _ in range(2, h + 1):
            current = (prev1 * prev1 + 2 * prev1 * prev2) % MOD
            prev2 = prev1
            prev1 = current
            
        return prev1