# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        max1 = len(word1)
        max2 = len(word2)

        i = 0
        if max1 > max2:
            while i < max2:
                string += word1[i] + word2[i]
                i += 1
            
            while i < max1:
                string += word1[i]
                i += 1
        else:
            while i < max1:
                string += word1[i] + word2[i]
                i += 1

            while i < max2:
                string += word2[i]
                i += 1
        
        return string
