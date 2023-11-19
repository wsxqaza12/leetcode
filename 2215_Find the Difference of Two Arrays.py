class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0 = list(set(nums1) - set(nums2))
        ans1 = list(set(nums2) - set(nums1))

        return [ans0, ans1]
