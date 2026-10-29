class Solution:
    def solve(self, n, m, h, a, b):
        vals = []
        cur = [0] * m
        prefix = [[] for _ in range(n)]

        for i in range(n):
            x = b[i] - 1
            cur[x] += a[i]
            prefix[i] = cur[x]
            vals.append(cur[x])

        vals = sorted(set(vals))
        size = len(vals)
        pos = {v: i for i, v in enumerate(vals)}

        count = [0] * (4 * size)
        sums = [0] * (4 * size)

        def update(node, left, right, idx, dc, ds):
            count[node] += dc
            sums[node] += ds

            if left == right:
                return

            mid = (left + right) // 2
            if idx <= mid:
                update(node * 2, left, mid, idx, dc, ds)
            else:
                update(node * 2 + 1, mid + 1, right, idx, dc, ds)

        def required(node, left, right, need):
            if left == right:
                return need // vals[left] + 1

            mid = (left + right) // 2
            rnode = node * 2 + 1

            if sums[rnode] > need:
                return required(rnode, mid + 1, right, need)

            return count[rnode] + required(
                node * 2, left, mid, need - sums[rnode]
            )

        total = [0] * m
        ans = [0] * (m + 1)
        damage = 0

        for i in range(n):
            gang = b[i] - 1
            old = total[gang]
            new = old + a[i]
            total[gang] = new
            damage += a[i]

            if old:
                update(1, 0, size - 1, pos[old], -1, -old)

            update(1, 0, size - 1, pos[new], 1, new)

            if damage < h:
                guards = 0
            else:
                guards = required(1, 0, size - 1, damage - h)

            ans[guards] = i + 1

        for k in range(1, m + 1):
            ans[k] = max(ans[k], ans[k - 1])

        return ans