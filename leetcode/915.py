"""
    https://leetcode.com/problems/partition-array-into-disjoint-intervals/
    915. Partition Array into Disjoint Intervals (medium)
"""

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        maxleft = [None] * N
        minright = [None] * N
        
        max = nums[0]
        for i in range(N):
            if max < nums[i]:
                max = nums[i]
            maxleft[i] = max
            
        min = nums[-1]
        for i in range(N-1, -1, -1):
            if min > nums[i]:
                min = nums[i]
            minright[i] = min
        
        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
    