class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_days(date_str):
            m, d = map(int, date_str.split('-'))
            return sum(days_in_months[:m -1]) + d

        a_start = to_days(arriveAlice)
        a_end = to_days(leaveAlice)

        b_start = to_days(arriveBob)
        b_end = to_days(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        return max(0, end - start + 1)