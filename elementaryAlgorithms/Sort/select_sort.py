# 选择排序和冒泡排序很类似，但是选择排序每轮比较只会有一次交换，而冒泡排序会有多次交换，交换次数比冒泡排序少，就减少cpu的消耗，所以在数据量小的时候可以用选择排序，实际适用的场合非常少。
#
# 比较性：因为排序时元素之间需要比较，所以是比较排序
#
# 稳定性：因为存在任意位置的两个元素交换，比如[5,  8, 5, 2]，第一个5会和2交换位置，所以改变了两个5原来的相对顺序，所以为不稳定排序。
#
# 时间复杂度：我们看到选择排序同样是双层循环n*(n-1))，所以时间复杂度也为：O(n^2)
#
# 空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1)

def select_sort(array):
    for i in range(len(array)):
        min_index= i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    print(array)
    return array

select_sort([5,8,2,5])