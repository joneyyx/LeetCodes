# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


# 方法1. 看index，如果左右数起的index都一样那就说明唯一值

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for wd in s:
#             if s.find(wd) == s.rfind(wd):
#                 return s.index(wd)
#         return  -1




# 方法2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        # 记录字符出现次数
        for c in s:
            # dic[c] = dic[c] + 1 if c in dic else 1
            dic[c] = dic.get(c, 0) + 1
            dic.items()
        # 过滤出现次数不为一的字符
        unique_chars = [ k for k, v in filter(lambda kvp: kvp[1] == 1, dic.items())]
        # 遍历目标字符串，返回首个出现在unique_chars中的字符的索引
        for i, c in enumerate(s):
            if c in unique_chars:
                return i
        return -1

s=Solution()
str = "leetcode"
print(s.firstUniqChar(str))

