class Solution:
    def canAliceWin(self, n: int) -> bool:

        take = 10
        alice = True

        while n >= take:
            n -= take
            take -= 1
            alice = not alice

        return not alice
        

