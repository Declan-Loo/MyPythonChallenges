def BinarySearch(arr, num, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            return BinarySearch(arr, num, mid+1, high)
        else:
            return BinarySearch(arr, num, low, mid-1)
        
my_list = [2,3,5,5,5,6,4,22,1,3]

print(BinarySearch(sorted(my_list), 22, 0, len(my_list)-1))
