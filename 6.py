# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        # listas das linhas (a 1a ja começa com s[0]
        rowcharacters = [[s[0]]]
        # inicializa listas vazias
        for i in range(1, numRows):
            rowcharacters.append([])

        i = 1 # caracter atual da string
        finished = False
        
        while True:
            for j in range(1, numRows):
                rowcharacters[j].append(s[i])
                i += 1
                if i == len(s):
                    finished = True
                    break

            if finished: break
            
            j = numRows-2
            while j >= 0:
                rowcharacters[j].append(s[i])
                i += 1
                if i == len(s):
                    finished = True
                    break
                j -= 1

            if finished: break

        for i in range(1, numRows):
            rowcharacters[0].extend(rowcharacters[i])
            
        return ''.join(str(c) for c in rowcharacters[0])
