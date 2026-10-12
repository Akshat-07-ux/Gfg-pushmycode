from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            curr, steps = queue.popleft()

            i = 0
            while i < len(curr) and curr[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i]:
                    next_str = list(curr)
                    next_str[i], next_str[j] = next_str[j], next_str[i]

                    next_str = "".join(next_str)

                    if next_str == s2:
                        return steps + 1

                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append((next_str, steps + 1))

        return 0
