class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for num in s:
            if num != '*':
                stack += num
            elif num == '*':
                stack.pop()

        return ''.join(stack)
