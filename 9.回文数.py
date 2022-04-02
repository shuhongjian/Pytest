#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        list1 = []
        for i in x:
            list1.append(i)
        for j in range(0,len(list1)):
            if list1[j] != list1[-(j+1)]:
                print(list1[-(j+1)])
                print(list1[j])
                return False 
        return True
            
# @lc code=end

