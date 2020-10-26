def reverseChess(board, targe):
    row_idx = len(board) - 1
    col_idx = len(board[0]) - 1
    for cp in targe:
        i = cp[0] - 1
        j = cp[1] - 1

        if i - 1 >= 0 and i - 1 <= row_idx and j >= 0 and j <= col_idx:
            swap(board, i-1, j)
        if i + 1 >= 0 and i + 1 <= row_idx and j >= 0 and j <= col_idx:
            swap(board, i+1, j)
        if i >= 0 and i <= row_idx and j-1 >= 0 and j-1 <= col_idx:
            swap(board, i, j-1)
        if  i >= 0 and i <= row_idx and j+1 >= 0 and j+1 <= col_idx:
            swap(board, i, j+1)
        print(board)

    return board


def swap(board, i, j):
    if board[i][j]== 1:
        board[i][j] = 0
    else:
        board[i][j] = 1
if __name__ == '__main__':
    array = eval(input())
    position = eval(input())
    reverseChess(array, position)



#
#
# reverseChess([[0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]],
#              [[2, 2], [3, 3], [4, 4]])



import sys


def serachMountani(nums):
    # line = sys.stdin.readline()
    # print(line)
    # line = sys.stdin.readline()
    # nums = list(map(int, line.split()))
    print("nums:", nums)
    for i in range(len(nums[:-2]), -1, -1):
        if nums[i]>nums[i+1] and nums[i] > nums[i-1]:

            return(i)
if __name__ == '__main__':
    array = list(map(int, input().split()))
    serachMountani(array)
