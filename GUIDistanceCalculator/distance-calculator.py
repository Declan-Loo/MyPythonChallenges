import tkinter
 
#Initialises a Tkinter object
window = tkinter.Tk()

#Creates a title for the Tkinter window 
window.wm_title("Metres/Kilometres/Miles/Yards converter")
Base_Number=""
 
def evaluate(event):
    #Checks if the user selects Metres as the option
    if Base_Number == "Metres":
        try:
            metres = float(Myentry.get())
            kilometres = round(metres/1000,5)
            miles = (metres/1609.34,5)
            yards = round(metres*1.09361,5)
            result1.configure(text = "Kilometres is: "+str(kilometres))
            result2.configure(text = "Miles is: "+str(miles))
            result3.configure(text = "Yards is: "+str(yards))

        except ValueError:
            result1.configure(text = "Please enter valid metre value")
            result2.configure(text = "")
 
    elif Base_Number == "Kilometres":
        try:
            kilometres = float(Myentry.get())
            metres = round(kilometres*1000,5)
            miles = round(kilometres/1.60934,5)
            yards = round(kilometres*1093.61,5)
            result1.configure(text = "Metres is: "+str(metres))
            result2.configure(text = "Miles is: "+str(miles))
            result3.configure(text = "Yards is: "+str(yards))
        except ValueError:
            result1.configure(text = "Please enter valid kilometre value")
            result2.configure(text = "")
 
    elif Base_Number == "Miles":
        try:
            miles = float(Myentry.get())
            metres = round(miles*1609.34,5)
            kilometres = round(miles*1.60934,5)
            yards = round(miles*1760,5)
            result1.configure(text = "Metres is: "+str(metres))
            result2.configure(text = "Kilometres is: "+str(kilometres))
            result3.configure(text = "Yards is: "+str(yards))
        except ValueError:
            result1.configure(text = "Please enter valid mile value")
            result2.configure(text = "")

    elif Base_Number == "Yards":
        try:
            yards = float(Myentry.get())
            metres = round(yards/1.09361,5)
            kilometres = round(yards/1093.61,5)
            miles = round(yards/1760,5)
            result1.configure(text = "Metres is: "+str(metres))
            result2.configure(text = "Kilometres is: "+str(kilometres))
            result3.configure(text = "Miles is: "+str(miles))
        except ValueError:
            result1.configure(text = "Please enter valid yard value")
            result2.configure(text = "")
    else:
        result1.configure(text = "Please select an appropriate UNIT!")
 
def calcStyle():
    global Base_Number
    Base_Number=base.get()
    print(base.get())
 
MyTitle = tkinter.Label(window, text="Metres/Kilometres/Miles/Yards converter")
MyTitle.pack()
 
Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()
 
result1 = tkinter.Label(window, text="1. Choose a unit")
result1.pack()
 
result2 = tkinter.Label(window, text="2. Enter a number and press<enter>")
result2.pack()

result3 = tkinter.Label(window)
result3.pack()
 
base = tkinter.StringVar()

#Four radio buttons to indiciate Metres, Kilometres, Miles or Yards, so conversion can be applied
tkinter.Radiobutton(window, text="Metres", variable=base, value="Metres", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Kilometres", variable=base, value="Kilometres", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Miles", variable=base, value="Miles", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Yards", variable=base, value="Yards", command=calcStyle).pack()

window.mainloop()
