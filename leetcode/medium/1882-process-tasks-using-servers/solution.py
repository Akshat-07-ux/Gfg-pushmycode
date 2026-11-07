class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free, busy, ans, t = [(w, i) for i, w in enumerate(servers)], [], [], 0
        heapq.heapify(free)

        for j, task in enumerate(tasks):
            t = max(t, j)
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)

                heapq.heappush(free, (w, i))

            if not free:
                t = busy[0][0]
                while busy and busy[0][0] <= t:
                    _, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (t + task, w, i))
        
        return ans