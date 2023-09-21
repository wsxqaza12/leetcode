class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = []
        while n != 1:
            n = [int(i)**2 for i in str(n)]
            n = sum(n)
            if n in nums:
                return False
            else:
                nums.append(n)

        return True


        