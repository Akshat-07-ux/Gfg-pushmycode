from collections import deque
class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        # code here
        
        visit = set([u])
        q = deque([u])
        
        while q:
            cur = q.popleft()
            if cur == v:
                return True
                
            for nxt in adj[cur]:
                if nxt not in visit:
                    visit.add(nxt)
                    q.append(nxt)
                    
        return False
        
        
