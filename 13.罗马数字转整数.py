#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        #luoma_num = ['I','V','X','L','C','D','M']
        luoma_zhi = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        new_num = []
        out_num = 0
        for x in s:
            if x in luoma_zhi:
                new_num.append(luoma_zhi[x])
        

        for j in range(0,len(new_num)):
            print("执行计数")
            out_num = out_num + new_num[j]
            if j+1<len(new_num):
                if new_num[j]<new_num[j+1]:
                    out_num = out_num - 2*new_num[j]
            """
            if j+1<len(new_num):
                if new_num[j]>=new_num[j+1]:
                    out_num = out_num+new_num[j]+new_num[j+1]
                elif new_num[j]<new_num[j+1]:
                    out_num = new_num[j+1]-new_num[j]+out_num
            else:
                out_num = out_num + new_num[j]
            """
        print(new_num)
        return out_num
        

# @lc code=end

