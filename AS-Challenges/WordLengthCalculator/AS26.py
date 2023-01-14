word_length = 0
word_count = 0
with open("rudyard.txt","r") as whole_file:
   for line in whole_file:
    if line != "\n":
      words = line.split()
      for i in range(len(words)):
        for letters in words:
          if letters.isalpha() == True:
            word_length += 1
        word_count += 1
    print(line,end="")
print("\n")
print(f"The average word count is: {word_length/word_count}")
