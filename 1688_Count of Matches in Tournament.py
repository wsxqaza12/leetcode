class Solution:
    def numberOfMatches(self, n: int) -> int:
        dp = [n]
        ans = 0

        while dp[-1] != 1:
            ans += dp[-1]//2
            if dp[-1] % 2 == 0:
                dp.append(dp[-1]//2)
            else:
                dp.append(dp[-1]//2+1)

        return ans
