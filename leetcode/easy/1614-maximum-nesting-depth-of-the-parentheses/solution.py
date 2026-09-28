class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0

        for char in s:
            if char == "(":
                cur_depth += 1
                if cur_depth > max_depth:
                    max_depth = cur_depth

            elif char == ")":
                cur_depth -= 1

        return max_depth