class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        path = None
        i = 0
        while path is None and i < (len(nums)-1):
            if nums[i] < nums[i+1]:
                path = "increasing"
            elif nums[i] > nums[i+1]:
                path = "decreasing"
            i += 1

        for j in range(i, len(nums)-1):
            if path == "increasing" and nums[j] > nums[j+1]:
                return False
            elif path == "decreasing" and nums[j] < nums[j+1]:
                return False

        return True
