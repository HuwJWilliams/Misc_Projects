from tkinter import *

window = Tk()

window.title("My first GUI")
window.minsize(width=200, height=100)
window.config(padx=10, pady=20)


def calculate():
    km = round(float(input.get()) * 1.609, 1)
    label3.config(text=km)


# Calculate Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Entry
input = Entry(width=5)
input.grid(column=1, row=0)

# Labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="km")
label4.grid(column=2, row=1)


window.mainloop()
