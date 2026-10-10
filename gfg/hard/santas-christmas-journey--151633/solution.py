import sys

# Set higher recursion limit for deep trees
sys.setrecursionlimit(200_000)

class Solution:
    def countVisits(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length() + 1
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        # BFS to compute depths and immediate parents
        from collections import deque
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            curr = q.popleft()
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    depth[nxt] = depth[curr] + 1
                    up[nxt][0] = curr
                    q.append(nxt)

        # Precompute binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j - 1]][j - 1]

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # Apply tree difference array updates
        diff = [0] * (n + 1)
        for u, v in queries:
            lca = get_lca(u, v)
            diff[u] += 1
            diff[v] += 1
            diff[lca] -= 1
            p = up[lca][0]
            if p != 0:
                diff[p] -= 1

        # Calculate final counts via subtree sum DFS
        ans = [0] * (n + 1)
        def dfs(node, parent):
            total = diff[node]
            for nxt in adj[node]:
                if nxt != parent:
                    total += dfs(nxt, node)
            ans[node] = total
            return total

        dfs(1, 0)
        return ans[1:]