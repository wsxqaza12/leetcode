class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        s = set()
        note = []

        for left in range(len(nums)):
            mid = left + 1
            right = len(nums)-1

            while mid < right:
                count = nums[left] + nums[mid] + nums[right]
                if count == 0:
                    s.add((nums[left], nums[mid], nums[right]))
                    mid += 1
                    right -= 1
                elif count < 0:
                    mid += 1
                else:
                    right -= 1

        note = list(s)
        return note
