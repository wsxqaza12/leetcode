class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0
        hash_table = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hash_table:
                    hash_table[n1 + n2] += 1
                else:
                    hash_table[n1 + n2] = 1

        for n3 in nums3:
            for n4 in nums4:
                key = -(n3 + n4)
                if key in hash_table:
                    count += hash_table[key]

        return count