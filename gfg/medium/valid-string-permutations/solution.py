class Solution:

    def countStrings(self, s):
        """code here"""
        
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
            
        total_swaps = 0
        n = len(s)
        
        for char in s:
            idx = ord(char) - 97
            total_swaps += n - counts[idx]
            counts[idx] -= 1
            n -= 1
            
        return total_swaps + 1


