class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        total_sum = 0
        for k in divisors:
            valid = True
            for j in range(0, n, k):
                orig = nums[j : j + k]
                target = sorted_nums[j : j + k]

                if orig == target:
                    continue

                s_orig = '.'.join(map(str, orig))
                s_target = '.'.join(map(str, target))

                if s_target not in s_orig + '.' + s_orig:
                    valid = False
                    break

            if valid:
                total_sum += k

        return total_sum