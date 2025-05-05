# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        # Romano -> Decimal:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        value = 0
        i = len(s)-1
        while(i > 0):
            if s[i] in "VX":
                if s[i-1] == 'I':
                    value += dic[s[i]] - 1
                    i -= 2
                else:
                    value += dic[s[i]]
                    i -= 1
            elif s[i] in "LC":
                if s[i-1] == 'X':
                    value += dic[s[i]] - 10
                    i -= 2
                else:
                    value += dic[s[i]]
                    i -= 1
            elif s[i] in "DM":
                if s[i-1] == "C":
                    value += dic[s[i]] - 100
                    i -= 2
                else:
                    value += dic[s[i]]
                    i -= 1
            else:
                value += dic[s[i]]
                i -= 1
        # se i = 0 retorna valor. se i = 1, ret valor atual + 1º caracter.
        return value + dic[s[0]] if i == 0 else value  
