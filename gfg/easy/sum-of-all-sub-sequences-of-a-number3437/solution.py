class Solution:

    def subsequenceSum(self, s):
        """code here"""
        
        MOD = 10**9 + 7
        
        digit_sum = sum(int(char) for char in s)
        return (digit_sum * pow(2, len(s) - 1, MOD)) % MOD
