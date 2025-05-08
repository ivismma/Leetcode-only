# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_freq = {}
        for number in nums:
            if number not in num_freq:
                num_freq[number] = 1
            else:
                num_freq[number] += 1
        
        keys_tuple = tuple(num_freq.keys())
        for key in keys_tuple:
            if num_freq[key] == 1:
                return key
