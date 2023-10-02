#my thought process here is 
# exaple 1: nums = [2,7,11,15]
# n = len(nums) which means n = 4
# and the target = 9
# so that means it has to go throught the array

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1): #[15,11,]
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]