class Solution:
    def isEqual(self, arr: list[int], queries: list[list[int]]) -> bool:
        # code here
        
        parent = list(range(len(arr)))
        comp_sum = list(arr)
        
        
        def find(i):
            path = []
            
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
                
            return i
            
        for u, v in queries:
            root_u = find(u - 1)
            root_v = find(v - 1)
            
            if root_u != root_v:
                parent[root_v] = root_u
                comp_sum[root_u] += comp_sum[root_v]
                
        sums = [comp_sum[i] for i in range(len(arr)) if parent[i] == i]
        
        total = sum(sums)
        
        if total % 2 != 0:
            return False
            
        target = total // 2
        dp = 1
        for s in sums:
            dp |= (dp << s)
            
        return bool((dp >> target) & 1)