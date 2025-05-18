# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        closestSum = nums[0]+nums[1]+nums[2]
        closestDiff = abs(target-closestSum)
        # var. p/ guardar diferença e evitar chamar abs(target-soma) em toda verificação.

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
                if currentSum > target:
                    k -= 1
                elif currentSum < target:
                    j += 1
                else:
                    return nums[i] + nums[j] + nums[k]
                if abs(target-currentSum) < closestDiff:
                    closestSum = currentSum
                    closestDiff = abs(target-currentSum)
            
            i += 1

        return closestSum
