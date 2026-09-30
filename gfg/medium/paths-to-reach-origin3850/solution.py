import math
class Solution:
    def ways(self, x: int, y: int) -> int:
        # code here
        
        MOD = 10**9 + 7
        
        return math.comb(x + y, x) % MOD