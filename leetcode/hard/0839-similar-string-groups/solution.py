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
        