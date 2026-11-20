class Solution:
    def minFlips(self, s):
        # Code here
        
        diff = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                diff += 1
                
        return min(diff, len(s) - diff)
        
