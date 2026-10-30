from typing import List
class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        """ code here """
        n = len(arr)
        M = 1000000007
        
        
        mp = {}
        
        for num in arr:
            mp[num] = mp.get(num, 0) + 1
            
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % M
            
        res = 0
        cur = 1
        seen = 0
        
        for i in range(l):
            freq = mp.get(i, 0)
            if freq == 0:
                return 0
                
            seen += freq
            cur = (cur * (power[freq] - 1 + M)) % M
            
        
        for i in range(l, r + 1):
            freq = mp.get(i, 0)
            here = (cur * power[n - seen - freq]) % M
            res = (res + here) % M
            
            if freq == 0:
                break
            seen += freq
            cur = (cur * (power[freq] - 1 + M)) % M
            
        return res
