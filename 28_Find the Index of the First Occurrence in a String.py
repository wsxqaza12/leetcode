class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lsp = [0] * len(needle)
        pre = 0

        for i in range(1, len(needle)):
            while (pre > 0 and needle[pre] != needle[i]):
                pre = lsp[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lsp[i] = pre

        n = 0
        for h in range(len(haystack)):
            while (n > 0 and needle[n] != haystack[h]):
                n = lsp[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1
