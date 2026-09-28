class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = list('L' + dominoes + 'R')
        win, i = [], 0

        for j in range(1, len(l)):
            if l[j] == '.':
                continue

            mid = j - i - 1
            if i > 0:
                win.append(l[i])
            if l[i] == l[j]:
                win.append(l[i] * mid)

            elif l[i] == 'L' and l[j] == 'R':
                win.append('.' * mid)

            else:
                win.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))

            i = j

        return ''.join(win)