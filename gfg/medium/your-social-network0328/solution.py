class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        ans = []
        
        for i in range(2, n + 1):
            curr = i
            dist = 0
            reachable = []
            
            while curr >= 2:
                parent = arr[curr - 2]
                
                dist += 1
                reachable.append((parent, dist))
                curr = parent
                
            reachable.sort(key=lambda x: x[0])
            
            for j, k in reachable:
                ans.append([i, j, k])
                
        return ans