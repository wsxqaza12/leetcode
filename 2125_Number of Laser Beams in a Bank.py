class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = 0
        total = 0
        for nums in bank:
            line = nums.count("1")
            if line != 0:
                total += pre*line
                pre = line
        return total