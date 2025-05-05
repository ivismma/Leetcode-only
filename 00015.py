# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        triplets = []

        i = 0
        n = len(nums)
        while i < n-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue # pular nº's repetidos
            
            j = i+1
            k = n-1
            while j < k:
                currentSum = nums[i]+nums[j]+nums[k]
                if currentSum > 0:
                    k -= 1
                elif currentSum < 0:
                    j += 1
                else:
                    triplets.append((nums[i], nums[j], nums[k]))
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1  # pular nº's repetidos
            
            i += 1

        return triplets
