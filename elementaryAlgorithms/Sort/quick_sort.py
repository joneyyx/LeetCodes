def quick_sort(start_idx, end_idx, array):
    if start_idx > end_idx:
        return

    pivot_idx = partition(start_idx, end_idx, array)
    quick_sort(start_idx, pivot_idx-1, array)
    quick_sort(start_idx, pivot_idx+1, array)



def partition(start_idx, end_idx, array):
    pivot = array[start_idx]
    mark =  start_idx
    for i in range(start_idx+1, end_idx+1):
        if array[i] < pivot:
            mark += 1
            p = array[i]
            array[i] =array[mark]
            array[mark] = p
    array[start_idx] = array[mark]
    array[mark] =pivot
    return mark