class Solution:
    def karyTree(self, n, m):
        # code here
        MOD = 10**9 + 7
        return pow(n, m, MOD)