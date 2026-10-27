class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        
        dp = [-float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == -float('inf'):
                continue
            
            if i + 1 <= n:
                dp[i + 1] = max(dp[i + 1], dp[i])
                
            if i + 2 <= n:
                    
                togg_ab = (0 if s[i] == 'A' else 1) + (0 if s[i + 1] == 'B' else 1)
                dp[i + 2] = max(dp[i + 2], dp[i] + 2 - togg_ab)
                    
                togg_ba = (0 if s[i] == 'B' else 1) + (0 if s[i + 1] == 'A' else 1)
                dp[i + 2] = max(dp[i + 2], dp[i] + 2 - togg_ba)
                    
        return n + dp[n]