# Write your code here :-)
alist = [5,4,7,3,1,2,10,31,57,41,61]

def insertionSort(alist):
    #Iterates over the list
    for index in range(1,len(alist)):
        #sets the current value to be the content of the array in the index position
        currentvalue = alist[index]
        
        #Set the position as the index
        position = index
        
        #Print the list
        print(alist)
        
        #Checks if the previous element is greater than the current element
        while (position>0) and (alist[position-1] > currentvalue):
            #Inserts the elements
            alist[position] = alist[position-1]
            position -= 1
        #The element in the list is now set to the current value
        alist[position] = currentvalue
    
#Access the function
insertionSort(alist)
