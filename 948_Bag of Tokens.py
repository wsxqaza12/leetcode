class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        if len(tokens) == 0 or power < tokens[0]:
            return score
            
        while len(tokens) != 0:
            if power >= tokens[0]:
                power -= tokens.pop(0)
                score += 1
            elif score > 0 and len(tokens) != 1:
                power += tokens.pop()
                score -= 1
            else:
                break
        
        return score