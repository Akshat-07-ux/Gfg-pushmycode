class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i + 1] for i in range(len(s) -1)):
            return 0

        if len(s) == 2:
            return -1

        mn, mx = min(s), max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        for i in range(1, len(s) -1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3