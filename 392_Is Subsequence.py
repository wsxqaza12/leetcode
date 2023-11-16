class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tp = 0

        if len(s) == 0:
            return True
        elif len(t) == 0 and len(s) == 0:
            return True
        elif len(t) == 0 and len(s) != 0:
            return False

        for letter in s:
            if tp >= len(t):
                return False
            while t[tp] != letter:
                tp += 1
                if tp >= len(t):
                    return False
            tp += 1

        return True
