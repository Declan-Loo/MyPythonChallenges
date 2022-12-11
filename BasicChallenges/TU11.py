import tkinter # imports main library
import random # For random functions
window = tkinter.Tk() #so that there's less confusing brackets

def RandomName():
    NameChoice = random.choice(name_list)
    name_picked.configure(text="Name picked: " + str(NameChoice))

name_list = []
done = "No"
while done.lower() != "yes":
    names = input("Name?: ")
    names.append(name_list)
    done  = input("Done? (yes/no): ")

MyTitle = tkinter.Label(window, text="Random Name Generator",font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="OK", command=RandomName) 
MyButton.pack()
name_picked = tkinter.Label(window, font="Helvetica 16 bold")
name_picked.pack()
window.mainloop()
