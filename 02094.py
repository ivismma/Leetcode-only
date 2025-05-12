# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = {i: 0 for i in range(10)}
        for number in digits:
            freq[number] += 1 
        
        result = [] # lista de números ímpares c/ 3 díg.
        for i in range(100, 1000, 2):
            currentFreq = {}
            currentFreq[i%10] = 1 # unidade
            
            d = i//10%10  # dezena
            if d not in currentFreq:
                currentFreq[d] = 1
            else:
                currentFreq[d] += 1
            
            c = i//100%10 # centena
            if c not in currentFreq:
                currentFreq[c] = 1
            else:
                currentFreq[c] += 1

            valid = True
            for number in currentFreq:
                if freq[number] - currentFreq[number] < 0:
                    valid = False
                    break
            if valid:
                result.append(i)

        return result
