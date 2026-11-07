class Solution:
    def smallestNum(self, n: int) -> str:
        # code here
        
        digits= []
        original = n
        
        while n > 0:
            d = min(n, 9)
            digits.append(str(d))
            n -= d
            
        digits.reverse()
        return "".join(digits) + "0" * original