# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        size_dic = {1: "IV", # unidade (1,5)
                    2: "XL", # dezena  (10, 50)
                    3: "CD"  # centena (100, 500)
                    }
                    
        subtractive = {1: ("IV", "IX"),  # 4 9
                       2: ("XL", "XC"), # 40 90
                       3: ("CD", "CM")   # 400 900
                       }
        
        roman = ""
        numString = str(num)
        n = len(numString)
        size = n
        if size == 4:
            roman += "M"*int(numString[0])
            i = 1
            size -= 1
        else:
            i = 0
    
        while i < n:
            digit = int(numString[i])
            if digit == 0:
                pass
            elif digit < 4:
                roman += digit*size_dic[size][0]
            elif 4 < digit < 9:
                roman += size_dic[size][1]
                if digit > 5:
                    roman += (digit-5)*size_dic[size][0]
            elif digit == 4:
                roman += subtractive[size][0]
            else:  # digit == 9
                roman += subtractive[size][1]
            
            i += 1
            size -= 1

        return roman
