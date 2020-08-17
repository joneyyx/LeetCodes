# 1，1，2，3，5，8，13，21
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(9)

from typing import List


def coinChange(coins: List[int], amount: int):
    memo = {}

    def dp(n):
        # 查找备忘录里面是否有
        if n in memo:
            return memo.get(n)

        if n == 0:
            return 0
        if n < 0:
            return -1

        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)

            res = min(res, subproblem + 1)

        return res if res != float('inf') else -1

    return dp(amount)


coinChange([1, 3, 5], 11)

import numpy as np

def checkDistance(c: List, ll: List[List]):
    tmp = 100
    res = []
    for i in range(len(ll)):
        dist = abs((c[0] - ll[i][0])**2 + (c[1] - ll[i][1])**2)
        # print(c[0], c[1])
        # print(ll[i][0], ll[i][1])
        # print((c[0] - ll[i][0]) , (c[1] - ll[i][1]))
        print(dist)
        if dist < tmp:
            tmp = dist
            res.append(i)

    print(res, tmp)


# if __name__ == '__main__':
    # checkDistance([3, 1], [[1, 2], [-3, 0], [4, 2]])
import re
string = "professor sjsjj entry 12 zhq st"
result = re.findall(".*\d+(.*?)(st.|rd.).*", string)
result

p = re.compile('(?<=\d ).*(?= st.|rd.)')
str = "professor sjsjj entry 113 zhq hgh st. jj"
p.search(str).group()

p = re.compile("(\d+.?\d*)(.*?)(st.|rd.)")

reg = re.findall(r'(?<=\d ).*?(?= st.|rd.)', str)
reg