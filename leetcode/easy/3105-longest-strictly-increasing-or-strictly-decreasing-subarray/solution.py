class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        if not nums:
            return 0


        max_l = 1
        inc_l = 1
        dec_l = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_l += 1
                dec_l = 1

            elif nums[i] < nums[i - 1]:
                dec_l += 1
                inc_l = 1

            else:
                inc_l = 1
                dec_l = 1

            max_l = max(max_l, inc_l, dec_l)

        return max_l
        