# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        isNegative = True if x < 0 else False
        x = abs(x)
        
        i = 0
        while x != 0:
            digits.append(x%10)
            x = x//10
            i += 1

        j = 0
        while j < len(digits):
            if digits[0] == 0:
                digits = digits[1:]
            else:
                break

        reversedNumber = 0
        power = len(digits)-1
        for dig in digits:
            reversedNumber += dig*(10**power)
            if reversedNumber > 2147483647 or reversedNumber < -2147483648:
                return 0
            power -= 1

        return reversedNumber if not(isNegative) else -reversedNumber
