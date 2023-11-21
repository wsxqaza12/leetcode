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
                    return (duplicate_num)
                continue
            if find in nums:
                return (i, nums.index(find))

# Method 2


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find_num = target - nums[i]
            if (find_num in nums) and nums.index(find_num) != i:
                return [i, nums.index(find_num)]


# One-pass Hash Table
# Time complexity: O(N);
# Space Complexity: O(N);
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for i in range(len(nums)):
            if target - nums[i] in numIndex:
                return [numIndex[target - nums[i]], i]
            else:
                numIndex[nums[i]] = i

        return False
