class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        max_dist = 0
        last_person = -1
        n = len(seats)

        for i in range(n):
            if seats[i]  == 1:
                if last_person == -1:
                    max_dist = i

                else:
                    max_dist = max(max_dist, (i - last_person) // 2)
                last_person = i

        max_dist = max(max_dist, n - 1 - last_person)

        return max_dist