# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [False, False] + [True]*(n-2)

        # invalidar todos os pares:
        for j in range(4, n, 2):
            primes[j] = False
        
        # para que eu possa pular de 2 em 2 aqui:
        for number in range(3, int(sqrt(n))+1, 2):
            if primes[number]:
                for j in range(number*number, n, number):
                    primes[j] = False
        
        return sum(primes)
