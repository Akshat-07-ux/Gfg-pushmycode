import heapq
class Solution:
    def findDelayTime(self, adj: list[list[list[int]]], src: int) -> int:
        # code here
        
        n = len(adj)
        dist = [float('inf')] * n
        dist[src] = 0
        
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
        max_delay = 0
        for d in dist:
            if d == float('inf'):
                return - 1
                
            if d > max_delay:
                max_delay = d
                
        return max_delay
        