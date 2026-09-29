from collections import deque

class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
		#Code here
		
		if knightPos == targetPos:
		    return 0
		    
		moves = [
		    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
		    ]
		
		visit = [[False] * (n + 1) for _ in range(n + 1)]
		
		queue = deque([(knightPos[0], knightPos[1], 0)])
		
		visit[knightPos[0]][knightPos[1]] = True
		
		while queue:
		    x, y, chess = queue.popleft()
		    
		    for dx, dy in moves:
		        nx, ny = x + dx, y + dy
		        
		        if nx == targetPos[0] and ny == targetPos[1]:
		            return chess + 1
		            
		        if 1 <= nx <= n and 1 <= ny <= n and not visit[nx][ny]:
		            visit[nx][ny] = True
		            queue.append((nx, ny, chess + 1))
		               
		return -1
		
		