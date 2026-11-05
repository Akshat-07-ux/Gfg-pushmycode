class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        ans = 0

        for num in arr1:
            found_close = False
            for other in arr2:
                if abs(num - other) <= d:
                    found_close = True

                    break

            if not found_close:
                ans += 1

        return ans