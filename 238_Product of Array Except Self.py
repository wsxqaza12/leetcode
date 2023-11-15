class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = [1] + [0]*(len(nums)-1)
        R = [0]*(len(nums)-1) + [1]

        for i in range(len(nums)-1):
            L[i+1] = L[i]*nums[i]
        for i in reversed(range(1, len(nums))):
            R[i-1] = R[i]*nums[i]
        for i in range(len(R)):
            R[i] = R[i]*L[i]

        return R
