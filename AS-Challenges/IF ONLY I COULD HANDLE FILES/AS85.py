count_1 = 0
count_2 = 0
with open("rudyard.txt","r") as file_1:
    for line in file_1:
        words = line.split()
        for word in words:
            if word == "if" or word == "If":
                count_1 += 1
with open("rudyard.txt","a") as file_1:
    file_1.write("\n"+ "Number of instances of 'if': "+str(count_1))
with open("mam.txt","r") as file_2:
    for line in file_2:
        words = line.split()
        for word in words:
            if word == "if" or word == "If":
                count_2 += 1
with open("mam.txt","a") as file_2:
    file_2.write("\n"+ "Number of instances of 'if': "+str(count_2))

print("Number of instances of 'if' in rudyard.txt: "+str(count_1))
print("Number of instances of 'if' in mam.txt: "+str(count_2))


if count_1 > count_2:
    print("'rudyard.txt' has more ifs than 'mam.txt'")
elif count_1 < count_2:
    print("'mam.txt' has more ifs than 'rudyard.txt'")
else:
    print("'rudyard.txt' has the same instances of ifs than 'mam.txt'")
