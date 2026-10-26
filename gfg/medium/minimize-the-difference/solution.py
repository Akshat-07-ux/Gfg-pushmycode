class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        # code here
        
        n = len(arr)
        if k >= n:
            return 0
            
        if k == 0:
            return max(arr) - min(arr)
            
        pref_max = [0] * n
        pref_min = [0] * n
        
        cur_max = arr[0]
        cur_min = arr[0]
        for i in range(n):
            cur_max = max(cur_max, arr[i])
            cur_min = min(cur_min, arr[i])
            
            pref_max[i] = cur_max
            pref_min[i] = cur_min
            
        suff_max = [0] * n
        suff_min = [0] * n
        
        cur_max = arr[-1]
        cur_min = arr[-1]
        
        for i in range(n - 1, -1, -1):
            cur_max = max(cur_max, arr[i])
            cur_min = min(cur_min, arr[i])
            suff_max[i] = cur_max
            suff_min[i] = cur_min

            
        ans = float('inf')
        
        for i in range(n - k + 1):
            rem_max = -float('inf')
            rem_min = float('inf')
            
            if i > 0:
                rem_max = max(rem_max, pref_max[i - 1])
                rem_min = min(rem_min, pref_min[i - 1])
                
            if i + k < n:
                rem_max = max(rem_max, suff_max[i + k])
                rem_min = min(rem_min, suff_min[i + k])
                
            ans = min(ans, rem_max - rem_min)
            
        return ans
        