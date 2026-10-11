class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        fleets = 0
        last_time = 0

        for p, s in cars:
            time = (target - p) / s
            if time > last_time:
                fleets += 1
                last_time = time

        return fleets