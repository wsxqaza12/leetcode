class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = list('aeiou')
        bool_s = [x in vowels for x in s]

        max_sub = curr_sub = sum(bool_s[:k])
        left = 0

        for i in range(k, len(s)):
            curr_sub = curr_sub - bool_s[left] + bool_s[i]
            max_sub = max(max_sub, curr_sub)
            left += 1

        return max_sub
