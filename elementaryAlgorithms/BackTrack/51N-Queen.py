from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res= []

        # 向下递归的只是棋盘的row。 至于col可以在每一次循环里做
        def back_track(board, row, n):
            if row == n:
                res.append(self.constructList(board)[:])
                return
                # print(board)

            for col in range(n):
                #约束条件->是否board[row][col]是valid
                if self.isValid(board, n, row, col):
                    board[row][col] = "Q"
                    back_track(board, row+1, n)
                    board[row][col] = "."

        back_track(board, 0, n)
        return res

    def isValid(self,board, n, row, col):
        #检查每一行是否是有重复的Q--->其实不用检测，因为每一行只放一个Q，所以比不会重复。
        #总共检查3种情况
        #1 每一列有没有冲突Q
        for i in range(n):
            if board[i][col] == "Q":
                return False
        #2 主对角线（左上-右下）：横-纵固定值===只要判断改数字的左上没有Q
        i1,j1 = row-1, col-1
        while i1 >=0 and j1 >=0 :
            if board[i1][j1] == "Q":
                return False
            i1 -= 1
            j1 -= 1
        #3 副对角线 （左下-右上）：横+纵固定值===只要判断该数字的右上没有Q
        i2,j2 = row-1, col+1
        while i2 >= 0 and j2 <  n:
            if board[i2][j2] == "Q":
                return False
            i2 -= 1
            j2 += 1
        return True

    def constructList(self,  board):
        final_list = []
        for sub_list in board:
            temp = "".join(sub_list)
            final_list.append(temp)
        return final_list

s=Solution()
s.solveNQueens(4)



