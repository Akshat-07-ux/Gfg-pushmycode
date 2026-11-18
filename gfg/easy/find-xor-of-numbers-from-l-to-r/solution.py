class Solution:
    def findXOR(self, l: int, r: int) -> int:
        # code here
        def bwXOR(n):
            return [n, 1, n + 1, 0][n % 4]
            
        return bwXOR(r) ^ bwXOR(l - 1)