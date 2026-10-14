import bisect
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.s = []

    def seat(self) -> int:
        if not self.s:
            self.s = [0]
            return 0

        d, seat = self.s[0], 0
        for a, b in zip(self.s, self.s[1:]):
            if (dist := (b - a) // 2) > d:
                d, seat = dist, a + dist

        if self.n - 1 - self.s[-1] > d:
            seat = self.n - 1

        bisect.insort(self.s, seat)
        return seat

    def leave(self, p: int) -> None:
        self.s.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)