class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        loss = defaultdict(int)

        for match in matches:
            win[match[0]] += 1
            loss[match[1]] += 1

        not_lost = []
        one_lost = []

        for k, v in win.items():
            if v > 0 and loss[k] == 0:
                not_lost.append(k)
        
        for k, v in loss.items():
            if v == 1 and win[k] >= 0:
                one_lost.append(k)

        not_lost.sort()
        one_lost.sort()
        return [not_lost, one_lost]
