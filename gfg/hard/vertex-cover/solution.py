class Solution:
    def vertexCover(self, edges):
        n = max(max(u, v) for u, v in edges)

        edge_masks = []
        for u, v in edges:
            edge_masks.append((1 << (u - 1)) | (1 << (v - 1)))

        ans = n

        for mask in range(1 << n):
            count = bin(mask).count('1')

            if count >= ans:
                continue

            valid = True

            for edge in edge_masks:
                if not (mask & edge):
                    valid = False
                    break

            if valid:
                ans = count

        return ans