class Solution:
    def beautySum(self, s: str) -> int:
        # code here
        ans = 0
        n = len(s)
        
        for i in range(n):
            counts = {}
            
            for j in range(i, n):
                counts[s[j]] = counts.get(s[j], 0) + 1
                
                max_freq = max(counts.values())
                min_freq = min(counts.values())
                
                ans += (max_freq - min_freq)
                
        return ans