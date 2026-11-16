class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            parts = []

            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                total = sum(int(digit) for digit in chunk)

                parts.append(str(total))
            s = "".join(parts)

        return s
        