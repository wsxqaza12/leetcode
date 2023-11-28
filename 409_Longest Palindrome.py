class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0

        d = defaultdict(int)
        for l in s:
            d[l] += 1

        ans = 0
        one = True
        for v in d.values():
            if v % 2 == 1 and one:
                ans += v//2*2 + 1
                one = False
            else:
                ans += v//2*2

        return ans
