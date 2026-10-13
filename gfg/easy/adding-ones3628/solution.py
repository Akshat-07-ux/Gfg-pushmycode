class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here
        
        diff = [0] * (n + 1)
        for x in updates:
            diff[x - 1] += 1
            diff[n] -= 1
            
        ans = [0] * n
        run_sum = 0
        for i in range(n):
            run_sum += diff[i]
            ans[i] = run_sum
            
        return ans