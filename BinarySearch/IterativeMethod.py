def BinarySearch2(arr, num):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False
