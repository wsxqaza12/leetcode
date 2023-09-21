class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        
        nums.sort()
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                count = 1
            else:
                count += 1

            if count > len(nums)/2:
                return nums[i]
        
            