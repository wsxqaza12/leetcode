class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_num = 0
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            max_num = max(max_num, counts[num])


        total = 0
        for k ,v in counts.items():
            if v == max_num:
                total += v
            
        return total
        
        