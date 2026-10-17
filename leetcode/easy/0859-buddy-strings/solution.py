class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True

                seen.add(ch)
            return False

        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)

        return len(diff_indices) == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]
        