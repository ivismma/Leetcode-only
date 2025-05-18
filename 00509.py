# https://leetcode.com/problems/fibonacci-number/

# usando prog. dinâmica e memoização

class Solution:
    fibCache = {} # armazenar fib(n) p/ todo n computado

    def fib(self, n: int) -> int:
        if n in Solution.fibCache:
            return Solution.fibCache[n]
        
        if n <= 1:
            return n
        
        Solution.fibCache[n] = self.fib(n-1) + self.fib(n-2)
        return Solution.fibCache[n]
