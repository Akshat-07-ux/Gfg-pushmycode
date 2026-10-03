class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        i = 1

        while i < n - 1:
            is_peak = arr[i - 1] < arr[i] > arr[i + 1]
            if not is_peak:
                i += 1
                continue

            left = i - 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            ans = max(ans, right - left + 1)
            i = right + 1

        return ans