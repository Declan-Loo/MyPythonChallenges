#Function to get sum of digits.
def getSumofDigits(n):
    the_sum = 0
    for digit in str(n): 
        the_sum += int(digit)      
    return the_sum

neat_num_list = []
for i in range(101,1001):
    #Check if number is divisible by sum of digits.
    if i % getSumofDigits(i) == 0:
        #Add number of list if true
        neat_num_list.append(i)
        
#Print the list of neat numbers from 101 to 1000 (inclusive).
print("Here are the list of 3-digit neat numbers up to 1000: ")
for neat_nums in neat_num_list:
    print(neat_nums)
