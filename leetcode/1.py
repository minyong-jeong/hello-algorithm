"""
    https://leetcode.com/problems/two-sum/
    1. Two Sum (easy)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in dic:
                return [dic[tmp], i]
            dic[nums[i]] = i