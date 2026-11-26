class Solution:
    def gfSeries(self, n):
        # code here
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-2] ** 2 - seq[-1])
            
        return seq