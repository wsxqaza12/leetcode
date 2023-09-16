class Solution(object):
    def commonChars(self, words):
        hash = [0] * 26
        result = []

        for i, letter in enumerate(words[0]):
            hash[ord(letter) - ord('a')] += 1

        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in range(len(words[1])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1
                
            for letter in range(26):
                hash[letter] = min(hash[letter], hashOtherStr[letter])

        for i in range(26):
            while hash[i] != 0:
                result.extend(chr(i + ord('a')))
                hash[i] -= 1
        return result