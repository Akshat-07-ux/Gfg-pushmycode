class Solution:
    def findRollOut(self, s, roll):
        # code here
        
        n = len(s)
        diff = [0]*(n + 1)
        
        for r in roll:
            diff[0] += 1
            diff[r] -= 1
            
        res = []
        curr_roll = 0
        
        for i in range(n):
            curr_roll += diff[i]
            base = ord(s[i]) - ord('a')
            shifted = chr(ord('a') + (base + curr_roll) % 26)
            
            res.append(shifted)
            
        return "".join(res)