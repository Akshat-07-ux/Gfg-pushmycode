# Similar String Groups

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Two strings, `X` and `Y`, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string `X`.

For example, `"tars"` and `"rats"` are similar (swapping at positions `0` and `2`), and `"rats"` and `"arts"` are similar, but `"star"` is not similar to `"tars"`, `"rats"`, or `"arts"`.

Together, these form two connected groups by similarity: `{"tars", "rats", "arts"}` and `{"star"}`.  Notice that `"tars"` and `"arts"` are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list `strs` of strings where every string in `strs` is an anagram of every other string in `strs`. How many groups are there?

 

 **Example 1:** 

```
Input: strs = ["tars","rats","arts","star"]
Output: 2

```

 **Example 2:** 

```
Input: strs = ["omv","ovm"]
Output: 1

```

 

 **Constraints:** 

- 1 <= strs.length <= 300
- 1 <= strs[i].length <= 300
- strs[i] consists of lowercase letters only.
- All words in strs have the same length and are anagrams of each other.

## Solution

**Language:** Python  
**Runtime:** 121 ms (beats 56.26%)  
**Memory:** 19.4 MB (beats 87.03%)  
**Submitted:** 2026-09-28T15:59:43.648Z  

```py
class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        strs = list(set(strs))

        l = len(strs)
        par = list(range(l))


        def find(i):
            if par[i] == i:
                return i

            par[i] = find(par[i])

            return par[i]

        def sim(s1, s2):
            diff = 0

            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False

            return diff == 0 or diff == 2

        groups = l
        for i in range(l):
            for j in range(i + 1, l):
                root_i, root_j = find(i), find(j)

                if root_i != root_j and sim(strs[i], strs[j]):
                    par[root_i] = root_j

                    groups -= 1

        return groups
        
```

---

[View on LeetCode](https://leetcode.com/problems/similar-string-groups/)