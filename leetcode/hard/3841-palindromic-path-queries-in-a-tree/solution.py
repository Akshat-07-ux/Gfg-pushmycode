class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj, tin, tout, timer = [[] for _ in range(n)], [0]*n, [0]*n, 0
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        
        LOG = 16
        up, depth = [[0]*n for _ in range(LOG)], [0]*n
        
        def dfs(u, p, d):
            nonlocal timer
            tin[u], depth[u], up[0][u], timer = timer, d, p, timer + 1
            for i in range(1, LOG): up[i][u] = up[i-1][up[i-1][u]]
            for v in adj[u]:
                if v != p: dfs(v, u, d+1)
            tout[u] = timer
        dfs(0, 0, 0)
        
        def lca(u, v):
            if depth[u] < depth[v]: u, v = v, u
            for i in range(LOG-1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]: u = up[i][u]
            if u == v: return u
            for i in range(LOG-1, -1, -1):
                if up[i][u] != up[i][v]: u, v = up[i][u], up[i][v]
            return up[0][u]

        bit = [0] * (n + 2)
        def add(i, x):
            while i <= n: bit[i] ^= x; i += i & -i
        def query(i):
            r = 0
            while i > 0: r ^= bit[i]; i -= i & -i
            return r

        mask = [1 << (ord(c) - ord('a')) for c in s]
        for i, m in enumerate(mask):
            add(tin[i] + 1, m)
            add(tout[i] + 1, m)
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0][0] == 'u':
                u, c = int(parts[1]), 1 << (ord(parts[2]) - ord('a'))
                if mask[u] != c:
                    add(tin[u] + 1, mask[u] ^ c)
                    add(tout[u] + 1, mask[u] ^ c)
                    mask[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                p_mask = query(tin[u] + 1) ^ query(tin[v] + 1) ^ mask[w]
                ans.append(p_mask & (p_mask - 1) == 0)
        return ans