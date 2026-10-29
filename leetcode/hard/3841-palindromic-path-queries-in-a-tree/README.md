# Palindromic Path Queries in a Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an undirected tree with `n` nodes labeled 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [ui, vi]` indicates an undirected edge between nodes `ui` and `vi`.

You are also given a string `s` of length `n` consisting of lowercase English letters, where `s[i]` represents the character assigned to node `i`.

You are also given a string array `queries`, where each `queries[i]` is either:

- "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
- "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.

Return a boolean array `answer`, where `answer[j]` is `true` if the `jth` query of type `"query ui vi"​​​​​​​` can be rearranged into a  **palindrome**, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

 **Output:**  [true,false]

 **Explanation:** 

- "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
- "update 1 b": Update node 1 to 'b', now s = "abc".
- "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.

Thus, `answer = [true, false]`.

 **Example 2:** 

 **Input:**  n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

 **Output:**  [false,false,true]

 **Explanation:** 

- "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
- "update 0 b": Update node 0 to 'b', now s = "bbca".
- "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
- "update 3 a": Update node 3 to 'a', s = "bbca".
- "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.

Thus, `answer = [false, false, true]`.

 

 **Constraints:** 

- 1 <= n == s.length <= 5 * 104
- edges.length == n - 1
- edges[i] = [ui, vi]
- 0 <= ui, vi <= n - 1
- s consists of lowercase English letters.
- The input is generated such that edges represents a valid tree.
- 1 <= queries.length <= 5 * 104​​​​​​​queries[i] = "update ui c" or queries[i] = "query ui vi" 0 <= ui, vi <= n - 1 c is a lowercase English letter.

## Solution

**Language:** Python  
**Runtime:** 1684 ms (beats 34.69%)  
**Memory:** 117 MB (beats 20.41%)  
**Submitted:** 2026-10-29T07:21:52.285Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)