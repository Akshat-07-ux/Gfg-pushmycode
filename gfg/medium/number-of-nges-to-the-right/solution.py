class Solution:
    def countGreater(self, arr, indices):
        # Code here
        
        ans = []
        n = len(arr)
        
        for idx in indices:
            val = arr[idx]
            cnt = 0
            for j in range(idx + 1, n):
                if arr[j] > val:
                    cnt += 1
            ans.append(cnt)
            
            
        return ans
        