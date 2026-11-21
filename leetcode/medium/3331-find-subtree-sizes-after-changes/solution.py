import sys

sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        last = [-1] * 26
        tree = [[] for _ in range(n)]


        def reparent(u: int):
            c = ord(s[u]) - 97
            prev = last[c]

            if prev != -1:
                tree[prev].append(u)

            elif parent[u] != -1:
                tree[parent[u]].append(u)

            last[c] = u
            for v in adj[u]:
                reparent(v)
            last[c] = prev

        reparent(0)

        ans = [1] * n

        def count(u: int) -> int:
            for v in tree[u]:
                ans[u] += count(v)
            return ans[u]

        count(0)
        return ans

