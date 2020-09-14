# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board[2][2]
board[2][1]


#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

#         rows-n ,and columns-m
        n, m = len(board), len(board[0])

#         二维数组来存取是否改字符已经用过
        mark = [[0] * m  for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.back_track(i, j, board, word[1:], mark) == True:
                        return True
                    else:
                        mark[i][j] = 0
        return False
#          递归的话，每一次算word的下一个数字


#       directions  上， 右， 下，左
    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    def back_track(self, i, j, board, word, mark):
#         回溯结束判断
        if len(word) == 0:
            return True
        print(mark)
        for direct in self.directions:
            # i 控制行，所以index要在y轴上相加； j控制列，所以index要在x轴上相加减
            cur_i = i + direct[1]
            cur_j  = j  + direct[0]

            #判断是否越界
            if 0 <= cur_i <len(board)  and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
            #判断是否用过
                if mark[cur_i][cur_j]  == 1:
                    continue

                mark[cur_i][cur_j] = 1
                if self.back_track(cur_i, cur_j, board, word[1:], mark) == True:
                    return True
                else:
                    mark[cur_i][cur_j] = 0
        return False


s=Solution()
s.exist(board, "ABCCED")
