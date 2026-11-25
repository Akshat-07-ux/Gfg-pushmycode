# Next Move in Tic Tac Toe

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a 3 x 3 character matrix  **board[][]** representing the current state of a Tic-Tac-Toe game, where  **'x'**  and  **'o'**  denote the moves already played by the two players and  **'_'**  denotes an empty cell, find the most optimal move for player ' **x** ' to play next. Assume player ' **o** ' always plays first, and both players play optimally. If no empty cell is available on the board, return  **{-1, -1}**.

 **Note:**  In Tic-Tac-Toe, players take turns marking an empty cell. A player wins by placing three of their marks consecutively in the same row, column, or diagonal. If all cells are filled and neither player has achieved this, the game ends in a draw.

 **Examples:** 

```
Input: board[][] = [[o, _, _], [_, _, _], [_, _, _]] 
Output: [1, 1]
Explanation: Placing 'x' at [1, 1], as shown in the second image, is the most optimal response.
  
```

```
Input: board[][] = [[x, o, _], [_, o, _], [x, _, _]]
Output: [1, 0]
Explanation: Placing 'x' at [1, 0], as shown in the second image, completes the first column and wins the game immediately.
  
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T06:50:23.994Z  

```py
from functools import lru_cache

class Solution:
    def findBestMove(self, board):
        state = ''.join(''.join(row) for row in board)

        @lru_cache(None)
        def solve(s, turn):
            lines = [s[i:i+3] for i in (0, 3, 6)]
            lines += [[s[i+j*3] for j in range(3)] for i in range(3)]
            lines += [[s[i*4] for i in range(3)],
                      [s[2+i*2] for i in range(3)]]

            filled = s.count('x') + s.count('o')

            for line in lines:
                if line[0] != '_' and line.count(line[0]) == 3:
                    return 100-filled if line[0] == 'x' else -100+filled

            if '_' not in s:
                return 0

            scores = []
            for i in range(9):
                if s[i] == '_':
                    new = s[:i] + turn + s[i+1:]
                    scores.append(solve(new, 'o' if turn == 'x' else 'x'))

            return (max if turn == 'x' else min)(scores)

        best, move = float('-inf'), [-1, -1]

        for i in range(9):
            if state[i] == '_':
                new = state[:i] + 'x' + state[i+1:]
                score = solve(new, 'o')

                if score > best:
                    best = score
                    move = [i//3, i%3]

        return move

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/next-optimal-move-in-tic-tac-toe2842/1)