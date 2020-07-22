# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
# Example:
#
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return 1

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l ,r = 1 , n
        while l < r:
            mid = l + (r-l)/2
            # 发现错误版本，往左走寻找更旧的错误版本
            if isBadVersion(mid):
                r = mid
            # 没发现错误版本，需要往右走
            else:
                l = mid + 1
        return l













#         if n%2 == 1:
#             state = isBadVersion((n+1)/2)
#             # state is False(不是错误的版本)=》往右边找
#             if not state:
#
#         elif:
#             state = isBadVersion(n/2)
#
#         # odd
#         # (n+1)/2
#         if n%2 == 1:
#             return 1
#
#
# s = Solution()
# s.firstBadVersion(5)
#
#
#         # even