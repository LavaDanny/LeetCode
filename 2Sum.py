# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        
        hash = {}
        
        for x in range(len(nums)):
            if nums[x] in hash:
                return [hash[nums[x]], x]
            else:
                hash[target - nums[x]] = x  # {num we're looking for : index of first number}
            
            
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        