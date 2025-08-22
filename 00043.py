# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        charToInt = { str(i) : ord(str(i))-48 for i in range(10) }
        num1_res = 0
        num2_res = 0
        num1_mag = 0 # magnitude atual
        num2_mag = 0 # magnitude atual

        if len(num1) > len(num2):
            i = len(num1)-1
            while i > len(num2)-1:
                num1_res += charToInt[num1[i]]*10**num1_mag
                num1_mag += 1
                i -= 1
        else:
            i = len(num2)-1
            while i > len(num1)-1:
                num2_res += charToInt[num2[i]]*10**num2_mag
                num2_mag += 1
                i -= 1

        while i >= 0:
            num1_res += charToInt[num1[i]]*10**num1_mag
            num2_res += charToInt[num2[i]]*10**num2_mag
            num1_mag += 1
            num2_mag += 1
            i -= 1

        return str(num1_res * num2_res)
