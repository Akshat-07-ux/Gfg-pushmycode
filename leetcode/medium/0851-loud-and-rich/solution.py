class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        adj = [[] for _ in range(n)]

        for u, v in richer:
            adj[v].append(u)

        ans = [-1] * n

        def dfs(node):
            if ans[node] != -1:
                return ans[node]

            best = node
            for parent in adj[node]:
                cand = dfs(parent)
                if quiet[cand] < quiet[best]:
                    best = cand

            ans[node] = best
            return best

        for i in range(n):
            dfs(i)

        return ans