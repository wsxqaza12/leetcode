class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2 == str2+str1:
            from fractions import gcd
            ans = str1[:gcd(len(str1), len(str2))]
            return ans
        else:
            return ""
