# Find Subtree Sizes After Changes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a tree rooted at node 0 that consists of `n` nodes numbered from `0` to `n - 1`. The tree is represented by an array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node 0 is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

We make the following changes on the tree  **one**  time  **simultaneously**  for all nodes `x` from `1` to `n - 1`:

- Find the closest node y to node x such that y is an ancestor of x, and s[x] == s[y].
- If node y does not exist, do nothing.
- Otherwise, remove the edge between x and its current parent and make node y the new parent of x by adding an edge between them.

Return an array `answer` of size `n` where `answer[i]` is the  **size**  of the subtree rooted at node `i` in the  **final**  tree.

 

Original
Python3
 **Example 1:** 

 **Input:**  parent = [-1,0,0,1,1,1], s = "abaabc"

 **Output:**  [6,3,1,1,1,1]

 **Explanation:** 

The parent of node 3 will change from node 1 to node 0.

 **Example 2:** 

 **Input:**  parent = [-1,0,4,0,1], s = "abbba"

 **Output:**  [5,2,1,1,1]

 **Explanation:** 

The following changes will happen at the same time:

- The parent of node 4 will change from node 1 to node 0.
- The parent of node 2 will change from node 4 to node 1.

 

 **Constraints:** 

- n == parent.length == s.length
- 1 <= n <= 105
- 0 <= parent[i] <= n - 1 for all i >= 1.
- parent[0] == -1
- parent represents a valid tree.
- s consists only of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 1018 ms (beats 52.17%)  
**Memory:** 106.1 MB (beats 64.13%)  
**Submitted:** 2026-11-21T10:50:56.363Z  

```py
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


```

---

[View on LeetCode](https://leetcode.com/problems/find-subtree-sizes-after-changes/)