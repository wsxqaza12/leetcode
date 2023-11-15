class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = right = float('inf')

        for i in range(len(nums)):
            if nums[i] <= left:
                left = nums[i]
            elif nums[i] <= right:
                right = nums[i]
            else:
                return True
        return False
