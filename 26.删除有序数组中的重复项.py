#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            print(i)
            if i+1<len(nums):
                if nums[i] == nums[i+1]:
                    nums.remove(nums[i])
        print(nums)
        return len(nums)
        
# @lc code=end

