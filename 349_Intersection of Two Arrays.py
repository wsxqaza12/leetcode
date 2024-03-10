class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return nums1_set.intersection(nums2_set) 