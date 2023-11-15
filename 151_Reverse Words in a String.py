class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        temp = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                temp += s[i]
                if i == len(s)-1:
                    words.insert(0, temp)
            elif s[i] == " " and temp != "":
                words.insert(0, temp)
                temp = ""

        return " ".join(words)


####  Method 2 ########


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return ' '.join(words[::-1])
