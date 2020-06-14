# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.


# class Solution:
#     def myAtoi(self, str: str) -> int:
#         maxbound = 2 ** 31
#         minbound = - 2** 31
#         print(maxbound)
#         result = ""
#         i = 0
#         while i < len(str):
#             if str[i] != " ":
#                  if str[i] == "-" or str[i] == "+":
#                      for k in (i+1,len(str)):
#                         if str[k].isdigit():
#                             result = result + str[k]
#                         else:
#                             break
#                      if str[i] == "-" and (-result) > minbound:
#                          return -result
#                      if str[i] == "+" and result < maxbound:
#                          return result
#                  if str[i].isalpha():
#                      return 0
#             else:
#                 i += 1
#
# S = Solution()
# str = "42"
# print(S.myAtoi(str))
#                 -       +/-          digital    alpha
# 'start':    ['start', 'signed', 'in_number',    'end'],
# 'signed':    ['end', 'end',     'in_number',    'end'],
# 'in_number': ['end', 'end', '   in_number',     'end'],
# 'end':       ['end', 'end',     'end',          'end'],




# # 自动机，现在状态+下一个字 => 下一个状态
# INT_MAX = 2 ** 31 - 1
# INT_MIN = -2 ** 31
#
#
# class AutoMachine:
#
#     def __init__(self):
#         self.result = 0
#         self.state = 'start'
#         #sign is 正负系数
#         self.sign = 1
#         self.table = {
#             'start': ['start', 'signed', 'in_number', 'end'],
#             'signed': ['end', 'end', 'in_number', 'end'],
#             'in_number': ['end', 'end', 'in_number', 'end'],
#             'end': ['end', 'end', 'end', 'end'],
#         }
#
#     def get_col(self, c):
#         if c.isspace():
#             return 0
#         if c == '+' or c == '-':
#             return 1
#         if c.isdigit():
#             return 2
#         else:
#             return 3
#
#     def getTable(self, c):
#         self.state = self.table[self.state][self.get_col(c)]
#         if self.state == 'in_number':
#             self.result = self.result * 10 + int(c)
#             if self.sign == 1:
#                 self.result = min(self.result, INT_MAX)
#             else:
#                 # 现在要取小的，因为现在都是正数，还没有乘符号
#                 self.result =  min(self.result, -INT_MIN)
#         if self.state == 'signed':
#             self.sign = 1 if c == '+' else -1
#
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         automachine = AutoMachine()
#         for c in str:
#             automachine.getTable(c)
#         return automachine.sign * automachine.result
#
# s = Solution()
# print(s.myAtoi('4193 with words'))



# 正则匹配
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2 ** 31 -1
        INT_MIN = - 2 ** 31
        st = str.strip()
        # complile设置正则的规则
        reg_rule = re.compile(r'^[ ]*([+-]?\d+)')
        reg = re.match(reg_rule, st)
        if reg:
            result = int(reg.group(0))
            return max(min(result, INT_MAX), INT_MIN)
        else:
            return 0


s=Solution()




