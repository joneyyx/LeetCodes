from typing import List


#
# N = 3, W = 4
# wt = [2, 1, 3]
# val = [4, 2, 3]
# 算法返回 6，选择前两件物品装进背包，总重量 3 小于W，可以获得最大价值 6

def bag(N: int, W: int, wt: List[int], val: List[int]):
    # 技巧:python 生成二维数组(数组)通常先生成列再生成行
    # 内循环在前，外循环在后
    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]
    print(dp)

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            #             背包j，装不下第i个物品，所以就不选他。 用的是第i-1个物品
            #              对于数组wt，第i个物品应该是index： i-1
            if j < wt[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                # 转入和不装，选max
                dp[i][j] = max(dp[i - 1][j - wt[i - 1]] + val[i - 1], dp[i - 1][j])

    for i in range(N + 1):
        for j in range(W + 1):
            print(dp[i][j], end='\t')
        print('\n')


import numpy as np

dd = np.zeros((4, 4))



# 二维数组进行一维优化。
#
def bag2(N: int, W: int, wt: List[int], val: List[int]):
    for i in range(N):
        for j in range(W, -1, -1):
            print(j, end='\t')
        print('\n')



if __name__ == '__main__':
    bag(3, 4, [2, 1, 3], [4, 2, 3])
    print("========================================")
    bag2(3, 4, [2, 1, 3], [4, 2, 3])
