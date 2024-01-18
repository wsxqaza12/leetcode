class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)

        step = 0
        two = 0
        one = n
        while one >= 0:
            step += factorial(one+two)/factorial(one)/factorial(two)

            one -= 2a
            two += 1
            
        return int(step)


# DP
class Solution:
def climbStairs(self, n: int) -> int:

    step = {}
    step[0] = 1
    step[1] = 2

    for i in range(2, n):
        step[i] = step[i-1] + step[i-2]

    return step[n-1]

            