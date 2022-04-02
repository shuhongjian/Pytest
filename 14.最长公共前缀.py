#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# @lc code=start
from typing import Counter


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 当strs为空时，返回空
        if len(strs) == 0:
            return strs
        # 当strs只有一个值时，返回这个唯一值
        if len(strs) == 1:
            return strs[0]
        # strs有多个时，进行比较,先把第一个定义为参考元素
        strs_XT = strs[0]
        
        i = 1
        while i < len(strs):
            # 因为第一个为参考元素，所以不用从0下标开始
            # 每次循环时，先将参考元素初始化为列表，保证每次都是最新的参考元素
            length = len(strs_XT)
            print("这是循环：",i)
            print("参考元素为：{0},length长为{1}".format(strs_XT,length))
            if strs[i].startswith(strs_XT):
                i = i + 1
            else:
                strs_XT=strs_XT[0:length-1]
                #print("length长度为：",length)
                length = length-1
            if length == 0:
                strs_XT = ""
                break
        return strs_XT


# @lc code=end