class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        l = 0

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

            while d[s[i]] > 1:
                d[s[l]] -= 1
                l += 1

            ans = max(ans, i-l+1)

        return ans
