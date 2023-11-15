class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s)-1
        vowels = list('aeiouAEIOU')
        list_s = list(s)

        while left < right:
            while left < right and list_s[left] not in vowels:
                left += 1
            while left < right and list_s[right] not in vowels:
                right -= 1

            if left == right or left > len(s)-1 or right < 0:
                break

            list_s[right], list_s[left] = list_s[left], list_s[right]
            left += 1
            right -= 1

        return ''.join(list_s)
