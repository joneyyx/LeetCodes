# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1, n+1):
            if i %15 == 0:
                lst.append("FizzBuzz")
            elif i % 5 == 0:
                lst.append("Buzz")
            elif i % 3 == 0:
                lst.append("Fizz")
            else:
                lst.append(str(i))
        return lst
s = Solution()
s.fizzBuzz(15)
