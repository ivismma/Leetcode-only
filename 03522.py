# https://leetcode.com/problems/calculate-score-after-performing-instructions/description/
# (Leetcode Weekly Contest 446)

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        n = len(values)
        executed = set()

        i = 0
        while i < n:
            if i in executed:
                break
            executed.add(i)
            v = values[i]

            if len(instructions[i]) == 3:
                score += v
                i += 1
            else:
                i += v
                if i not in range(n):
                    break
        
        return score
