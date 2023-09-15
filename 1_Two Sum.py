class Solution:
    def twoSum(
            self,
            nums,
            target):

        symmetry = [target - x for x in nums]
        for i in range(len(nums)):
            find = symmetry[i]

            if symmetry[i] == nums[i]:
                duplicate_num = [i for i, v in enumerate(nums) if v == find]
                if len(duplicate_num) > 1:
                    return(duplicate_num)
                continue
            if find in nums:
                return(i, nums.index(find))
