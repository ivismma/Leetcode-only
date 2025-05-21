# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsAffected = set() # linhas a serem zeradas
        colsAffected = set() # colunas a serem zeradas
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsAffected.add(i)
                    colsAffected.add(j)
        
        for i in rowsAffected:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for j in colsAffected:
            for i in range(len(matrix)):
                matrix[i][j] = 0
