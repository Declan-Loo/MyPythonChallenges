#Initialises a list
MyList = [9,7,5,435,3,423,432,43,9]
n = len(MyList) - 1

changes = 0
for i in range(0,n+1):
    for j in range(0,n):
        #Compares if the previous element is greater than the next element
        if MyList[j] > MyList[j+1]:
            #Create a temporary variable that stores the previous element
            Temp = MyList[j]
            #The element accessed by the index is changed to the next element (accessed by index+1)
            MyList[j] = MyList[j+1]
            #Earlier element is 
            MyList[j+1] = Temp
            #Increment changes - to show how many swaps happen
            changes+= 1
    n -= 1

print(*MyList,sep=",")
print("Number of changes:",changes)
