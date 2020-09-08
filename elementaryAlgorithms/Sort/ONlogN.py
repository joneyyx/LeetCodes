# quick sort form single side
def quick_sort(start_index, end_index, array):
    # 递归结束条件，start_index >= end_index
    if start_index >= end_index:
        return

    # get piovt_index
    pivot_index = partition_v2(start_index,end_index,array)

    quick_sort(start_index, pivot_index-1, array)
    quick_sort(pivot_index+1, end_index, array)


def partition_v2(start_index, end_index, array):
    # get the first element as piovt
    pivot = array[start_index]

    #!!!!mark index
    mark = start_index

    for i in range(start_index+1 , end_index+1):
        if array[i] <pivot:
            # 当元素小于pivot的时候， mark +1 ，并且mark+1 的值与元素兑换
            mark += 1
            p = array[mark]
            array[mark] = array[i]
            array[i] = p
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark
