class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = list(s)
        position = 0

        if len(s) < k:
            ans.reverse()
            return "".join(ans)

        while position < len(s)-1:
            left = position
            if position+k-1 > len(s):
                right = len(s)-1
            else:
                right = position+k-1
            while left < right and right < len(s):
                temp = ans[left]
                ans[left] = ans[right]
                ans[right] = temp
                left += 1
                right -= 1
            position += k*2

        return "".join(ans)
