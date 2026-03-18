# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        elif n == 3:
            return 1
        
        primes = []
        if n%2 == 0:
            primes = [False]*2+[True]*2 + [False, True]*(n//2-2)
        else:
            primes = [False]*2+[True]*2 + [False, True]*(n//2-2) + [False]

        for i in range(3, int(sqrt(n))+1,2):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False

        return sum(primes)
