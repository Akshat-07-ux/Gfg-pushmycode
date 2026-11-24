from collections import defaultdict
class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        # code here
        
        n = len(arr)
        b_s: dict[int, list[tuple[int, int]]] = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                b_s[arr[i] + arr[j]].append((i, j))
                
                
        for a in range(n):
            for b in range(a + 1, n):
                s = arr[a] + arr[b]
                for c, d in b_s[s]:
                    if (a, b) < (c, d) and c != a and c != b and d != a and d != b:
                        return [a, b, c, d]
                        
        return [-1, -1, -1, -1]
        