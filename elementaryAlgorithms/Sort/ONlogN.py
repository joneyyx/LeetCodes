#>>>>>>>>>>>>>>>>>>>>>>quick sort form single side
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>归并排序
def merge(left, right):
    res = []
    p, q = 0 , 0
    #当list是>1
    while p < len(left) and q < len(right):
        if left[p] < right[q]:
            res.append(left[p])
            p += 1
        else:
            res.append(right[q])
            q += 1
    #当左右两个排序后的数组，左边排序完了，右边的直接入站
    if p == len(left):
        while q < len(right):
            res.append(right[q])
            q += 1
    else:
        while p < len(left):
            res.append(left[p])
            p += 1
    return res

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

if __name__ == '__main__':
    merge_sort([4,3,2,1,7,5,6,9])