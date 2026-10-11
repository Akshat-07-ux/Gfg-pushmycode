class Solution:
    def kthAncestorQueries(self, arr, queries):
        # code here
        
        n = len(arr)
        LOG = 18
        
        up = [[-1] * LOG for _ in range(n)]
        
        for i in range(n):
            up[i][0] = arr[i]
            
        for j in range(1, LOG):
            for i in range(n):
                parent = up[i][j - 1]
                if parent != -1:
                    up[i][j] = up[parent][j - 1]
                    
        ans = []
        for u, k in queries:
            curr = u
            
            for j in range(LOG):
                if (k >> j) & 1:
                    curr = up[curr][j]
                    if curr == -1:
                        break
            ans.append(curr)
            
        return ans