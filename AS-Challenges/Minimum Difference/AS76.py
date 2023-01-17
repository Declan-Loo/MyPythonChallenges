"""
AS76	
50	
MINIMUM DIFFERENCE	

Output the minimum differences between any two numbers in an array:
eg.
Input
numbers = [1, 5, 7, 10, 12]

Output
2
"""

numbers = [1, 5, 7, 10, 12]

def MinimumDifference(arr):
    #Ensure array is sorted.
    arr.sort()
    #Big number which will be changed for minimum difference
    diff = 10**50
    #Iterate over array
    for i in range(len(arr)-1):
        #Difference:
        arr_diff = arr[i+1] - arr[i]
        #If difference calculated smaller than current minimum difference, set new difference as current minimum difference.
        if arr_diff < diff:
            diff = arr_diff
            
    return arr_diff

#Should get 2.
print(MinimumDifference(numbers))
