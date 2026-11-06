class Solution:
    def minimumTime(self, cur: int, pos: list[int], time: list[int]) -> int:
        # code here
        
        return min(abs(p - cur) * t for p, t in zip(pos, time))
