class Solution:
    def getCount (self, s, k):
        # code here
        freq = {}
        n = len(s)
        
        i = 0
        
        while i < n:
            ch = s[i]
            while i < n and s[i] == ch:
                i += 1
            freq[ch] = freq.get(ch, 0) + 1
            
        return sum(1 for ch in freq if freq[ch] == k)