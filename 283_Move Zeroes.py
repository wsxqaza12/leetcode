class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        curr = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[curr] = nums[i]
                curr += 1

        for _ in range(count):
            nums[curr] = 0
            curr += 1

        return nums
