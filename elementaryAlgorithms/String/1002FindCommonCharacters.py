# Given an array A of strings made only from lowercase letters,
# return a list of all characters that show up in all strings within the list (including duplicates).For example,
# if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
#
# You may return the answer in any order.
#
#
# Example 1:
#
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dict = {}
        for word in A[0]:
            for wd in word:
                dict[wd]  = dict.get(wd, 0) + 1
        print(dict)


        for new_word in A[1:]:
            temp_dict = {}
            for wd in new_word:
                temp_dict[wd] = temp_dict.get(wd, 0) + 1
            print("temp", temp_dict)

            for k1 in dict:
                if k1 in temp_dict and dict[k1] >= temp_dict[k1]:
                    dict[k1] = temp_dict[k1]
                if k1 not in temp_dict:
                    dict[k1] = 0
        print(dict)

        res = []
        for k in dict:
            res += k * dict[k]
        return res


s = Solution()
A=["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
s.commonChars(A)

from collections import Counter
A=["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = None
        for a in A:
            c = Counter(a)
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())

from collections import Counter
temp = Counter(A)


