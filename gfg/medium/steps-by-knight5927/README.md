# Min Steps by Knight

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a square chessboard of size  **n × n**, the initial position  **knightPos**  and target position  **targetPos**  of a Knight are given. Find the minimum number of moves required for the Knight to reach targetPos.

A Knight moves in an L-shape, covering 2 cells in one direction and 1 cell perpendicular to it. From (x, y), it can move to: (x ± 2, y ± 1) and (x ± 1, y ± 2)

This gives at most 8 possible moves:

 **Note:**  The positions are given using 1-based indexing.

 **Examples:** 

```
Input: n = 3, knightPos[] = [3, 3], targetPos[]= [1, 2]
Output: 1
Explanation: Knight takes 1 step to reach from (3, 3) to (1,2).
```

```
Input: n = 6, knightPos[] = [1, 3], targetPos[] = [5, 1]
Output: 2
Explanation: In above diagram Knight takes 2 step to reach from (1, 3) to (5, 0): (1, 3) -> (3, 2) -> (5, 1)  
 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T07:10:22.486Z  

```py
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
		
		
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/steps-by-knight5927/1)