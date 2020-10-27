def binary_search(array, item):
    low , high = 0, len(array)-1
    while low <= high:
        mid = (high-low)//2 + low
        if item < array[mid]:
            high = mid - 1
        elif item > array[mid]:
            low = mid + 1
        else:
            return mid
    print("None")
mylist = [1,3,5,7,9]
print(binary_search(mylist, 3))
