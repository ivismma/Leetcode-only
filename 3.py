# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        strset = {s[0]}
        i = 0
        j = 1
        largestSize = 1

        while j < len(s):
            previousSize = len(strset)
            strset.add(s[j])
            if len(strset) == previousSize:
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        j += 1
                        break
                    else:
                        strset.discard(s[i])
                        i += 1
            else:
                j += 1
                if len(strset) > largestSize:
                    largestSize = len(strset)
            
            if len(strset) > largestSize:
                largestSize = len(strset)
        
        return largestSize


print(Solution.lengthOfLongestSubstring(None, "dvdf"))
