#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(0,len(nums)+1):
            for j in range(a+1,len(nums)):
                if int(nums[a])+int(nums[j]) == target:
                    return a,j
        a = a + 1
# @lc code=end

