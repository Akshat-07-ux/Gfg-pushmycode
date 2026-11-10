class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        # code here
        seen = {}
        for a in arr:
            seen[a] = seen.get(a, 0) + 1
            if seen[a] == k:
                return a
                
        return -1