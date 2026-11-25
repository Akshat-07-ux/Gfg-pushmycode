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
