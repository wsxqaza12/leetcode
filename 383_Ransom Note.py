class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash = [0]*26
        hash_Note = [0]*26

        for i, letter in enumerate(magazine):
            hash[ord(letter) - ord('a')] += 1

        for i, letter in enumerate(ransomNote):
            hash[ord(letter) - ord('a')] -= 1
            if hash[ord(letter) - ord('a')] < 0:
                return False
        
        return True
        
