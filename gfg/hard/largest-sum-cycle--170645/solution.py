class Solution:
    def largestSumCycle(self, edge):
        # code here
        
        n = len(edge)
        visited = [0] * n
        max_sum = -1
        
        for i in range(n):
            if visited[i] == 0:
                curr = i
                path = []
                path_index = {}
                
                while curr != -1 and visited[curr] == 0:
                    visited[curr] = 1
                    path_index[curr] = len(path)
                    path.append(curr)
                    curr = edge[curr]
                    
                    
                if curr != -1 and visited[curr] == 1:
                    start_idx = path_index[curr]
                    cycle_sum = sum(path[start_idx:])
                    if cycle_sum > max_sum:
                        max_sum = cycle_sum
                        
                for node in path:
                    visited[node] = 2
                    
        return max_sum