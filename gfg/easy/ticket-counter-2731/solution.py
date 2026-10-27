from collections import deque
class Solution:
    def distributeTicket(self, n: int, k: int) -> int:
        # Code Here
        
        dq = deque(range(1, n + 1))
        last_removed = -1
        
        while dq:
            
            for _ in range(min(k, len(dq))):
                last_removed = dq.popleft()
                
            if not dq:
                break
            
            for _ in range(min(k, len(dq))):
                last_removed = dq.pop()
                
        return last_removed