import random
prompts = []
with open("promptspal.txt","r") as file_1:
    for line in file_1:
        prompts.append(line)
    print(prompts[random.randint(0,len(prompts)-1)])
