#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 把输入的值，列表化
        s_list = list(s)
        # 定义字典
        kuohao = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        cao = []
        if len(s_list)%2 != 0:
            return False
        # ! 遍历s
        for i in s:
            # 先遍历所有的值，判断值是否在属于右括号，如果不属于，则放入槽中
            # 如果属于右括号，则判断槽中的最后一位和现在的右括号是否相对应
            # 如果对应，则删除槽的最后一位，如果不对应且槽里有值则直接报错，不对应且槽里无值则跳过
            #print("当前的i为：{0}，槽为：{1}".format(i,cao))
            if i in kuohao:
                if not cao or cao[-1] != kuohao[i]:
                    return False
                else:
                    cao.pop()
            else:
                cao.append(i)
        #print("最后的槽为：",cao)
        return not cao

# @lc code=end

