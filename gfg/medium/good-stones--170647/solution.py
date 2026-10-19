class Solution:
    def goodIndices(self, arr):
        # code here
        n = len(arr)
        vis = [0]*n
        
        for i in range(n):
            if vis[i] != 0:
                continue
            
            curr = i
            path = []
            
            while 0 <= curr < n and vis[curr] == 0:
                vis[curr] = 1
                path.append(curr)
                curr += arr[curr]
                
            if 0 <= curr < n and vis[curr] == 2:
                status = 2
                
            elif 0 <= curr < n and (vis[curr] == 3 or vis[curr] == 1):
                status = 3
                
            else:
                status = 2
                
            for node in path:
                vis[node] = status
                
        return vis.count(2)