# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        #m行，n列
        m, n = len(matrix), len(matrix[0])

        res = []
        #起始点
        left, top, right, bottom = 0, 0, len(matrix[0])-1, len(matrix)-1

        while True:
            #>>>>>>>>从左到右，到达之后top+1
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top += 1
            #边界条件
            if top > bottom:
                break
            #>>>>>>>从上倒下，到达之后right-1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            #边界条件
            if right < left:
                break
            #>>>>>>>从右到左，到达之后bottom-1
            for j in range(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
            if bottom < top:
                break
            #>>>>>>>从下到上，到达之后left+1
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res



