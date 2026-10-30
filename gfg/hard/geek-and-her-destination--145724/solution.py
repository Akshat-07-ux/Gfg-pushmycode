class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        def get_T(X):
            if X <= 0:
                return 0
            elif X <= a:
                return X
            else:
                m = a - b
                k = (X - a + m - 1) // m
                return 2 * k * b + X

        def jump_time(j):
            return get_T(d - j) + 1

        k_norm = (d - b - 1) // (a - b)
        T_norm = 2 * k_norm * b + d

        
        low, high = l, r
        j_star = r + 1
        while low <= high:
            mid = (low + high) // 2
            if jump_time(mid) < T_norm:
                j_star = mid
                high = mid - 1
            else:
                low = mid + 1

        total_sum = 0

        
        if j_star > l:
            count1 = j_star - l
            total_sum = (total_sum + count1 * T_norm) % MOD

        
        if j_star <= r:
            X_min = d - r
            X_max = d - j_star

            
            min_a = min(X_max, a)
            if X_min <= min_a:
                cntA = min_a - X_min + 1
                sumA = (X_min + min_a) * cntA // 2 + cntA
                total_sum = (total_sum + sumA) % MOD

            
            max_X_min = max(X_min, a + 1)
            if max_X_min <= X_max:
                X1 = max_X_min
                X2 = X_max
                cntB = X2 - X1 + 1
                sum_X_plus_1 = (X1 + X2 + 2) * cntB // 2

                m = a - b
                Z1 = X1 - a + m - 1
                Z2 = X2 - a + m - 1

                def F(N):
                    if N < 0:
                        return 0
                    q = N // m
                    r_rem = N % m
                    return m * q * (q - 1) // 2 + q * (r_rem + 1)

                sum_ceil = F(Z2) - F(Z1 - 1)
                sum_T_plus_1 = sum_X_plus_1 + 2 * b * sum_ceil
                total_sum = (total_sum + sum_T_plus_1) % MOD

        return total_sum % MOD