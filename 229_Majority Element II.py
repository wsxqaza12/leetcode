class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        threshold = len(nums) / 3

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        ans = [k for k, v in dict.items() if v > threshold]
        return ans
