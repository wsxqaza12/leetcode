class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        lsp = [0] * len(s)
        pre = 0

        for i in range(1, len(s)):
            while (pre > 0 and s[pre] != s[i]):
                pre = lsp[pre-1]
            if s[pre] == s[i]:
                pre += 1
                lsp[i] = pre

        if lsp[-1] != 0 and len(s) % (len(s) - lsp[-1]) == 0:
            return True
        else:
            return False
