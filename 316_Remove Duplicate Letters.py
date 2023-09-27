class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        dict = [0] * 26
        stack = []

        for letter in s:
            dict[ord(letter) - ord('a')] += 1

        for letter in s:
            if stack and letter == stack[-1]:
                dict[ord(letter) - ord('a')] -= 1

            elif letter not in stack:
                while stack and stack[-1] > letter and dict[ord(stack[-1]) - ord('a')] > 0:
                    letter_s = stack[-1]
                    stack.remove(letter_s)
                    # dict[ord(letter_s) - ord('a')] -= 1

                stack.append(letter)
                dict[ord(letter) - ord('a')] -= 1

            else:
                dict[ord(letter) - ord('a')] -= 1

        return "".join(stack)
