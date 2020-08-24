# 题目描述
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# >>>>>>思路从左下或者右上开始2分

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 二维数组的长度=》二维数组有几行
        row = len(array)
        # 二维数组第一个元素的长度=>二维数组有几列
        column = len(array[0])
        if row == 0 or column == 0:
            return False

        # 左下角的横坐标，纵坐标
        r, c = row-1, 0
        while r >=0 and c <=column-1:
            if target == array[r][c]:
                return True
            elif target < array[r][c]:
                r = r-1
            else:
                c = c +1
        return False


ary = [[0 for i in range(5)] for j in range(6)]
len(ary[0])
