class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        A_count = 0
        B_count = 0

        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    A_count += 1
                else:
                    B_count += 1

        if A_count > B_count:
            return True
        else:
            return False
