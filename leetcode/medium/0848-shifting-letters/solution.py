class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        s = list(s)

        cur = 0

        for i in range(len(s) - 1, -1, -1):
            cur = (cur + shifts[i]) % 26
            s[i] = chr((ord(s[i]) - 97 + cur) % 26 + 97)

        return "".join(s)