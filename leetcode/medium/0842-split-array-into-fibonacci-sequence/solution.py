class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:

        def dfs(i, path):
            if i == len(num) and len(path) >= 3:
                return path

            for j in range(i, len(num)):
                if num[i] == '0' and j > i: 
                    break

                v = int(num[i:j+1])

                if v >= 2**31:
                    break

                if len(path) >= 2 and v > path[-1] + path[-2]:
                    break

                if len(path) < 2 or v == path[-1] + path[-2]:
                    if res := dfs(j + 1, path + [v]): 
                        return res

            return []
        
        return dfs(0, [])
        