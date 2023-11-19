class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for aste in asteroids:
            while stack and stack[-1] > 0 > aste:
                if stack[-1] < abs(aste):
                    stack.pop()
                    continue
                elif stack[-1] == abs(aste):
                    stack.pop()
                break
            else:
                stack.append(aste)

        return stack
