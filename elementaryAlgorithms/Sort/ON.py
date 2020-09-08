# 1.  冒泡排序
def bubble_sort_v1(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

bubble_sort_v1([3,4,14,1,5,6,7,8,1,-1,0,9,11])

# 到最后几轮如果不变化的情况下，就可以直接跳出循环
def bubble_sort_v2(array):
    for i in range(len(array)-1):
        is_sorted = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                is_sorted = False
        if is_sorted:
            break
    return array


def bubble_sort_v3(array):
    # 记录最后一次改变顺序的位置, 说明之后的数都是有序的。 之前的都是无序数列
    last_index = 0
    # initialize =>boarder
    boarder = len(array)-1
    for i in range(len(array)-1):
        is_sorted = True
        for j in range(boarder):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                is_sorted = False
        #         最后一次交换的index记录，说明之前的都是无序的。 下次就做前面那些就可以了
                last_index = j
        boarder = last_index
        if is_sorted:
            break
    return array