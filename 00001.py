# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_index = {}
        duplicate_index = {} # vai guardar um par de índices duplicados

        # preenche dicionário de índices:
        for i in range(0, len(nums)):
            if nums[i] not in dic_index:
                dic_index[nums[i]] = i
            else:
                if nums[i] not in duplicate_index:
                    duplicate_index[nums[i]] = [dic_index[nums[i]], i]

    
        nums.sort()
        i = 0
        j = len(nums)-1
       
        while i < j:
            currentSum = nums[i] + nums[j]
            if currentSum < target:
                i += 1
            elif currentSum > target:
                j -= 1
            else:
                if nums[i] == nums[j]:
                    return duplicate_index[nums[i]]
                else:
                    return [dic_index[nums[i]], dic_index[nums[j]]]
