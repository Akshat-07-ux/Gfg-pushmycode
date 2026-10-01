from collections import deque
class Solution:
    def minTime(self, duration: list[int], dependencies: list[list[int]]) -> int:
        # code here
        
        l = len(duration)
        grp = [[] for _ in range(l)]
        
        deg = [0] * l
        
        for u, v in dependencies:
            grp[u].append(v)
            deg[v] += 1
            
        queue = deque(i for i in range(l) if deg[i] == 0)
        dp = list(duration)
        
        
        processed = 0
        while queue:
            cur = queue.popleft()
            processed += 1
            
            for nxt in grp[cur]:
                dp[nxt] = max(dp[nxt], dp[cur] + duration[nxt])
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    queue.append(nxt)
                    
        return max(dp) if processed == l else -1
